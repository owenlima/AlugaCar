# Generated by Django 5.1 on 2024-08-19 16:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cars', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(choices=[('AWAITING_PAYMENT', 'Awaiting Payment'), ('IN_PROGRESS', 'In Progress'), ('COMPLETED', 'Completed'), ('CANCELED', 'Canceled')], default='AWAITING_PAYMENT', max_length=20)),
                ('odometer_last', models.IntegerField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentals', to='cars.cars')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentals', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Rental',
                'verbose_name_plural': 'Rentals',
                'db_table': 'rentals',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL)),
                ('rentail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='rental.rental')),
            ],
            options={
                'verbose_name': 'Payment',
                'verbose_name_plural': 'Payments',
                'db_table': 'payments',
                'managed': True,
            },
        ),
    ]
