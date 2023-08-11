from django import forms
from .models import Company


class CompanyForm(forms.Form):
    Company = forms.ModelChoiceField(queryset=Company.objects.all().order_by('ticker'), to_field_name="ticker")

    @staticmethod
    def label_from_instance(self, obj):
        return "My Object #%i" % obj.ticker

    class Meta:
        model = Company
