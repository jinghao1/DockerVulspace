
from django.urls import path, include
from drf_spectacular.views import SpectacularJSONAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [

    path("demo/", include('demo.urls')),
    # api 文档地址
    path('demo/XZPcGFKoxYXScwGjQtJx8u/schema/',
         SpectacularJSONAPIView.as_view(),
         name='schema'),
    path('demo/XZPcGFKoxYXScwGjQtJx8u/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path('demo/XZPcGFKoxYXScwGjQtJx8u/schema/redoc/',
         SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),

]


