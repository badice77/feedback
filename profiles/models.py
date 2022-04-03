from django.db import models

# Create your models here.

class UserProfile(models.Model):
    image = models.ImageField(upload_to="images")
    title = models.TextField(default = "GOOOOOOOOOOOOOOOOOOOL is best")

    def __str__(self):
        return self.title