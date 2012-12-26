from django.conf.urls.defaults import *

urlpatterns = patterns('tags_admin.views',
    url(r'^list$', 'list_tags', name='tags_admin-list'),
)
