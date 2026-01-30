from instructorApp.models import Order
from django.contrib import messages
from django.shortcuts import redirect

def course_count(request):
    if request.user.is_authenticated:
        orders=Order.objects.filter(user_instance=request.user,is_paid=True).count()
        return {'order_count':orders}
    else:
        return {'order_count':0}
    

def login_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            messages.warning(request,"You must login first")
            return redirect('student_login')
        else:
            return fn(request,*args,**kwargs)
    return wrapper
