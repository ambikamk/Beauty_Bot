from django import forms
from .models import Product
from .models import Address

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock','image','description','brand','expiry_date','skin_concern','skin_type','ingredients','product_type','country_of_origin']

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'image','description','brand','expiry_date','skin_concern','skin_type','ingredients','product_type','country_of_origin']



class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['recepient_name', 'recepient_contact', 'address_line1', 'address_line2', 'city', 'state', 'postal_code']        

