from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()
    email = models.TextField(unique=True)
    password_hash=models.TextField()

class Session(models.Model):
    token = models.TextField()
    user = models.OneToOneField("User", on_delete=models.CASCADE)

class Destination(models.Model):
    name = models.TextField()
    review = models.TextField()
    rating = models.IntegerField()
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    share_publicly = models.BooleanField()


