from typing import Any

from custom_user.models import CustomUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.db.models import F
from django.db.models.signals import post_delete
from django.dispatch import receiver

vin_validator = RegexValidator(
    regex=r"^[A-HJ-NPR-Z0-9]{17}$",
    message="Введите корректный VIN: 17 символов, латинские буквы (без I, O, Q) и цифры."
)

class Car(models.Model):
    # Основная информация
    title = models.CharField(max_length=255, verbose_name="Заголовок объявления")
    description = models.TextField(blank=True, null=True,
                                   verbose_name="Описание автомобиля")

    # Производитель и модель
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE)
    model = models.ForeignKey("CarModel", on_delete=models.CASCADE, blank=True, null=True)
    generation = models.CharField(max_length=100, blank=True, null=True,
                                  verbose_name="Поколение (если нужно)")
    year = models.PositiveSmallIntegerField(verbose_name="Год выпуска")

    # Технические характеристики
    transmission = models.CharField(
        max_length=20,
        choices=[("AT", "Автомат"), ("MT", "Механика"),
                 ("CVT", "Вариатор"), ("AMT", "Робот")],
        verbose_name="Коробка передач"
    )
    drive_type = models.CharField(
        max_length=20,
        choices=[("FWD", "Передний"), ("RWD", "Задний"), ("AWD", "Полный")],
        verbose_name="Тип привода"
    )
    body_type = models.CharField(max_length=20,
                                 verbose_name="Кузов (седан, хэтчбек и т.д.)")
    color = models.CharField(max_length=50, verbose_name="Цвет")
    engine_type = models.CharField(
        max_length=20,
        choices=[("petrol", "Бензин"), ("diesel", "Дизель"),
                 ("hybrid", "Гибрид"), ("ev", "Электро")],
        verbose_name="Тип двигателя"
    )
    engine_volume = models.DecimalField(max_digits=3, decimal_places=1,
                                        verbose_name="Объем двигателя, л")
    horsepower = models.PositiveSmallIntegerField(verbose_name="Мощность, л.с.")

    # Пробег и история
    mileage = models.PositiveIntegerField(verbose_name="Пробег, км")
    owners_count = models.PositiveSmallIntegerField(verbose_name="Количество владельцев")
    vin = models.CharField(max_length=17, blank=True, verbose_name="VIN номер",
                           validators=[vin_validator], error_messages={
                               "unique": ("A car with that vin is already exists.")
                               })

    # Состояние и документы
    is_new = models.BooleanField(default=False, verbose_name="Новый или с пробегом")
    state = models.CharField(
        max_length=20, 
        choices=[("excellent", "Отличное"), ("good", "Хорошее"),
                 ("needs_repair", "Требует ремонта")],
        verbose_name="Состояние"
    )
    pts_type = models.CharField(
        max_length=10, 
        choices=[("original", "Оригинал"), ("duplicate", "Дубликат")],
        verbose_name="ПТС"
    )

    # Цена и размещение
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена, руб.")  # noqa: E501
    city = models.CharField(max_length=100, verbose_name="Город продажи")
    address = models.CharField(max_length=200, blank=True, verbose_name="Адрес")

    # Фото из CarImage

    # Дополнительные сведения
    features = models.TextField(blank=True,
                                verbose_name="Дополнительные опции и комплектация")

    # Владелец и дата публикации
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"
        constraints = (
            models.CheckConstraint(
                check=models.Q(year__gte=1500),
                name="car_year_gte_1500"
            ),
            models.CheckConstraint(
                check=models.Q(updated_at__gte=F("created_at")),
                name="check_created_date"
            ),
        )

    def clean(self) -> None:
        # Проверяем, что марка есть в базе моделей
        if self.brand in Brand.objects.all():
            # Проверяем, что модель входит в допустимый список для этой марки
            if self.model_id not in CarModel.objects.filter(brand=self.brand).only("id"):
                raise ValidationError(
                    f"Модель {self.model} не подходит для марки {self.brand}!"
                )
        else:
            raise ValidationError(f"Марка {self.brand} не поддерживается!")

    def save(self, *args:Any, **kwargs:Any) -> None:
        # Делаю обязательный вызов метода clean при сохранении объекта
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.brand} {self.model} {self.year}"

class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name="images", on_delete=models.CASCADE,
                            verbose_name="К какой машине привязано фото")
    image = models.ImageField(upload_to="car_photos/", verbose_name="Фотография автомобиля")  # noqa: E501
    is_primary = models.BooleanField(default=False, verbose_name="Главное фото")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self) -> str:
        return f"Фото к {self.car} ({'главное' if self.is_primary else 'обычное'})"

# Удаление файла картинки при удалении объекта 
@receiver(post_delete, sender=CarImage)
def delete_image_file(sender:str, instance:str, **kwargs:Any) -> None:
    if instance.image:
        instance.image.delete(False)  # False — не сохранять модель

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Марка")

    class Meta:
        verbose_name = "Марка автомобиля"
        verbose_name_plural = "Марки автомобилей"

    def __str__(self) -> str:
        return self.name

class CarModel(models.Model):
    brand = models.ForeignKey("Brand", on_delete=models.CASCADE,
                              related_name="models", verbose_name="Марка")
    name = models.CharField(max_length=100, verbose_name="Модель")

    class Meta:
        unique_together = ("brand", "name")
        verbose_name = "Модель автомобиля"
        verbose_name_plural = "Модели автомобилей"

    def __str__(self) -> str:
        return f"{self.brand} {self.name}"

class CarArchive(Car):
    archived_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Архивная машина"
        verbose_name_plural = "Архивные машины"

    def __str__(self) -> str:
        return f"{self.brand} {self.model}"