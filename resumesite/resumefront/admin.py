from django.contrib import admin
from .models import (
    UserProfile,
    Resume,
    Education,
    Experience,
    Skill,
    Project,
    Certificate,
    Language,
    AIFeedback
)

admin.site.register(UserProfile)
admin.site.register(Resume)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Certificate)
admin.site.register(Language)
admin.site.register(AIFeedback)