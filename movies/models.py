from django.contrib.auth.models import User
from django.db import models
from django.conf import settings


# Create your models here.
class Movies(models.Model):
    class Ratings(models.IntegerChoices):
        AMAZING = 5, 'absolute cinema'
        GOOD = 4, 'not sure if its amazing'
        AVERAGE = 3, 'worth one watch'
        BAD = 2, 'its bad but it cant get worse'
        WORST = 1, 'waste of time'

    title = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='movies_rated')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(max_length=1, choices=Ratings, default=Ratings.AMAZING)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Movies, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"comment by {self.user.username} on {self.post.title}: {self.content[0:25]}"
