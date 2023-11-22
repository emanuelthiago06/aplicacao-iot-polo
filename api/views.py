from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from api.models import Sensor
from django.utils import timezone


# Create your views here.


def view_graph(request):
    if request.method == "POST" and "clean_database" in request.POST:
        Sensor.objects.all().delete()
    data = []
    dates =[]
    bellow_1_count = []
    sensores = Sensor.objects.all()
    for i in sensores:
        date = i.created_at
        if not date:
            continue
        data.append(i.value)
        if i.value < 1:
            bellow_1_count.append(i.value)
        dates.append(date.strftime("%Y-%m-%d %H:%M"))
    print(bellow_1_count)

    context = {
        'data': data,
        'labels': dates,
        'below_1_count': len(bellow_1_count),
        'average_value': 0 if not data else sum(data)/len(data)
    }
    return render(request, 'plot.html', context)


@csrf_exempt
def add_point(request):
    if request.method == "POST":
        value = float(request.POST.get('value', 0))
        print(value)
        new_entry = Sensor(value=value, created_at= timezone.now())
        new_entry.save()
        return JsonResponse({
            "status" : 200
        })
