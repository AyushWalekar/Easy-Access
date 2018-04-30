from django.shortcuts import render

from django.urls import resolve

from django.conf import settings
import os
import platform

from .forms import UserForm
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def homepage(request):
    if 'username' not in request.session:
        return render(request, 'blog/login.html', {})
    return render(request,'blog/homepage.html')


def post_list(request):
    #to check the session.
    if 'username' not in request.session:
        return render(request, 'blog/login.html', {})
    #sub_folder_path = request.GET.get('sub_folder_path')
    #current_url = resolve(request.path_info).url_name
    #sub_folder_path = current_url

    current_url = request.path
    sub_folder_path = current_url 
    static_folder_path = "/home/admin1/Desktop/django_test2/blog/static"

    if sub_folder_path is not None :
        static_folder_path = static_folder_path + sub_folder_path 
        
    test_directory = static_folder_path
    dir_list = []
    file_list = []
    #to create a directory structure of the requested path
    if os.path.isdir(test_directory):
        for child in os.listdir(test_directory):
            test_path = os.path.join(test_directory, child)
            if os.path.isdir(test_path):
                dir_list.append(child)
            else:
                file_list.append(child)
    else:
        file_loc = settings.STATIC_URL[:-1] +  current_url
        return render(request, 'blog/play_video.html', {"file_loc": file_loc})           
    return render(request, 'blog/post_list.html', {"file_list": file_list, "dir_list": dir_list, "username": request.session['username'], })
#to authenticate an authorized user.
def login(request):
    username = 'not logged in'
    if request.method == 'POST':
        userform = UserForm(request.POST)

        if userform.is_valid():
            username = userform.cleaned_data['username']
            if username == "Ayu":
                request.session['username'] = username
                request.session.set_expiry(0)
        else:
            userform = UserForm()
    return render(request, "blog/homepage.html",{"username": username})

#to take username and password from user
def formView(request):
   if request.session.has_key('username'):
      username = request.session['username']
      return render(request, 'blog/homepage.html', {"username": username})
   else:
      return render(request, 'blog/login.html', {})
#to drop the session
def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request,"blog/login.html",{})
