"""readit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from blog import views as blog_view
from django.contrib.auth import views as auth_view
from users import views as user_view
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('myarticles/',blog_view.MyArticles.as_view(),name="my-articles"),
    path('register/',user_view.register,name="register"),
    path('cdelete/<int:pk>/<int:x>/',blog_view.CommentDelete,name="cdelete"),
    path('profile/',user_view.profile,name="profile"),
    path('article/<int:pk>/',blog_view.PostDetailView,name="article-detail"),
    path('article/new/',blog_view.PostCreateView.as_view(),name="article-create"),
    path('article/<int:pk>/update/',blog_view.PostUpdateView.as_view(),name="article-update"),
    path('article/<int:pk>/delete/',blog_view.PostDeleteView.as_view(),name="article-delete"),
    path('login/',auth_view.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('like/article/<int:pk>/',blog_view.ArticleLike,name="article-like"),
    path('dislike/article/<int:pk>/',blog_view.ArticleDislike,name="article-dislike"),
    path('comment/',blog_view.ArticleComment,name="article-comment"),
    path('logout/',auth_view.LogoutView.as_view(template_name='users/logout.html'),name='logout')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)