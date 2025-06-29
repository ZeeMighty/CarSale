from typing import Any

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):
    def create_user(self, email: str, password: str=None, **extra_fields: Any) -> Any:
        if not email:
            raise ValueError("Email is required")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, password:str | None = None, 
                         **extra_fields: Any) -> Any:
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class Company(models.Model):
    name = models.CharField(max_length=70, verbose_name="Название организации")
    rating = models.FloatField(default=0)

    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

    def __str__(self) -> str:
        return self.name

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    username = models.CharField(blank=True, unique=False, max_length=50)
    email = models.EmailField(("email address"), blank=False, unique=True, error_messages={  # noqa: E501
            "unique": ("A user with that email already exists."),
        },)
    is_partner = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.email
