# Generated by Django 3.2 on 2023-05-06 10:46

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExampleModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('content', mdeditor.fields.MDTextField()),
            ],
        ),
    ]
