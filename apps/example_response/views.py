import os
import re

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import Template
from django.template.engine import Engine

from . import models

static_response_template_dir = "static_responses"
dynanmic_response_template_dir = "dynamic_responses"
template_engine = Engine.get_default()
dr_404 = "dynamic_response_not_found.html"


def _after_response(response: HttpResponse, status: int = 200, headers: dict = None):
    """Add specified headers to the response and set status"""
    if headers:
        for k, v in headers.items():
            response.headers[k] = v
    response.status_code = status
    return response


def _respond_template(request: HttpRequest, template_name: str, context_dict: dict, status: int = 200, headers: dict = None):
    """Render the specified template and set headers and status"""
    response = render(request, template_name, context_dict)
    return _after_response(response, status, headers)


def respond_404(request: HttpRequest, error: str = None, status: int = 404):
    """Respond with an error page, optionally with an error message"""
    context = {}
    if error is not None:
        context["error"] = error
    return _respond_template(request, dr_404, context_dict=context, status=status)


def static_response(request: HttpRequest, template_name: str, **context_dict) -> HttpResponse:
    """Respond with a specified template"""
    template = os.path.join(static_response_template_dir, template_name)
    return _respond_template(request, template, context_dict=context_dict)


def dynamic_response(request: HttpRequest, path: str):
    """
    Match the request to a CannedResponse object, check the request for any
        regular expressions associated with the CannedResponse (from the
        BodyMatch object), generate a response from the specified template,
        add any specified headers, and return it.
    """
    body = request.body.decode()

    possible_matches = models.CannedResponse.objects.filter(path=path)
    if not possible_matches:
        return respond_404(request, "BodyMatch object not found")
    canned_response = possible_matches.first()

    context = {"body": body}
    for bm in canned_response.body_matches.all():
        possible_matches = re.search(bm.match_pattern, body)
        if possible_matches:
            context.update(possible_matches.groupdict())

    template_name = os.path.join(dynanmic_response_template_dir, canned_response.response_template_name)
    headers = {header.name: header.value for header in canned_response.headers.all()}

    return _respond_template(request, template_name, context_dict=context, headers=headers)
