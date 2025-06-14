from django.db import models
from custom_user.models import CustomUser
from django.db.models import CheckConstraint, Q, F
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class Car(models.Model):
    # Основная информация
    title = models.CharField(max_length=255, help_text="Заголовок объявления")
    description = models.TextField(blank=True, help_text="Описание автомобиля")

    # Производитель и модель
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    model = models.ForeignKey('CarModel', on_delete=models.CASCADE, blank=True)
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
    vin = models.CharField(max_length=17, blank=True, help_text="VIN номер", error_messages={
            "unique": ("A car with that vin is already exists.")})

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
        constraints = (
            models.UniqueConstraint(
                fields=['vin'],
                name='car_vin_unique'
            ),
            models.CheckConstraint(
                check=models.Q(year__gte=1500),
                name='car_year_gte_1500'
            ),
            models.CheckConstraint(
                check=models.Q(updated_at__gte=F('created_at')),
                name='check_created_date'
            ),
        )

    def clean(self):
        # Проверяем, что марка есть в базе моделей
        if self.brand in Brand.objects.all():
            # Проверяем, что модель входит в допустимый список для этой марки
            if self.model not in CarModel.objects.filter(brand=self.brand):
                raise ValidationError(
                    f"Модель {self.model} не подходит для марки {self.brand}!"
                )
        else:
            raise ValidationError(f"Марка {self.brand} не поддерживается!")

    def save(self, *args, **kwargs):
        # Делаю обязательный вызов метода clean при сохранении объекта
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.brand} {self.model} {self.year}"

class CarImage(models.Model):
    car = models.ForeignKey(Car, related_name='images', on_delete=models.CASCADE, help_text="К какой машине привязано фото")
    image = models.ImageField(upload_to='car_photos/', help_text="Фотография автомобиля")
    is_primary = models.BooleanField(default=False, help_text="Главное фото")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return f"Фото к {self.car} ({'главное' if self.is_primary else 'обычное'})"

# Удаление файла картинки при удалении объекта 
@receiver(post_delete, sender=CarImage)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        instance.image.delete(False)  # False — не сохранять модель

class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Марка")

    class Meta:
        verbose_name = "Марка автомобиля"
        verbose_name_plural = "Марки автомобилей"

    def __str__(self):
        return self.name

class CarModel(models.Model):
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='models', verbose_name="Марка")
    name = models.CharField(max_length=100, verbose_name="Модель")

    class Meta:
        unique_together = ('brand', 'name')
        verbose_name = "Модель автомобиля"
        verbose_name_plural = "Модели автомобилей"

    def __str__(self):
        return f"{self.brand} {self.name}"
