from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    fullName = models.CharField(max_length=128)
    photoUrl = models.URLField(blank=True)
    profile = models.CharField(max_length=128, blank=True)

    def __str__(self):
        return self.fullName + ' (' + self.user.username + ')'