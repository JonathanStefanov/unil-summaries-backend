# Generated by Django 5.0.1 on 2024-02-21 15:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("summaries", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="summary",
            name="rating",
        ),
        migrations.AlterField(
            model_name="summary",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="summaries",
                to="summaries.course",
            ),
        ),
        migrations.CreateModel(
            name="Vote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("upvoted", models.BooleanField(default=True)),
                (
                    "summary",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="votes",
                        to="summaries.summary",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "summary")},
            },
        ),
    ]
