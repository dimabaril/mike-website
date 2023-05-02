# from month_year_field.fields import MonthYearField
from django.db import models


class Image(models.Model):
    """Image."""

    # event = models.ForeignKey(
    #     to="Event",
    #     on_delete=models.CASCADE,
    #     # related_name="images",
    # )
    image = models.ImageField(
        upload_to="images",
        # related_name="images",
    )

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"


class Event(models.Model):
    """Event."""

    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    # author = models.CharField("author of event", max_length=50)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    date = models.DateField("date of event")
    location = models.CharField(max_length=50, null=True, blank=True)
    # image = models.ImageField(upload_to="images", null=True, blank=True)
    images = models.ManyToManyField(Image, related_name="events", blank=True)
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
        SET_DESIGN = "set_design", "set design"
        INTERACTIVE_CG = "interactive_cg", "interactive cg"
        UNTYPE = "untype", "Неопределенный"

    type = models.CharField(
        "type of event",
        max_length=15,
        choices=TypeChoice.choices,
        default=TypeChoice.UNTYPE,
    )

    pub_date = models.DateTimeField("date of add", auto_now_add=True)
    # pub_author = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ["-date"]
