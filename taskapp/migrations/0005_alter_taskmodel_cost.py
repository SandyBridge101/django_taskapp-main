# Generated by Django 4.1 on 2022-09-03 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0004_alter_taskmodel_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]