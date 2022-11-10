from django.urls import path
from .views import index, CookListView, DishTypeCreateView, DishListView, DishTypeListView, DishTypeUpdateView, \
    CookDetailView, CookCreateView, CookYearOfExperienceUpdateView, DishDetailView, DishCreateView, DishDeleteView, \
    DishUpdateView

urlpatterns = [
    path("", index, name="index"),
    path(
        "dishes-type-list/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path(
        "dishes-type-list/create/",
        DishTypeCreateView.as_view(),
        name="dish_type_list-create"
    ),
    path(
        "dishes-type-list/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish_type_list-update"
    ),
    path(
        "dishes-type-list/<int:pk>/delete/",
        DishTypeCreateView.as_view(),
        name="dish-type-list-delete"
    ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list"
    ),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail"
    ),
    path(
        "cooks/create/",
        CookCreateView.as_view(),
        name="cook-create"
    ),
    path(
        "cooks/<int:pk>/delete/",
        CookCreateView.as_view(),
        name="cook-delete"
    ),
    path(
        "cooks/<int:pk>/update/",
        CookYearOfExperienceUpdateView.as_view(),
        name="cook-update"
    ),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list"
    ),
    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail"
    ),
    path(
        "dishes/create/",
        DishCreateView.as_view(),
        name="dish-create"
    ),
    path(
        "dishes/<int:pk>/update/",
        DishUpdateView.as_view(),
        name="dish-update"
    ),
    path(
        "dishes/<int:pk>/delete/",
        DishDeleteView.as_view(),
        name="dish-delete"
    ),
]

app_name = "restaurant"
