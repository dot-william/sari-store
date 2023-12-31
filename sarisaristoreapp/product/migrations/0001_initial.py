# Generated by Django 2.1.7 on 2023-09-08 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='')),
                ('brand', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.DecimalField(decimal_places=1, max_digits=1000)),
                ('expiration_date', models.DateField(help_text='Please use the following format YYYY-MM-DD')),
            ],
        ),
    ]
