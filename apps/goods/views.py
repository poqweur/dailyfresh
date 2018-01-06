from django.shortcuts import render
from django.http import HttpResponse

# Ê×Ò³ÊÓÍ¼
def Index(request):
    return render(request,'index.html')
    # return HttpResponse('ok')
