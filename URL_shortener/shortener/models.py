from django.db import models

class Url(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=6, unique=True, null=True)

    def __str__(self):
        return self.original_url
