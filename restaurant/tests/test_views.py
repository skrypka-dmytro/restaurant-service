from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from restaurant.models import Position, DishType

INDEX = reverse("restaurant:index")
LOGIN = reverse("login")
POSITION_LIST = reverse("restaurant:position-list")
DISH_TYPE_LIST = reverse("restaurant:dish-type-list")
DISH_LIST = reverse("restaurant:dish-list")
COOK_LIST = reverse("restaurant:cook-list")
POSITION_CREATE = reverse("restaurant:position-create")
DISH_TYPE_CREATE = reverse("restaurant:dish-type-create")
DISH_CREATE = reverse("restaurant:dish-create")


class PublicTests(TestCase):
    def test_login_required_for_index(self):
        res = self.client.get(INDEX)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_for_position_list(self):
        res = self.client.get(POSITION_LIST)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_for_position_create(self):
        res = self.client.get(POSITION_CREATE)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_for_dish_type_list(self):
        res = self.client.get(DISH_TYPE_LIST)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_for_dish_type_create(self):
        res = self.client.get(DISH_TYPE_CREATE)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_for_dish_list(self):
        res = self.client.get(DISH_LIST)
        self.assertNotEqual(res.status_code, 200)

    def test_login_required_for_dish_create(self):
        res = self.client.get(DISH_CREATE)
        self.assertNotEqual(res.status_code, 200)


class PrivateTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test",
            "password1234",
        )
        self.client.force_login(self.user)

    def test_index_page(self):
        res = self.client.get(INDEX)

        self.assertEqual(res.status_code, 200)

    def test_login_page(self):
        res = self.client.get(LOGIN)

        self.assertEqual(res.status_code, 200)

    def test_retrieve_position_list(self):
        Position.objects.create(name="test_v1")
        Position.objects.create(name="test_v2")
        res = self.client.get(POSITION_LIST)
        position_list = Position.objects.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["position_list"]), list(position_list)
        )

        self.assertTemplateUsed(res, "restaurant/position_list.html")

    def test_retrieve_dish_type_list(self):
        DishType.objects.create(name="test1")
        DishType.objects.create(name="test2")
        res = self.client.get(DISH_TYPE_LIST)
        dish_type_list = DishType.objects.all()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(
            list(res.context["dish_type_list"]), list(dish_type_list)
        )

        self.assertTemplateUsed(res, "restaurant/dish_type_list.html")

    def test_retrieve_cook_list(self):
        res = self.client.get(COOK_LIST)

        self.assertEqual(res.status_code, 200)


class CreateCookTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user("test", "password")
        self.client.force_login(self.user)

    def test_create_driver(self):
        from_data = {
            "username": "username",
            "password1": "1qazcde3",
            "password2": "1qazcde3",
            "first_name": "test_name",
            "last_name": "test_surname",
            "years_of_experience": 1,
        }

        self.client.post(reverse("restaurant:cook-create"), data=from_data)
        new_user = get_user_model().objects.get(username=from_data["username"])

        self.assertEqual(new_user.first_name, from_data["first_name"])
        self.assertEqual(new_user.last_name, from_data["last_name"])
        self.assertEqual(new_user.years_of_experience, from_data["years_of_experience"])
