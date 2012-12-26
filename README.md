django-tags-admin
=================

Support for Tags in DJango Admin with Autocomplete and tags-input jquery plugin

REQUIREMENTS 
==================

jQuery and django-taggit is required 

INSTALLATION 
==================

add tags_admin to your apps or python path 

SETUP
==================

1) add 'tags_admin' to INSTALLED_APPS 
2) in models use 
from tags_admin.managers import TaggableManager

and in some class definition 

class SomeModel(models.Model)
  tag = TaggableManager()

3) in urls.py add 
    url(r'^tags_admin/', include('tags_admin.urls')),
