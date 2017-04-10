from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from posts.views import HomeView, PostDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', HomeView, name='home'),
    url(r'^posts/(?P<post_id>[0-9]+)/$', PostDetailView, name='post_detail')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
