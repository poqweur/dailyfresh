from django.contrib.auth.views import login_required
#@login_request,װ�������Ը���ͼ����ʹ��,�������ͼ����Ҫ��д
#����û�û�е�¼
class Definition(object):
    @classmethod
    def as_view(clsc,**initkwargs):
        #���ȵ��ø����as_view
        view =super().as_view(**initkwargs)
        return login_required(view)