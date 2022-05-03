from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_lengh = 50)
    content = models.Textfield()

    def__str__(self):
    return self.title 