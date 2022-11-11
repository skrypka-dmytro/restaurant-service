from django.urls import path
from .views import index, CookListView, DishTypeCreateView, DishListView, DishTypeListView, DishTypeUpdateView, \
    CookDetailView, CookCreateView, CookYearOfExperienceUpdateView, DishDetailView, DishCreateView, DishDeleteView, \
    DishUpdateView, DishTypeDeleteView, PositionListView, PositionCreateView, PositionUpdateView, PositionDeleteView, \
    CookDeleteView

urlpatterns = [
    path("", index, name="index"),
    path(
        "positions/",
        PositionListView.as_view(),
        name="position-list"
    ),
    path(
        "positions/create/",
        PositionCreateView.as_view(),
        name="position-create"
    ),
    path(
        "positions/<int:pk>/update",
        PositionUpdateView.as_view(),
        name="position-update"
    ),
    path(
        "positions/<int:pk>/delte",
        PositionDeleteView.as_view(),
        name="position-delete"
    ),
    path(
        "dishes-type-list/",
        DishTypeListView.as_view(),
        name="dish-type-list"
    ),
    path(
        "dishes-type-list/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create"
    ),
    path(
        "dishes-type-list/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update"
    ),
    path(
        "dishes-type-list/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete"
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
        CookDeleteView.as_view(),
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
