# Generated by Django 5.1.1 on 2024-09-11 13:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_borrow_student_borrow_student_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='borrow_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
