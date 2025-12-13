import re
from django import forms
from taxi.models import Driver

LICENSE_REGEX = r"[A-Z]{3}\d{5}"


class BaseDriverForm(forms.ModelForm):
    def clean_license_number(self):
        license_number = self.cleaned_data["license_number"]

        if not re.fullmatch(LICENSE_REGEX, license_number):
            raise forms.ValidationError(
                "License number must have format: XXXDDDDD"
            )
        return license_number


class DriverForm(BaseDriverForm):
    class Meta:
        model = Driver
        fields = "__all__"


class DriverLicenseUpdateForm(BaseDriverForm):
    class Meta:
        model = Driver
        fields = ("license_number",)
