from django.db import models

class UploadedAudio(models.Model):
    file = models.FileField(upload_to='uploads/')




