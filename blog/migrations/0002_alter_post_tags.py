# Generated by Django 4.1.3 on 2022-12-01 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(blank=True, null=True, to="blog.tag"),
        ),
    ]
