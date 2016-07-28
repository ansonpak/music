from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    fullName = models.CharField(max_length=128)
    photoUrl = models.URLField(blank=True, default='http://www.aspirehire.co.uk/aspirehire-co-uk/_img/profile.svg')
    profile = models.CharField(max_length=128, blank=True, default='')

    def __str__(self):
        return self.user.username