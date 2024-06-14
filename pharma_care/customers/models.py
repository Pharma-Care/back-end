from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    id_number = models.CharField(max_length=255, unique=True, blank=False, null=False)

    def __str__(self):
        return self.name
    