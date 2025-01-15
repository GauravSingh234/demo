from django.db import models

# Create your models here.
# Slider/Carousel
class Slider(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to='static/images/slider/images/' ,null=True)
    image2 = models.ImageField(upload_to='static/images/slider/images/'  ,null=True)
    image3 = models.ImageField(upload_to='static/images/slider/images/' ,null=True)
    link = models.URLField(blank=True, null=True)  # Optional link for the slide
    order = models.PositiveIntegerField(default=0)  # Display order
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


# Cards
class Card(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='static/images/cards/images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# Buttons
class Button(models.Model):
    label = models.CharField(max_length=100)
    action = models.CharField(max_length=200, blank=True, null=True)  # Optional URL or JS action
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.label


# Images
class Image(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='static/images/images/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Image"