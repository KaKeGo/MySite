from django import forms

from .models import Skills


class SkillCreateForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ('title', 'score',)
