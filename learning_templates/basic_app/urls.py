from django.urls import path
from . import views

#TEMPLATE TANGGING
app_name = 'basic_app'

urlpatterns= [
    path('relative', views.relative, name='relative'), #STEP 2: bring back relative view which links to template
    path('other', views.other, name='other'),
]
