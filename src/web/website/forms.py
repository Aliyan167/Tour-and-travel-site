from django import forms
from .models import Contact
from .models import NewsletterSubscription


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'full_name', 'email', 'phone_number', 'country',
            'city', 'state', 'zip_code', 'address', 'tour', 'tour_content'
        ]


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



