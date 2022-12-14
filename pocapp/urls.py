
from django.urls import path, include
from pocapp import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('customer_api', views.CustomerCRUDCBV)
router.register('product_api', views.ProductCRUDCBV)
router.register('order_api', views.OrderCRUDCBV)
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.home),
    path('generate/', views.generate),
    path('clone/', views.clone),
    path('customer/', views.dev_customer),
     path('unmask/', views.unmask),
    path('unmask_customer/', views.dev_unmask_customer),
    path('', include(router.urls)),
]