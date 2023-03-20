from django.db import models
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    # id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author')

    def __str__(self):
        return self.title, self.created_at

    def get_absolute_url(self):
        return reverse('hello', args=[str(self.id)])
