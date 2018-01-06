from django.contrib.auth.views import login_required
#@login_request,装饰器可以给视图函数使用,如果是视图类需要重写
#如果用户没有登录
class Definition(object):
    @classmethod
    def as_view(clsc,**initkwargs):
        #首先调用父类的as_view
        view =super().as_view(**initkwargs)
        return login_required(view)