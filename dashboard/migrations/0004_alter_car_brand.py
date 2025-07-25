# Generated by Django 5.2.2 on 2025-06-13 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_car_vin_car_car_vin_unique_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(choices=[('Toyota', 'Toyota'), ('Volkswagen', 'Volkswagen'), ('Ford', 'Ford'), ('Honda', 'Honda'), ('Chevrolet', 'Chevrolet'), ('Mercedes-Benz', 'Mercedes-Benz'), ('BMW', 'BMW'), ('Nissan', 'Nissan'), ('Hyundai', 'Hyundai'), ('Kia', 'Kia'), ('Renault', 'Renault'), ('Peugeot', 'Peugeot'), ('Audi', 'Audi'), ('Suzuki', 'Suzuki'), ('Fiat', 'Fiat'), ('Lexus', 'Lexus'), ('Mazda', 'Mazda'), ('Škoda', 'Škoda'), ('Mitsubishi', 'Mitsubishi'), ('Chery', 'Chery'), ('Subaru', 'Subaru'), ('Jeep', 'Jeep'), ('Daihatsu', 'Daihatsu'), ('Great Wall', 'Great Wall'), ('Volvo', 'Volvo'), ('Land Rover', 'Land Rover'), ('Citroën', 'Citroën'), ('Jaguar', 'Jaguar'), ('Opel', 'Opel'), ('Dacia', 'Dacia'), ('Buick', 'Buick'), ('Cadillac', 'Cadillac'), ('Infiniti', 'Infiniti'), ('Mini', 'Mini'), ('Porsche', 'Porsche'), ('Acura', 'Acura'), ('Seat', 'Seat'), ('BYD', 'BYD'), ('Geely', 'Geely'), ('Tesla', 'Tesla'), ('Saab', 'Saab'), ('Lada', 'Lada'), ('Haval', 'Haval'), ('Ram', 'Ram'), ('Dongfeng', 'Dongfeng'), ('Lincoln', 'Lincoln'), ('GMC', 'GMC'), ('Alfa Romeo', 'Alfa Romeo'), ('Chrysler', 'Chrysler'), ('Lotus', 'Lotus'), ('Isuzu', 'Isuzu'), ('Smart', 'Smart'), ('FAW', 'FAW'), ('DS', 'DS'), ('Rover', 'Rover'), ('Proton', 'Proton'), ('Genesis', 'Genesis'), ('Zotye', 'Zotye'), ('Lancia', 'Lancia'), ('Bugatti', 'Bugatti'), ('Bentley', 'Bentley'), ('Rolls-Royce', 'Rolls-Royce'), ('Maserati', 'Maserati'), ('Aston Martin', 'Aston Martin'), ('Ferrari', 'Ferrari'), ('Lamborghini', 'Lamborghini'), ('Pagani', 'Pagani'), ('McLaren', 'McLaren'), ('Maybach', 'Maybach'), ('Scion', 'Scion'), ('Tata', 'Tata'), ('Mahindra', 'Mahindra'), ('Maruti', 'Maruti'), ('Perodua', 'Perodua'), ('BAIC', 'BAIC'), ('Foton', 'Foton'), ('GAC', 'GAC'), ('JAC', 'JAC'), ('Hino', 'Hino'), ('SsangYong', 'SsangYong'), ('Iran Khodro', 'Iran Khodro'), ('Luxgen', 'Luxgen'), ('Dodge', 'Dodge'), ('Pontiac', 'Pontiac'), ('Saturn', 'Saturn'), ('Oldsmobile', 'Oldsmobile'), ('Hummer', 'Hummer'), ('Scania', 'Scania'), ('MAN', 'MAN'), ('Kenworth', 'Kenworth'), ('Peterbilt', 'Peterbilt'), ('Mack', 'Mack'), ('IVECO', 'IVECO'), ('Gaz', 'Gaz'), ('UAZ', 'UAZ'), ('Buggy', 'Buggy'), ('Troller', 'Troller'), ('Navistar', 'Navistar'), ('DFSK', 'DFSK'), ('Wuling', 'Wuling')], help_text='Марка', max_length=100),
        ),
    ]
