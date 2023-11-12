from django.db import models

class File(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')