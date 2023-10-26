from django.db import models
from django.core.validators import MinLengthValidator


class TreeMenu(models.Model):
    name = models.CharField(
        max_length=128,
        validators=[
            MinLengthValidator(1),
        ],
    )
    path = models.TextField(unique=True)
    parent = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='children'
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        parent = self.parent
        if parent is None:
            self.path = self.name
        else:
            self.path = "%s/%s" % (self.parent.path, self.name)

        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "меню"
        verbose_name_plural = "меню"

# Create your models here.
