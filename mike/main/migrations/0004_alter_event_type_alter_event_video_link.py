# Generated by Django 4.2 on 2023-05-02 17:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_alter_event_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="event",
            name="type",
            field=models.CharField(
                choices=[
                    ("video_design", "video design"),
                    ("av_performance", "a/v performance"),
                    ("visuals", "visuals"),
                    ("typeless", "Неопределенный"),
                ],
                default="typeless",
                max_length=15,
                verbose_name="type of event",
            ),
        ),
        migrations.AlterField(
            model_name="event",
            name="video_link",
            field=models.URLField(
                blank=True,
                help_text="If Youtube link like this: https://www.youtube.com/embed/kLiVzoNSDh4 if Vimeo: https://player.vimeo.com/video/819819044",
                null=True,
            ),
        ),
    ]
