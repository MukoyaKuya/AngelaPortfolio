from django.contrib import admin
from .models import Profile, Skill, Achievement, Experience, Education, Certification


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'location']
    fieldsets = (
        ('Basic Info', {
            'fields': ('name', 'title', 'summary', 'avatar')
        }),
        ('Contact', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Links', {
            'fields': ('linkedin', 'github')
        }),
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    list_filter = ['category']
    search_fields = ['name']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['description']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['role', 'company', 'date_range', 'order']
    list_editable = ['order']
    fieldsets = (
        ('Position', {
            'fields': ('role', 'company', 'date_range', 'order')
        }),
        ('Details', {
            'fields': ('description',)
        }),
        ('Media', {
            'fields': ('company_logo', 'work_image'),
            'description': 'Upload company logo and work samples'
        }),
    )


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['level', 'degree', 'institution', 'year', 'grade', 'order']
    list_filter = ['level']
    list_editable = ['order']
    fieldsets = (
        ('Level', {
            'fields': ('level',)
        }),
        ('Details', {
            'fields': ('degree', 'institution', 'grade', 'year', 'order')
        }),
        ('Media', {
            'fields': ('logo',)
        }),
    )


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuer', 'year', 'order']
    list_editable = ['order']
