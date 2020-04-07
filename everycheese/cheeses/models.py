from django.urls import reverse
from django.db import models
from django_countries.fields import CountryField
from django.conf import settings

# TimeStampedModel automatically gives the model created and modified fields,
# which automatically track when the object is created or modified.
from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField #autopopulating slug field

class Cheese(TimeStampedModel):

    # Note that we defined the firmness constants as variables within the scope of the Cheese model.
    # This allows us to do things like this comparison:
    # if cheese.firmness == Cheese.Firmness.SOFT
    class Firmness(models.TextChoices):
        UNSPECIFIED = "unspecified", "Unspecified"
        SOFT = "soft", "Soft"
        SEMI_SOFT = "semi-soft", "Semi-Soft"
        SEMI_HARD = "semi-hard", "Semi-Hard"
        HARD = "hard", "Hard"

    name = models.CharField("Name of cheese", max_length=255)
    slug = AutoSlugField("Cheese Address",
                         unique=True, always_update=False, populate_from="name")
    description = models.TextField("Description", blank=True) # use TextField when might need more then 255 characters
    firmness = models.CharField("Firmness", max_length=20, choices=Firmness.choices, default=Firmness.UNSPECIFIED)
    #We want country_of_origin to be optional, since it might be unknown for some cheeses, and so we set blank=True.
    # But we don’t set null=True because Django’s convention is to store empty values as the empty string, and to
    # retrieve NULL/empty values as the empty string.
    country_of_origin = CountryField("Country of Origin", blank=True) #from django-countries third party app

    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """Return absolute URL to the Cheese Detail page."""
        return reverse(
            'cheeses:detail', kwargs={"slug": self.slug}
        )
