from django.urls import path
from user.views import UserTokenLogin, UserSignUp, UserTokenRefresh
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
schema_view = get_schema_view(
    openapi.Info(
        title="Authentication API",
        default_version='v1',
        description="API documentation for authentication service",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="meysamkheyrollahnejad@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('signup/', view= UserSignUp.as_view(),name='user_signup'),
    path('login/', view= UserTokenLogin.as_view(),name='user_login'),
    path('refresh/', view= UserTokenRefresh.as_view(),name='user_refresh'),


]
