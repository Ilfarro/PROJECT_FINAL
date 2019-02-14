from django import forms
from .models import Contact_us

class PostForm(forms.ModelForm):

    class Meta:
        model = Contact_us
        fields = ('name', 'email', 'phone','comment')