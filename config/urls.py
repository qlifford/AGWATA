from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kwach/shop', include('shop.urls')),
    path('kwach/money/', include('moneypath.urls')),
    path('kwach/photos/', include('snapy.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
