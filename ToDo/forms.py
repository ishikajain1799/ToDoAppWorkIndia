from django import forms
from ToDo.models import agentLogin
from django.contrib.auth.models import User

class AgentForm(forms.ModelForm):
    password = forms.CharField(max_length= 20)
    class Meta():
        model = User
        fields = ('agent_id','password')

class agentLoginForm(forms.ModelForm):
    class Meta():
        model = agentLogin
        fields = ('agent_id')

