from django import forms
from user.models import User, Contact, Mobile, Profile
from django.contrib.auth import get_user_model
# User = get_user_model()
from django.core.exceptions import ValidationError
# creating a form
class RegistrationForm(forms.ModelForm):

    class Meta:
        """
        Class to define required model and its field to user registration
        """
        model = User
        fields = ["fname", "lname", "Address", "mobile", "email", "password"]

    def save(self, commit=True):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")
        user = super(RegistrationForm, self).save(commit=False)
        # user.password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
    

class ContactForm(forms.Form):
    fname = forms.CharField(max_length = 30)
    lname = forms.CharField(max_length = 30)
    mobile= forms.IntegerField(
                     help_text = "Enter mobile number"
                     )
class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        fields =('image')