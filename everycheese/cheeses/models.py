from django.db import models

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
        Hard = "hard", "Hard"

    name = models.CharField("Name of cheese", max_length=255)
    slug = AutoSlugField("Cheese Address",
                         unique=True, always_update=False, populate_from="name")
    description = models.TextField("Description", blank=True) # use TextField when might need more then 255 characters
    firmness = models.CharField("Firmness", max_length=20, choices=Firmness.choices, default=Firmness.UNSPECIFIED)

    def __str__(self):
        return self.name
