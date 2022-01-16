from django.urls import path
from . import views

urlpatterns = [
    #path('blog/', views.blog, name='blog'),
    #path('blog-post/', views.blog_post, name='blog-post'),
    path('blog/', views.postList, name='blog'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.postDetail,  name='blog_detail'),
]