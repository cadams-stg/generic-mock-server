from django.urls import path

from . import views

urlpatterns = [
    # These are static responses. The content of the request is ignored, and
    #   any extra kwargs are sent to the specified template.
    path("version", views.static_response, name="version-info", kwargs={"template_name": "application_identity.json"}),
    path("hello", views.static_response, name="hello", kwargs={"template_name": "hello.json", "extraneous": "superfluous"}),
    # This is the dynamic view, which pulls response definition from the db
    path("dynamic/<str:path>", views.dynamic_response, name="dynamic-example"),
]
