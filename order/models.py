from django.db import models
from custom_user.models import CustomUser
from dashboard.models import Car
from django.db.models import CheckConstraint, Q, F

class Order(models.Model):
    """Заказ на проверку и размещение авто."""
    STATUS_CHOICES = [
        ('draft', 'Черновик'),
        ('pending', 'Ожидает проверки'),
        ('checked', 'Проверено'),
        ('listed', 'Размещено'),
        ('rejected', 'Отклонено'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Заказчик", related_name="customer")
    car = models.OneToOneField(Car, on_delete=models.CASCADE, verbose_name="Автомобиль")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft', verbose_name="Статус заявки")
    comment = models.TextField(blank=True, verbose_name="Комментарий заказчика")
    is_check = models.BooleanField(default=False, verbose_name="С проверкой или без")
    checker = models.ForeignKey(CustomUser, blank=True, on_delete=models.CASCADE, verbose_name="Проверяющий партнёр", related_name="checker_partner")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return f"Заказ №{self.pk} — {self.car} ({self.user})"
