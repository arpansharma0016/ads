from django.db import models

class Person(models.Model):
    points = models.IntegerField(default=0)
    username = models.TextField()

    def __str__(self):
        return self.username, self.points
    
class Yt(models.Model):
    video_id = models.TextField()
    views = models.IntegerField(default=0)
    demand = models.IntegerField(default=0)
    username = models.TextField()
    category = models.TextField(default='Vlog')

    def __str__(self):
        return self.username

class Viewed(models.Model):
    video_id = models.TextField()
    username = models.TextField()
    time = models.TextField()

    def __str__(self):
        return self.username

