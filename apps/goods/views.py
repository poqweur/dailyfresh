from django.shortcuts import render
from django.http import HttpResponse

# ��ҳ��ͼ
def Index(request):
    return render(request,'index.html')
    # return HttpResponse('ok')
