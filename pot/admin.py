from django.contrib import admin
from .models import Plant, History_Pest, History_Water

# Register your models here.


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display=['id','plant_name','alarm','humidity','threadhold', 'customer']
    list_filter=['plant_name']


@admin.register(History_Pest)
class History_PestAdmin(admin.ModelAdmin):
    list_display=['id','pest_name','create_at','img','plant']
    # list_filter=['']

@admin.register(History_Water)
class History_WaterAdmin(admin.ModelAdmin):
    list_display=['id','plant', 'create_at']
    # list_filter=['']
