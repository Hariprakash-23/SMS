from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from api.views import dashboard_api

def redirect_to_login(request):
    return redirect('login')  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/',redirect_to_login,name='root'),
    path('api/v1/list/', include('api.urls')),
    path('accounts/', include('accounts.urls')),
    path('students/', include('students.urls')),
    path('courses/', include('courses.urls')),
    path('attendance/', include('attendance.urls')),
    path('marks/', include('marks.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/dashboard/', dashboard_api),
]