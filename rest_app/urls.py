from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('students',setview)
urlpatterns = [
    path('create/',crudoperation.as_view()),
    path('get/',crudoperation.as_view()),
    path('get/<int:student_id>/',crudoperation.as_view()),
    path('put/<int:student_id>/',crudoperation.as_view()),
    path('delete/<int:student_id>/',crudoperation.as_view()),
    # path('students/',getandpostgenerics.as_view()),
    # path('students/<int:pk>/',retrivegenerics.as_view())
    path('crud/',include(router.urls))

]
