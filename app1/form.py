from django import forms


class UserForm(forms.Form):
    name = forms.CharField(help_text="Имя")
    surname = forms.CharField(help_text="Фамилия")
    age = forms.IntegerField(help_text="Сколько лет", required=False)
    born = forms.DateField(widget=forms.SelectDateWidget, required=False)
