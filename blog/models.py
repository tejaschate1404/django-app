from django.db import models

class Post(models.Model):
    sno =models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content=models.TextField()
    auther = models.CharField(max_length=13)
    slug = models.CharField(max_length=130,blank=True)
    timeStamp = models.DateTimeField(blank=True)

    def __str__(self):
        return " Message From " + self.title + ' by ' + self.auther

