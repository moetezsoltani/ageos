from django.contrib import admin
from .models import Event, Publication, Formation  # Import the Formation model
from ageos_project.admin import admin_site  # Import the custom admin site

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')  # Adjust as per your actual fields
    list_filter = ('date', 'location')  # Adjust as per your actual fields
    fields = ('title', 'date', 'location', 'description', 'image')  # Include image in the admin form
    actions = ['delete_selected']  # Add this line to enable delete option

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'author')  # Adjust as per your actual fields
    list_filter = ('published_date', 'author')  # Adjust as per your actual fields
    fields = ('title', 'published_date', 'author', 'content', 'image')  # Include image in the admin form
    actions = ['delete_selected']  # Add this line to enable delete option

# Define the admin options for the Formation model
class FormationAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')  # Adjust as per your actual fields
    list_filter = ('date',)  # Adjust as per your actual fields
    fields = ('title', 'date', 'description', 'image')  # Include image in the admin form
    actions = ['delete_selected']  # Add this line to enable delete option

# Register with the custom admin site
admin_site.register(Event, EventAdmin)
admin_site.register(Publication, PublicationAdmin)
admin_site.register(Formation, FormationAdmin)  # Register Formation with the custom admin site


