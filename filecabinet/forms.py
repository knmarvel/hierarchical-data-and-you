from django import forms
from filecabinet.models import File
from mptt.forms import TreeNodeChoiceField

class FileForm(forms.Form):
    name = forms.CharField(max_length=200)
    parent = TreeNodeChoiceField(queryset=File.objects.all())
    

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)