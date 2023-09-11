# Generated by Django 4.0.2 on 2023-09-05 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_delete_stor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milk_storage', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('expance', models.DecimalField(decimal_places=2, max_digits=100, null=True)),
            ],
        ),
    ]
