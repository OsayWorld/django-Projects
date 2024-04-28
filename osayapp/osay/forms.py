# forms.py

# ... (your other imports)

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import Profile

# Define your CustomAuthenticationForm here
class CustomAuthenticationForm(AuthenticationForm):
    # Add any custom fields you need for your form
    remember_me = forms.BooleanField(required=False)

    # You can also add any custom methods you need
    def custom_method(self):
        # Custom method logic here
        pass

# ... (your other form definitions)

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=15)
    bio = forms.CharField(widget=forms.Textarea, required=False)  # Make bio optional
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)  # Make date_of_birth optional

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2', 'phone_number', 'bio', 'date_of_birth']

    def save(self, commit=True):
        user = super().save(commit=False)  # Save the user instance without committing to the database
        user.email = self.cleaned_data['email']
        user.phone_number = self.cleaned_data['phone_number']  # Save the phone number to the CustomUser

        if commit:
            user.save()  # Save the user instance to the database
            # Create or update the Profile instance for the user
            profile, created = Profile.objects.get_or_create(user=user)
            profile.bio = self.cleaned_data.get('bio', '')
            profile.date_of_birth = self.cleaned_data.get('date_of_birth', None)
            profile.save()  # Save the profile instance to the database

        return user
