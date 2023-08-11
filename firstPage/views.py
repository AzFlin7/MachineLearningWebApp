import json

import pandas as pd
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from template import *
from .forms import *

# Create your views here.
from .lr_prediction import lr_prediction
from .models import StockInfo


def index(request):
    # companies = [obj.ticker for obj in Company.objects.all()]
    form = CompanyForm(request.POST, initial=0)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {'form': CompanyForm(request.POST)}

    return render(request, 'company_template.html', context)


@api_view(('GET',))
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def predictStockPrice(request):
    symbol = request.GET['Company']
    data = lr_prediction(symbol)
    data['day'] = pd.to_datetime(data.day, format='%Y-%m-%d')
    data['day'] = data['day'].dt.strftime('%Y-%m-%d')
    data = data.set_index('day')
    out = {'labels': data.index.tolist(), 'datasets': []}
    out['datasets'].append({
        'label': 'Close',
        'data': data['close'].values.tolist(),
        'backgroundColor': 'rgba(255,99,132,0.2)'
    })
    out['datasets'].append({
        'label': 'PredictClose',
        'data': data['pclose'].values.tolist(),
        'backgroundColor': 'rgba(54,162,64,0.2)'
    })

    # data = json.loads(result)
    return Response({'data': out}, template_name='index.html')
# return render(request, 'index.html', {'data': data})
