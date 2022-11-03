# -*- coding: utf-8 -*-
from rest_framework import routers

from cent import views

urlpatterns = [

]
staff = routers.SimpleRouter()
staff.register('staff', views.StaffView)
urlpatterns += staff.urls
