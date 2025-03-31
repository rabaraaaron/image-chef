from django.db import models


class Prompt(models.Model):
    prompt = models.TextField()

    def __str__(self):
        return self.prompt[:200]


class ImageToImage(models.Model):
    prompt = models.TextField()
    image = models.ImageField()
    mask = models.ImageField()

    def __str__(self):
        return self.prompt[:200] + image.name + mask.name
