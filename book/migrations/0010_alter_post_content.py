# Generated by Django 4.2.2 on 2023-06-18 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0009_alter_post_book_name_alter_post_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]