from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import Position, Cook, DishType


class ModelsTests(TestCase):
    def test_position_format_str(self):
        position = Position.objects.create(
            name="test_chief-cook",
        )
        self.assertEqual(
            str(position), position.name
        )

    def test_cook_format_str(self):
        cook = Cook.objects.create(
            username="gangster288",
            password="testpassword",
            first_name="test_name",
            last_name="test_name",
        )
        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_dish_type_format_str(self):
        dish_type = DishType.objects.create(
            name="test_name",
        )
        self.assertEqual(
            str(dish_type), dish_type.name
        )

    def test_create_cook_with_years_of_experience(self):
        username = "username"
        password = "test_password"
        years_of_experience = 0

        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )

        self.assertEqual(cook.username, username)
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertTrue(cook.check_password(password))
