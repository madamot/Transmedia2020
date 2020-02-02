from django.db import models
from django.urls import reverse
import datetime

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField()
    date = models.DateField(("Date"), default=datetime.date.today)
    blogImg = models.CharField(max_length=500)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', args=[str(self.id)])
