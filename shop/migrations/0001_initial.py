# Generated by Django 4.2.3 on 2023-09-06 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('composition', models.TextField()),
                ('energy_value', models.PositiveIntegerField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image_url', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='image/', verbose_name='Изображение товара')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['pk'],
            },
        ),
    ]
