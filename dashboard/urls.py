from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('horizon-admin/', admin.site.urls),
    path('accounts/', include('account.urls', namespace='accounts')),
    path('', include('staticpages.urls', namespace="pages")),
    path('core/', include('core.urls', namespace="core")),
    path('chat/', include('chat.urls', namespace="chat")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
