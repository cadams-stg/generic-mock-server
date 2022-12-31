from django.db import models


class CannedResponse(models.Model):
    response_template_name = models.CharField("Response Template Name", max_length=255)
    path = models.CharField("Path", max_length=1023)

    def __str__(self) -> str:
        return f"Canned Response at path `{self.path}`"


class CannedResponseHeader(models.Model):
    response = models.ForeignKey(CannedResponse, related_name="headers", on_delete=models.CASCADE)
    name = models.CharField("Header Name", max_length=255)
    value = models.TextField("Header Value")


class BodyMatch(models.Model):
    canned_response = models.ForeignKey(CannedResponse, related_name="body_matches", on_delete=models.CASCADE)
    match_pattern = models.TextField("Regex Pattern to Search")
