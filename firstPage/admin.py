from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from .models import *
from .resources import *

# Register your models here.
admin.site.register(StatementEntries)
admin.site.register(ItemSetting)
admin.site.register(ItemFact)
admin.site.register(IndexInfo)


@admin.register(Exchange)
class ExchangeAdmin(ImportExportModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(ImportExportModelAdmin):
    list_display = ("ticker", "name", "exchange", "industry")
    pass


@admin.register(StockInfo)
class StockInfoAdmin(ImportExportModelAdmin):
    list_display = ("ticker", "day", "close", "volume")
    pass


@admin.register(Industry)
class IndustryAdmin(ImportExportModelAdmin):
    list_display = ("industry_code", "industry")
    pass
