from . import views
from django.urls import path, include
# from rest_framework import routers
from .views import *


# router = routers.DefaultRouter()
# router.register('tasks', viewset=views.TaskList)
# router.register('tags', viewset=views.TagList)
# router.register('taskTags', viewset=views.TaskTagList)
# router.register('ColumnAttributes', viewset=views.ColumnAttributeList)
# router.register('comments', viewset=views.CommentList)
# router.register('projects', viewset=views.ProjectList)
# router.register('customColumnValues', viewset=views.CustomColumnValueList)
# router.register('permission', viewset=views.PermissionList)
# router.register('taskAttribute', viewset=views.TaskAttributeList)


urlpatterns = [
    # path('', include(router.urls)),
    #To user list:response users list
    path('api/users/',ListUsers.as_view()),

    #To view tokens: response user_id,token and email
    path('api/token/auth/', CustomAuthToken.as_view()),

    # create user
    path('api/createUser/',views.userCreate,name="usercreate"),

    #Projects related routes
    path('api/project/',Projects.as_view()),
    path('api/project/<str:pk>/',Projects.as_view()),

    #Tag related route
    path('api/tag/',Tags.as_view()),
    path('api/tag/<str:pk>/',Tags.as_view()),

    # Task related routes
    path('api/task/',Tasks.as_view()),
    path('api/task/<str:pk>/',Tasks.as_view()),


    #TaskTags related routes
    path('api/tasktag/',TaskTags.as_view()),
    path('api/tasktag/<str:pk>/',TaskTags.as_view()),

    #TaskAttributes related routes
    path('api/taskAttribute/',TaskAttributes.as_view()),
    path('api/taskAttribute/<str:pk>/',TaskAttributes.as_view()),

    #ColumnAttribute related routes
    path('api/columnattribute/',ColumnAttributes.as_view()),
    path('api/columnattribute/<str:pk>/',ColumnAttributes.as_view()),
    
    #CustomColumnValue related routes
    path('api/customColumnValue/',CustomColumnValues.as_view()),
    path('api/customColumnValue/<str:pk>/',CustomColumnValues.as_view()),

    #Comment related routes
    path('api/comment/',Comments.as_view()),
    path('api/comment/<str:pk>/',Comments.as_view()),

   
    #Permissions related routes
    path('api/permission/',Permissions.as_view()),
    path('api/permission/<str:pk>/',Permissions.as_view()),
]
