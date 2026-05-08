from django.db import models
from django.contrib.auth.models import User
import json

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name

class CareerRole(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True, null=True)
    required_skills = models.JSONField(default=list, help_text="List of required skills")
    average_salary = models.CharField(max_length=100, blank=True, null=True)
    market_trend = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    target_role = models.ForeignKey(CareerRole, on_delete=models.SET_NULL, null=True, blank=True)
    current_title = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class ResumeAnalysis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume_analyses', null=True, blank=True)
    session_id = models.CharField(max_length=100, null=True, blank=True) # For anonymous users
    
    # Extracted data
    extracted_skills = models.JSONField(default=list)
    education = models.JSONField(default=list)
    experience = models.JSONField(default=list)
    projects = models.JSONField(default=list)
    
    # Scores
    ats_score = models.IntegerField(default=0)
    improvement_suggestions = models.JSONField(default=list)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        owner = self.user.username if self.user else f"Session {self.session_id}"
        return f"Resume Analysis for {owner}"

class SkillGapReport(models.Model):
    resume_analysis = models.ForeignKey(ResumeAnalysis, on_delete=models.CASCADE, related_name='skill_gaps')
    target_role = models.ForeignKey(CareerRole, on_delete=models.CASCADE)
    
    readiness_score = models.IntegerField(default=0)
    matching_skills = models.JSONField(default=list)
    missing_skills = models.JSONField(default=list)
    recommendations = models.JSONField(default=list)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Gap Report: {self.target_role.name}"

class LearningPath(models.Model):
    skill_gap_report = models.ForeignKey(SkillGapReport, on_delete=models.CASCADE, related_name='learning_paths')
    
    # structured as a timeline: [{"phase": "Beginner", "duration": "4 weeks", "topics": [...], "resources": [...]}]
    timeline = models.JSONField(default=list)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Learning Path for {self.skill_gap_report.target_role.name}"
