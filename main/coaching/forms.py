from django import forms
from django.forms import widgets
from .models import TrainingExperience, SportTag, ClientRequest

# class ClientForm(forms.Form):
#     name = forms.CharField(label="Имя")
#     age = forms.IntegerField(label="Возраст")
#     sport = forms.ModelChoiceField(label="Вид спорта", queryset=SportTag.objects.all(), empty_label="Категория не выбрана!")
#     experience = forms.ModelChoiceField(label="Опыт", queryset=TrainingExperience.objects.all(), empty_label="Категория не выбрана!")
#     request = forms.CharField(label="Описание", widget=forms.Textarea(attrs={"cols":60, "rows": 7}))

class ClientForm(forms.ModelForm):
    #name = forms.CharField(label="Имя")
    #birth_date = forms.DateField(label="Дата рождения", widget=forms.NumberInput(attrs={"class": "form-control", "style":"width:400px"}))
    sport = forms.ModelChoiceField(label="Вид спорта", queryset=SportTag.objects.all(), empty_label="Категория не выбрана!",  widget=forms.Select(attrs={"class": "form-control", "style":"width:400px"}))
    experience = forms.ModelChoiceField(label="Опыт", queryset=TrainingExperience.objects.all(), empty_label="Категория не выбрана!", widget=forms.Select(attrs={"class": "form-control", "style":"width:400px"}))
    request = forms.CharField(label="Описание", widget=forms.Textarea(attrs={"cols":60, "rows": 5, "class":"form-control", "placeholder": "Подробно опишите ваш запрос..."}))
    class Meta:
        model = ClientRequest
        fields = "__all__"

        labels = {
           "name": "Имя"
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Ваше ФИО", "class": "form-control", "style":"width:400px"}),
            "experience": widgets.ChoiceWidget(attrs={"class":"form-control"})
        }