from django.contrib import admin

from . import models


class BodyMatchInline(admin.TabularInline):
    model = models.BodyMatch


class CannedResponseHeaderInline(admin.TabularInline):
    model = models.CannedResponseHeader


@admin.register(models.CannedResponse)
class CannedResponseAdmin(admin.ModelAdmin):
    inlines = (
        BodyMatchInline,
        CannedResponseHeaderInline,
    )
