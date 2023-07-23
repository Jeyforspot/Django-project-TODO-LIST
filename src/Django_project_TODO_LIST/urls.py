from django.contrib import admin
from django.urls import include, path
from ToDoList.views import render_main_page

urlpatterns = [
    path('', render_main_page, name='main_page'),
    path('all-tasks/', include('ToDoList.urls')),
    path('admin/', admin.site.urls),
]
