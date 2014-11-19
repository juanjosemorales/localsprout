from django import forms
from django.contrib.auth.forms import UserCreationForm

'''class AccountRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False, label = "Phone Number")
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'password1', 'password2')

    def save(self, commit=True):
        user = super(AccountRegistrationForm, self).save(commit=False)
        user.phone = self.cleaned_data['phone']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user'''
