from django.conf.urls.defaults import patterns
from todo.views import index

urlpatterns = patterns('',
    (r'^$', index),
)
