from django.test import TestCase
import tablib
from import_export import resources
from .models import Industry

# Create your tests here.
industry_resource = resources.modelresource_factory(model=Industry)()
dataset = tablib.Dataset(['', 'New book'], headers=['id', 'industry', 'industry_code'])
result = industry_resource.import_data(dataset, dry_run=True)
print(result.has_errors())
