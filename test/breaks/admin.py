from django.contrib import admin
from django.contrib.admin import TabularInline

import breaks.models.breaks
from breaks.models import organizations, groups, replacement, breaks
from breaks.models import dicts


class ReplacementEmployeeInline(TabularInline):
    model = replacement.ReplacementEmployee
    fields = ('employee', 'status',)


@admin.register(organizations.Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'director',)


@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', 'min_active',)


@admin.register(replacement.Replacement)
class ReplacementAdmin(admin.ModelAdmin):
    list_display = ('id', 'group', 'date', 'break_start', 'break_end', 'break_max_duration')

    inlines = (
        ReplacementEmployeeInline,
    )


@admin.register(dicts.ReplacementStatus)
class ReplacementStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active',)


@admin.register(dicts.BreakStatus)
class BreakStatusAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'sort', 'is_active',)


@admin.register(breaks.Break)
class BreakAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'replacement', 'break_start', 'break_end',
    )
