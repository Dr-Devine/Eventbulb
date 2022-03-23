from random import choices
from django.db import models
from django.contrib.auth.models import User




class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now=False, auto_now_add=False)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='upload/', blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):

    class Rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    rating = models.IntegerField(choices=Rating.choices)
    text = models.TextField()

    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, blank=True, null=True, related_name="reviews")
    profile = models.ForeignKey(
        "accounts.UserProfile", on_delete=models.CASCADE, blank=True, related_name="reviews")

# class Review(models.Model):
#     user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
#     event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
#     # rating = models.IntegerChoices(choices=range)
#     text = models.TextField()
