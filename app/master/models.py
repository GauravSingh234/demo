from django.db import models

# Create your models here.
class MasterModel(models.Model):
    model_name = models.CharField(max_length=255)
    creation_date = models.DateTimeField(auto_now_add=True)
    template_path = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.model_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)


# Forms
class FormField(models.Model):
    label = models.CharField(max_length=100)
    field_type = models.CharField(
        max_length=50, choices=[
            ('text', 'Text'),
            ('email', 'Email'),
            ('password', 'Password'),
            ('textarea', 'Textarea'),
        ]
    )
    is_required = models.BooleanField(default=True)

    def __str__(self):
        return self.label