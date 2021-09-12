from django.db import models

class Confirm(models.Model):
    username = models.TextField()
    name = models.TextField()
    email = models.TextField()
    password = models.TextField()
    otp = models.TextField()
    attempts = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Password(models.Model):
    email = models.TextField()
    otp = models.TextField()
    confirmed = models.BooleanField(default=False)
    attempts = models.IntegerField(default=0)

    def __str__(self):
        return self.email

class Referral(models.Model):
    username = models.TextField()
    referred_username = models.TextField()

    def __str__(self):
        return self.username
    