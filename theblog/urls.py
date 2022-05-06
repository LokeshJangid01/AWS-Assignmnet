from os import name
from django.urls import path
from .views import HomeView,ArticalView,AddPosts,UpdatePost,DeletePost,AddCategory,Catagoryview


urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('Artical/<int:pk>',ArticalView.as_view(),name='detail-artilcal'),
    path('add_post/',AddPosts.as_view(),name='Add_Post'),
    path('add_category/',AddCategory.as_view(),name='Add_Category'),
    path('update_post/<int:pk>',UpdatePost.as_view(),name='updatePost'),
    path('delete_post/<int:pk>',DeletePost.as_view(),name='deletePost'),
    path('category/<str:cats>',Catagoryview,name='catagory')

]