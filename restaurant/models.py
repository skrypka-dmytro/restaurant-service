from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(max_length=65, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("restaurant:position-create", kwargs={"pk": self.pk})


class DishType(models.Model):
    name = models.CharField(max_length=65, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(
        default=0,
        null=True,
        blank=True
    )
    position = models.ForeignKey(
        Position,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self):
        return reverse("restaurant:cook-detail", kwargs={"pk": self.pk})


class Dish(models.Model):
    name = models.CharField(max_length=65, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    def __str__(self) -> str:
        return f"{self.name} (price: {self.price})"
