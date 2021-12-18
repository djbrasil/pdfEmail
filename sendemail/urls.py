from django.urls import path, re_path
from sendemail import views
from sendemail.views import (NewView, IndexView, DeleteView, UpdateView, ListView)

# app_name = "equipment"

urlpatterns = [
	path('', IndexView.as_view(), name='index'),
	path('table/', ListView.as_view(), name='table'), 
	path('novo/', NewView.as_view(), name='novo'), 
	path('<int:pk>/alterar/', UpdateView.as_view(), name='alterar'),
	path('<int:pk>/delete/', DeleteView.as_view(), name='delete'),  
]