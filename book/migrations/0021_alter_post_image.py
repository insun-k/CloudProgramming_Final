# Generated by Django 4.2.2 on 2023-06-18 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0020_alter_post_book_name_alter_post_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='book/images/%Y/%m/%d/'),
        ),
    ]
