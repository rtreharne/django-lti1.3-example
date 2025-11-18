from django.contrib import admin
from django.apps import apps

# ---------------------------------------------------------------
# Automatically register ALL models in the 'tool' app
# ---------------------------------------------------------------

app = apps.get_app_config('tool')

for model_name, model in app.models.items():
    # Skip if already registered manually
    if admin.site.is_registered(model):
        continue

    # Create a generic ModelAdmin with sensible defaults
    class GenericAdmin(admin.ModelAdmin):
        list_display = [
            field.name for field in model._meta.fields
            if field.get_internal_type() not in ("TextField",)
        ]
        search_fields = [
            field.name for field in model._meta.fields
            if field.get_internal_type() in ("CharField", "SlugField", "TextField")
        ]
        list_filter = [
            field.name for field in model._meta.fields
            if field.get_internal_type().endswith("Field") and not field.many_to_many
            and field.get_internal_type() != "TextField"
        ]

    try:
        admin.site.register(model, GenericAdmin)
    except admin.sites.AlreadyRegistered:
        pass
