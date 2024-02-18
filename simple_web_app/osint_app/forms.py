from django import forms
# from .models import Post
# from .modules.organization_info import OrganizationInfo


class PostForm(forms.Form):
    name_of_organization = forms.CharField(max_length=255, label='Organization title', help_text='enter organization title')
    domains = forms.CharField(max_length=255, label='Domain', help_text='enter domain')
