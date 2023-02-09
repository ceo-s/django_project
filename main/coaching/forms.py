from django import forms
from .models import TrainingExperience, SportTag, ClientRequest

# class ClientForm(forms.Form):
#     name = forms.CharField(label="Имя")
#     age = forms.IntegerField(label="Возраст")
#     sport = forms.ModelChoiceField(label="Вид спорта", queryset=SportTag.objects.all(), empty_label="Категория не выбрана!")
#     experience = forms.ModelChoiceField(label="Опыт", queryset=TrainingExperience.objects.all(), empty_label="Категория не выбрана!")
#     request = forms.CharField(label="Описание", widget=forms.Textarea(attrs={"cols":60, "rows": 7}))

class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientRequest
        fields = "__all__"