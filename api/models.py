from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100000)

class Game(models.Model):  
    name = models.TextField()
    description = models.TextField()
    image = models.TextField()
    category = models.ForeignKey(Category, on_delete=Category, blank=True, null=True)
    price = models.FloatField()
    screenshots = models.TextField()
    text = models.TextField()

class Review(models.Model):
    username = models.CharField(max_length=200)
    rating = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=Category, blank=True, null=True)
    text = models.TextField()

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class Manager(User):
    pass    