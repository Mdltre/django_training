# Generated by Django 4.2 on 2023-05-02 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_publisher_remove_author_full_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='classification',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercises', to='exercises.classification'),
        ),
        migrations.AddField(
            model_name='publisher',
            name='website',
            field=models.URLField(null=True),
        ),
    ]
