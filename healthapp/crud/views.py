from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from.forms import UserInfoModelForm

# Create your views here.
from .models import UserInfo

def list_all_user(request):
    data = UserInfo.objects.all()

    context = {
        'data': data
    }

    return render(request, 'crud/list.html', context = context)


def detail_view_of_users(request, user_id):
    # try:
    #     user_obj = UserInfo.objects.get(id=user_id)
    # except UserInfo.DoesNotExist:
    #     return HttpResponse("User Doesnot Exist!")
    user_obj = get_object_or_404(UserInfo, id=user_id)

    return render(request, 'crud/detail.html', context={
        'user_obj': user_obj
    })


def create_user_info(request):
    if request.method == 'POST':
        # Form will get processed
        form = UserInfoModelForm(request.POST) 
        if form.is_valid():
            print(form.cleaned_data)
            print("Form is valid!")
            form.save()
            return redirect('/crud/list/')
        
        else:
            print("Form is invalid!")
    else:
        form = UserInfoModelForm()

    return render(request, 'crud/create.html', {'form': form})