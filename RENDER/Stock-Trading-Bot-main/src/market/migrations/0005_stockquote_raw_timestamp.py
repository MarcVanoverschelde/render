# Generated by Django 5.1.3 on 2024-11-12 23:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0004_alter_stockquote_unique_together"),
    ]

    operations = [
        migrations.AddField(
            model_name="stockquote",
            name="raw_timestamp",
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]
