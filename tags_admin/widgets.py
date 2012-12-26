from django import forms
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.safestring import mark_safe

from utils import edit_string_for_tags


class TagAutocomplete(forms.TextInput):
	input_type = 'text'
	
	def render(self, name, value, attrs=None):
		list_view = reverse('tags_admin-list')
		if value is not None and not isinstance(value, basestring):
			value = edit_string_for_tags([o.tag for o in value.select_related("tag")])
		html = super(TagAutocomplete, self).render(name, value, attrs)
		js =  u'<script type="text/javascript">'
		js += u'jQuery().ready(function() {'
		js += u'	jQuery("#%s").tagsInput({ autocomplete_url: "%s" });' % (attrs['id'], list_view)
		js += u'});'
		js += u'</script>' 
		return mark_safe("\n".join([html, js]))

	class Media:
		js = (
			"%sjs/jquery/jquery.tagsinput.js" % settings.STATIC_URL,
		)
		css = {
			'all': ( "%scss/jquery.tagsinput.css" % settings.STATIC_URL, )
		}

