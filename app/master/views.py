from django.shortcuts import render

# Create your views here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps
from .models import MasterModel
import os

@receiver(post_save)
def save_model_metadata(sender, instance, created, **kwargs):
    if sender == MasterModel:
        return

    if created:
        template_name = f"{sender.__name__.lower()}.html"  # Example: 'product.html'
        template_path = os.path.join('templates', template_name)

        # Save model name and template path to MasterModel
        MasterModel.objects.get_or_create(
            model_name=sender.__name__,
            defaults={'template_path': template_path}
        )