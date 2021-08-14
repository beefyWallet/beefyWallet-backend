"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('beefy_wallet_api/api-auth/', include('rest_framework.urls')),
    path('beefy_wallet_api/rest-auth/', include('rest_auth.urls')),
    path('beefy_wallet_api/rest-auth/registration/', include('rest_auth.registration.urls')),
    path('beefy_wallet_api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('beefy_wallet_api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('beefy_wallet_api/', include('beefy_wallet_api.api.urls')),
]
