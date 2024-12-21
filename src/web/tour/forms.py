from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    """
    A form for creating and editing Booking entries.
    Includes validation for better user experience.
    """

    class Meta:
        model = Booking
        fields = [
            "full_name",
            "email",
            "phone_number",
            "country",
            "city",
            "state",
            "zip_code",
            "address_2",
            "tour",
            "tour_content",
        ]
        widgets = {
            "tour": forms.Select(attrs={"class": "form-control"}),
            "tour_content": forms.Textarea(attrs={"rows": 4, "class": "form-control"}),
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "phone_number": forms.TextInput(attrs={"class": "form-control"}),
            "country": forms.TextInput(attrs={"class": "form-control"}),
            "city": forms.TextInput(attrs={"class": "form-control"}),
            "state": forms.TextInput(attrs={"class": "form-control"}),
            "zip_code": forms.TextInput(attrs={"class": "form-control"}),
            "address_2": forms.TextInput(attrs={"class": "form-control"}),
        }

    def clean_phone_number(self):
        """
        Custom validation logic for phone numbers.
        Ensures only valid phone numbers are allowed.
        """
        phone = self.cleaned_data.get("phone_number")
        if not phone.isdigit():
            raise forms.ValidationError("Phone number must contain only digits.")
        return phone
