# Generated by Django 4.2.16 on 2024-11-29 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Blog.category'),
            preserve_default=False,
        ),
    ]
