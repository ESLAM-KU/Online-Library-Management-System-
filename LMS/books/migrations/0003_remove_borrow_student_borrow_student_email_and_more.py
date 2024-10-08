# Generated by Django 5.1.1 on 2024-09-11 11:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_borrow_return_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrow',
            name='student',
        ),
        migrations.AddField(
            model_name='borrow',
            name='student_email',
            field=models.EmailField(blank=True, max_length=254, null=True, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='borrow',
            name='return_date',
            field=models.DateTimeField(null=True),
        ),
    ]
