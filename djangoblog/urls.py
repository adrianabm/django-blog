from django.conf.urls import url
from django.contrib import admin

from posts.views import HomeView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView, name='home')
]
