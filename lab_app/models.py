from django.contrib.auth.models import User
from django.db import models
from registration import forms


class Media(models.Model):
    user = models.ForeignKey(User)
    file = models.FileField(upload_to="files")
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
