from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("movies", "0002_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="source",
            field=models.CharField(blank=True, default="", max_length=255),
        ),
        migrations.AddField(
            model_name="review",
            name="source_url",
            field=models.URLField(blank=True, default=""),
        ),
    ]
