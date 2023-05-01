from django.db import models
from users.models import User

# Create your models here.
class Theme(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

class State(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    text = models.TextField()
    photo = models.ImageField(upload_to='state_photo/%Y/%m/%d',blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    theme = models.ForeignKey(Theme, on_delete=models.PROTECT, default=None)


    @property
    def imageURL(self):
        return self.photo.url

    def __str__(self):
        return f' {self.title} by - {self.author}'
    

class Like(models.Model):
    count = models.IntegerField(default=0)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    text = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)