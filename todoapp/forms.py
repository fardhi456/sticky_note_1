from django import forms
from .models import TodoTask

class TodoTaskForm(forms.ModelForm):
    class Meta:
        model = TodoTask
        fields = ['title', 'due_date'] 

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    username = forms.CharField(
        max_length=150,
        required=True,
        help_text='Required. 150 characters or fewer.',
        widget=forms.TextInput(attrs={'autocomplete': 'username'}),
    )

    def clean_username(self):
        # Here you could add your own validation or skip it entirely
        username = self.cleaned_data['username']
        # Example: allow spaces by removing the default validator restriction
        return username

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class RegisterForm(UserCreationForm):
#     email = forms.EmailField(required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']


from django import forms

class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput)

from .models import StickyNote

class StickyNoteForm(forms.ModelForm):
    class Meta:
        model = StickyNote
        fields = ['content']
