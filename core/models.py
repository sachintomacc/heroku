from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    phone = models.IntegerField()

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    comments = models.IntegerField(default=0)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
