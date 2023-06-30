# from month_year_field.fields import MonthYearField
from django.db import models


class Event(models.Model):
    """Event."""

    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    date = models.DateField("date of event")
    description = models.TextField(null=True, blank=True)
    # images = models.ManyToManyField(Image, related_name="events", blank=True)
    video_link = models.URLField(
        null=True,
        blank=True,
        help_text=(
            "If Youtube link like this: "
            "https://www.youtube.com/embed/kLiVzoNSDh4 "
            "if Vimeo: "
            "https://player.vimeo.com/video/819819044"
        ),
    )

    class TypeChoice(models.TextChoices):
        TYPELESS = "typeless", "HIDDEN"
        MEDIA_ARTIST = "media_artist", "MEDIA ARTIST"
        VIDEO_DESIGN = "video_design", "VIDEO DESIGN"
        AV_PERFORMANCE = "av_performance", "A/V PERFORMANCE"
        VISUALS = "visuals", "VISUALS"

    type = models.CharField(
        "type of event",
        max_length=15,
        choices=TypeChoice.choices,
        default=TypeChoice.TYPELESS,
    )

    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date of add", auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["-date"]


class Image(models.Model):
    """Image."""

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(
        upload_to="images",
    )

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
