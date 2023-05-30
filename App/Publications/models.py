from django.db import models

class Publication(models.Model):
    file = models.FileField(upload_to='Publiations/', unique=True)
