from django.test import TestCase

from restaurant.forms import CookCreationForm


class FormsTests(TestCase):
    def test_cook_creation_form_with_years_of_experience_is_valid(self):
        form_data = {
            "username": "username",
            "password1": "1qazcde3",
            "password2": "1qazcde3",
            "first_name": "test_name",
            "last_name": "test_surname",
            "years_of_experience": 0,
        }

        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
