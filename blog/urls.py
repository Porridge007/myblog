from django.conf.urls import url
from . import views

import blog.views as bv
urlpatterns = [
    url(r'^$', views.index),
]
