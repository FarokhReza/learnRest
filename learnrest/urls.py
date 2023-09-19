from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    # path('<str:name>/', views.Home.as_view(), name='home'),  # ar
    path('', views.Home.as_view()),
    path('questions/<int:pk>/', views.QuestionView.as_view()),
    path('questions/', views.QuestionView.as_view()),
    path('accounts/', include('accounts.urls', namespace='accounts'))
]
