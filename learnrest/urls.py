from django.contrib import admin
from rest_framework.schemas import get_schema_view
from django.urls import path, include
from home import views
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    # path('<str:name>/', views.Home.as_view(), name='home'),  # ar
    path('', views.Home.as_view()),
    path('question/delete/<int:pk>/', views.QuestionDeleteView.as_view()),
    path('question/update/<int:pk>/', views.QuestionUpdateView.as_view()),
    path('question/create/', views.QuestionCreateView.as_view()),
    path('questions/', views.QuestionListView.as_view()),
    path('accounts/', include('accounts.urls', namespace='accounts')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # path('schema/', get_schema_view(
    #     title="Your Project",
    #     description="API for all things …",
    #     version="1.0.0"
    # ), name='openapi-schema'),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]

# {
# 	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NTY2Mjk3MywiaWF0IjoxNjk1NTc2NTczLCJqdGkiOiJjYjUyNWQ0NTI4ZGY0NWJiYWZmZDhhODJjMDk1MzJmOSIsInVzZXJfaWQiOjF9.PLRr-QZUHSHiwlKsZMLS_Ns28RiDN0X4RO8DpbaWHFQ",
# 	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1NTc2ODczLCJpYXQiOjE2OTU1NzY1NzMsImp0aSI6IjljM2Q1YzAzMDZlMzQ1MzQ4N2JlNDczZTY2OGZjNGRhIiwidXNlcl9pZCI6MX0.wl5gO6tKnH2InJNDA9Ht7ucV1JRSgRaQzcCY0DU9F0o"
# }
