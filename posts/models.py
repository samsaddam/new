from unicodedata import name
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Post(models.Model):
    class Meta(object):
        db_table = 'post'


    name = models.CharField(
        'Name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
        )

    body = models.CharField(
        'Body', blank=True, null=True, max_length=140, db_index=True
        )

    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
        )

    likes = models.IntegerField(
        'Like_Count', default=0, blank=True
     )

    picture = CloudinaryField(
        'Picture', blank=True, db_index=True
        )

    def __str__(self):
        return '{} ||| {} ||| {}'.format(self.name, self.likes, self.created_at)

    @property
    def total_likes(self):
        return self.likes.count()