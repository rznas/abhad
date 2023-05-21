from django.contrib import admin
from jalali_date import datetime2jalali, date2jalali
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin
from cognitive.models import Soldier, Skill, SoldierRelevant

# Register your models here.

@admin.register(Soldier)
class SoldierAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    model = Soldier
    list_display = ['name', 'rank', 'military_id', 'dispath_date_jalali', 'birth_date_jalali']
    search_fields = ['name', 'rank', 'military_id', 'national_id', 'skills', 'education_field']
    autocomplete_fields = ['skills']

    @admin.display(description='تاریخ تولد', ordering='created')
    def birth_date_jalali(self, obj: Soldier):
        return date2jalali(obj.birth_date).strftime('%Y/%m/%d')
    
    @admin.display(description='تاریخ اعزام', ordering='created')
    def dispath_date_jalali(self, obj: Soldier):
        return date2jalali(obj.dispatch_date).strftime('%Y/%m/%d')
    
    @admin.display(description='نام و نشان', ordering='created')
    def name(self, obj: Soldier):
        return f'{obj.first_name} {obj.last_name}'


@admin.register(Skill)
class SkillModelAdmin(admin.ModelAdmin):
    model = Skill
    search_fields = ['name']


@admin.register(SoldierRelevant)
class BaseAdmin(admin.ModelAdmin):
    pass
