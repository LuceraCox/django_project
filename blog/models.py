from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# One to many relationship

# Each class is own table in db, each attr is dif field in db
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # if a user is deleted, also delete their post

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
