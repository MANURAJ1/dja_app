from django.conf.urls import include, url
from django.contrib import admin


admin.site.site_header='EAG Site'
admin.site.site_title="EAG Portal1"
admin.site.index_title='Welcome To EAG Site'

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
