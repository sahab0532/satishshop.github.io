from django.urls import path
from customers import views

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin route
    path('customers/', include("customers.urls")),  # Django customers route
    # ...
]

# to support and show media & static files in developer mode
if settings.DEVEL:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)