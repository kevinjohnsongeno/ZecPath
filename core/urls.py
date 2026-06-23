from django.urls import path
from . views import JobList,UserList,JobCreate,UserCreate,ApplicationList
urlpatterns = [
    path('jobs/',JobList.as_view(),name='job-list'),
    path('users/',UserList.as_view(),name='user-list'),
    path('jobs/create/',JobCreate.as_view(),name='job-create'),
    path('users/create/',UserCreate.as_view(),name='user-create'),
    path('app/',ApplicationList.as_view(),name='application-list'),
]