from django.forms import ModelForm
from main.models import Item

# Form untuk input data
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "category", "borrow_date", "description"]