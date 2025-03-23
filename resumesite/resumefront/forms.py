from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import (
    UserProfile,
    Resume,
    Education,
    Experience,
    Skill,
    Project,
    Certificate,
    Language
)

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'profile_picture']
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': '+91 1234567890'})
        }

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'template', 'summary', 'is_public']
        widgets = {
            'summary': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write a brief summary of your professional background...'}),
            'title': forms.TextInput(attrs={'placeholder': 'e.g., Software Developer Resume'})
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'field_of_study', 'start_date', 'end_date', 'gpa', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['company', 'position', 'location', 'start_date', 'end_date', 'is_current', 'description']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe your responsibilities and achievements...'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        is_current = cleaned_data.get('is_current')
        end_date = cleaned_data.get('end_date')

        if is_current and end_date:
            raise forms.ValidationError("End date should be empty if this is your current position")
        
        return cleaned_data

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'level']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g., Python, Project Management'})
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'url', 'start_date', 'end_date', 'technologies']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 3}),
            'technologies': forms.TextInput(attrs={'placeholder': 'e.g., Python, Django, React'})
        }

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['name', 'issuing_organization', 'issue_date', 'expiry_date', 'credential_id', 'url']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'expiry_date': forms.DateInput(attrs={'type': 'date'})
        }

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name', 'proficiency']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'e.g., English, Spanish'})
        }

class ResumeImportForm(forms.Form):
    resume_file = forms.FileField(
        label='Upload Resume',
        help_text='Upload your existing resume (PDF, DOCX)',
        widget=forms.FileInput(attrs={'accept': '.pdf,.docx'})
    )

class AIGenerateForm(forms.Form):
    SECTION_CHOICES = [
        ('summary', 'Professional Summary'),
        ('experience', 'Work Experience'),
        ('skills', 'Skills'),
    ]
    
    section = forms.ChoiceField(choices=SECTION_CHOICES)
    current_content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4}),
        required=False,
        help_text='Current content (optional)'
    )
    instructions = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False,
        help_text='Any specific instructions for the AI'
    )