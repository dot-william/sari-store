from django.urls import path
from . import views
from sarisaristoreapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index, name='index'),
    path('upload/', views.upload, name='upload-product'),
    path('update/<int:prod_id>', views.update_product),
    path('delete/<int:prod_id>', views.delete_product),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)