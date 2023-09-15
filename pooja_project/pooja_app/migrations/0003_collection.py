# Generated by Django 4.2.5 on 2023-09-14 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pooja_app', '0002_person_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection_name', models.CharField(max_length=100)),
                ('collection_price', models.IntegerField()),
                ('collection_image', models.ImageField(upload_to='pooja_app/images/collections')),
            ],
        ),
    ]