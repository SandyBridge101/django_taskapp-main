# Generated by Django 4.1 on 2022-09-04 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0008_report_alter_taskmodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='projectmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='taskmodel',
            name='taskproject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='taskapp.projectmodel'),
        ),
    ]
