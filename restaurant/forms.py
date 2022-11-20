from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from restaurant.models import Dish, Cook


class PositionSearchForm(forms.Form):
    name = forms.CharField(
        max_length=65,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Enter Position"})
    )


class DishTypeSearchForm(forms.Form):
    name = forms.CharField(
        max_length=65,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Enter the Dishes Type"})
    )


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class DishSearchForm(forms.Form):
    name = forms.CharField(
        max_length=65,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Enter the Dishes"})
    )


class CookCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Cook
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
            "position",
        )


class CookYearOfExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["years_of_experience"]