from django.forms import ModelForm
from users.models import User,Product 

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["name", "first_name"]

class ProductForm(ModelForm):
    class Meta:
        model = Product 
        fields = ["name", "price", "description"]
        
