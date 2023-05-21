from django.shortcuts import render
import pandas as pd
# Create your views here.
from django.shortcuts import HttpResponse
from cmdb.models import Device

# def index(request):     #从Excel提取数据
#     devs_df = pd.read_excel('cmdb/inventory.xlsx')
#     devs = devs_df.to_dict(orient='records')
#     data = {'devs':devs}
#     return render(request, 'cmdb/index.html', context=data)

def index(request):
    device_objs = Device.objects.all()
    data = {'devs': device_objs}
    return render(request, 'cmdb/index.html', context=data)