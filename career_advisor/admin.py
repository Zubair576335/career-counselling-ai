from django.contrib import admin
from .models import Skill, CareerRole, UserProfile, ResumeAnalysis, SkillGapReport, LearningPath

@admin.register(CareerRole)
class CareerRoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'average_salary', 'market_trend')
    search_fields = ('name',)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'target_role', 'current_title')

@admin.register(ResumeAnalysis)
class ResumeAnalysisAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_id', 'ats_score', 'created_at')

@admin.register(SkillGapReport)
class SkillGapReportAdmin(admin.ModelAdmin):
    list_display = ('resume_analysis', 'target_role', 'readiness_score', 'created_at')

@admin.register(LearningPath)
class LearningPathAdmin(admin.ModelAdmin):
    list_display = ('skill_gap_report', 'created_at')
