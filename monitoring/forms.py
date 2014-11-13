from django import forms
from django.contrib.auth.models import User
from django.contrig.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True, label = "First Name")
    last_name = forms.CharField(required=True, label = "Last Name")
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

'''
    def save(self, commit=True)
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save() '''
