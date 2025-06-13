from django.db import models
from custom_user.models import CustomUser

class Car(models.Model):
    # Основная информация
    title = models.CharField(max_length=255, help_text="Заголовок объявления")
    description = models.TextField(blank=True, help_text="Описание автомобиля")

    # Производитель и модель
    brand = models.CharField(max_length=100, help_text="Марка")
    model = models.CharField(max_length=100, help_text="Модель")
    generation = models.CharField(max_length=100, blank=True, help_text="Поколение (если нужно)")
    year = models.PositiveSmallIntegerField(help_text="Год выпуска")

    # Технические характеристики
    transmission = models.CharField(
        max_length=20,
        choices=[("AT", "Автомат"), ("MT", "Механика"), ("CVT", "Вариатор"), ("AMT", "Робот")],
        help_text="Коробка передач"
    )
    drive_type = models.CharField(
        max_length=20,
        choices=[("FWD", "Передний"), ("RWD", "Задний"), ("AWD", "Полный")],
        help_text="Тип привода"
    )
    body_type = models.CharField(max_length=20, help_text="Кузов (седан, хэтчбек и т.д.)")
    color = models.CharField(max_length=50, help_text="Цвет")
    engine_type = models.CharField(
        max_length=20,
        choices=[("petrol", "Бензин"), ("diesel", "Дизель"), ("hybrid", "Гибрид"), ("ev", "Электро")],
        help_text="Тип двигателя"
    )
    engine_volume = models.DecimalField(max_digits=3, decimal_places=1, help_text="Объем двигателя, л")
    horsepower = models.PositiveSmallIntegerField(help_text="Мощность, л.с.")

    # Пробег и история
    mileage = models.PositiveIntegerField(help_text="Пробег, км")
    owners_count = models.PositiveSmallIntegerField(help_text="Количество владельцев")
    vin = models.CharField(max_length=17, blank=True, help_text="VIN номер (опционально)")

    # Состояние и документы
    is_new = models.BooleanField(default=False, help_text="Новый или с пробегом")
    state = models.CharField(
        max_length=20, 
        choices=[("excellent", "Отличное"), ("good", "Хорошее"), ("needs_repair", "Требует ремонта")],
        help_text="Состояние"
    )
    pts_type = models.CharField(
        max_length=10, 
        choices=[("original", "Оригинал"), ("duplicate", "Дубликат")],
        help_text="ПТС"
    )

    # Цена и размещение
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Цена, руб.")
    city = models.CharField(max_length=100, help_text="Город продажи")
    address = models.CharField(max_length=200, blank=True, help_text="Адрес")

    # Фото из CarImage

    # Дополнительные сведения
    features = models.TextField(blank=True, help_text="Дополнительные опции и комплектация")

    # Владелец и дата публикации
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Машина"
        verbose_name_plural = "Машины"

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"

class CarImage(models.Model):
    car = models.ForeignKey(
        Car,
        related_name='images',
        on_delete=models.CASCADE,
        help_text="К какой машине привязано фото"
    )
    image = models.ImageField(
        upload_to='car_photos/',
        help_text="Фотография автомобиля"
    )
    is_primary = models.BooleanField(
        default=False,
        help_text="Главное фото"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return f"Фото к {self.car} ({'главное' if self.is_primary else 'обычное'})"