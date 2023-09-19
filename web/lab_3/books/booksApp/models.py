from django.db import models


# Create your models here.
class Books(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    author = models.TextField()
    price = models.SmallIntegerField()
    descr = models.TextField()

    def __str__(self):
        return self.title
