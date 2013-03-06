from django.conf.urls.defaults import patterns
from todo.views import index, edit

urlpatterns = patterns('',
    (r'^$', index),
    (r'^edit/(?P<id>\d+)/$', edit),
    (r'^new/$', edit),
)
