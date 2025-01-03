from django import forms
from .models import Contact
from .models import NewsletterSubscription


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number (optional)'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message'}),
        }


class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']

        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'newsletter-email',
                'placeholder': 'Your email address',
                'required': 'required'
            })
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if NewsletterSubscription.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already subscribed.')
        return email
