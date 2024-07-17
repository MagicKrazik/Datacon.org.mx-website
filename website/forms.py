from django import forms
from .models import QuoteRequest
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'company', 'country', 'language', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your Phone Number (optional)'}),
            'company': forms.TextInput(attrs={'placeholder': 'Your Company (optional)'}),
            'country': forms.TextInput(attrs={'placeholder': 'Your Country (optional)'}),
            'language': forms.TextInput(attrs={'placeholder': 'Preferred Language (optional)'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message'}),
        }



class QuoteRequestForm(forms.ModelForm):
    project_type = forms.ChoiceField(
        choices=[
            ('', 'Select a project type'),
            ('custom-web-app', 'Custom Web Application'),
            ('data-analytics', 'Data Analytics Solution'),
            ('process-automation', 'Process Automation'),
            ('financial-system', 'Financial Management System'),
            ('other', 'Other (please specify)'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    budget = forms.ChoiceField(
        choices=[
            ('', 'Select an aproximate budget range (USD)'),
            ('under-5k', 'Under $5,000'),
            ('5k-15k', '$5,000 - $15,000'),
            ('15k-30k', '$15,000 - $30,000'),
            ('30k-75k', '$30,000 - $75,000'),
            ('over-75k', 'Over $75,000'),
        ],
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = QuoteRequest
        fields = ['name', 'email', 'phone', 'company', 'industry', 'project_type', 'project_description', 'budget', 'timeline', 'additional_info']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Your Phone Number'}),
            'company': forms.TextInput(attrs={'placeholder': 'Your Company Name'}),
            'industry': forms.TextInput(attrs={'placeholder': 'Your Industry'}),
            'project_description': forms.Textarea(attrs={'placeholder': 'Describe your project'}),
            'timeline': forms.TextInput(attrs={'placeholder': 'e.g., 3 months, 6 months'}),
            'additional_info': forms.Textarea(attrs={'placeholder': 'Any additional information'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if isinstance(self.fields[field].widget, forms.Select):
                self.fields[field].widget.attrs.update({'class': 'form-control'})
            elif not isinstance(self.fields[field].widget, forms.CheckboxSelectMultiple):
                self.fields[field].widget.attrs.update({'class': 'form-control'})