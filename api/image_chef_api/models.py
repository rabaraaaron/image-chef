from django.db import models


class Prompt(models.Model):
    prompt = models.TextField()

    def __str__(self):
        # Optional: how the object will be represented as a string
        return self.prompt[:200]  # First 200 characters
