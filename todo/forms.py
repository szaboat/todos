from django import forms

class TodoItemForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    done = forms.BooleanField(required=False)
