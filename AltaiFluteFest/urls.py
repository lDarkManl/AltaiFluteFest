from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
]

urlpatterns += i18n_patterns(
    path('', include(('main.urls'), namespace='main')),
    path('application/', include(('application.urls'), namespace='application')),
    path('account/', include(('account.urls'), namespace='account')),
    path('gallery/', include(('gallery.urls'), namespace='gallery')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
