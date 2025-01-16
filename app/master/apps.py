from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.db import models

class MasterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.master'


    def ready(self):
        post_migrate.connect(self.populate_master_model, sender=self)

    def populate_master_model(self, **kwargs):
        from .models import MasterModel  # Import your MasterModel here

        # Iterate over all models in the app
        for model in self.get_models():
            model_name = model.__name__
            template_name = f"{model_name.lower()}.html"
            template_path = f"templates/{template_name}"

            # Check if model already exists in MasterModel
            MasterModel.objects.get_or_create(
                model_name=model_name,
                defaults={'template_path': template_path}
            )