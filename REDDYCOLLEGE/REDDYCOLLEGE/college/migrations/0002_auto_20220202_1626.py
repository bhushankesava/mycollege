# Generated by Django 3.2 on 2022-02-02 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
