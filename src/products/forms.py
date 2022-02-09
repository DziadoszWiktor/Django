from djmoney.models.fields import MoneyField
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "summary",
        ]

    def validator(self,*args, **kwagrs):
        title = self.cleaned_data("title")
        if not "ok" in title:
            raise forms.ValidationError("nope")

#the difference between this and Product form is the forms.Form attribute
#that means this is a standard django form
class RawProductForm(forms.Form):
    # in the forms module we don't have textfiled only charfield (modified by models.py)
    title = forms.CharField()
    description = forms.CharField()
    price = forms.DecimalField()
    # price = MoneyField(
    #     decimal_places=2,
    #     default=0,
    #     default_currency='PLN',
    #     max_digits=10,
    # )
    summary = forms.CharField()

