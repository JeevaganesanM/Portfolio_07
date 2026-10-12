from django import forms
from .models import ContactMessage
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]
        widgets = {field: forms.TextInput(attrs={"class": "field"}) for field in ["name", "email", "subject"]}
        widgets["message"] = forms.Textarea(attrs={"class": "field", "rows": 6})
