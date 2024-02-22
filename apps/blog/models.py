from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'post'
        verbose_name = 'blog'

    def __str__(self):
        return self.title
    