from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.index , name="home"),
    path('signup/',views.signup,name="signup"),
    path('accounts/',include('django.contrib.auth.urls')),
    path('upload/',views.uploads,name="uploads")
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
