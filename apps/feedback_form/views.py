
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, CreateView, FormView

from django.shortcuts import render_to_response
from django.template import RequestContext

class CompletedPage(TemplateView):
    template_name = "feedback_form/feedback_done.html"

class ContactFormObject(object):
    """
    Form view that sends email when form is valid. You'll need
    to define your own form_class and template_name.
    """
    def form_valid(self, form):
        form.send_email(self.request)
        return super(ContactFormObject, self).form_valid(form)

    def get_success_url(self):		
        return reverse("feedback_form:completed")
        #return reverse("contact_form:contact")

	def get_context_data(self, **kwargs):
		context = super(ContactFormObject, self).get_context_data(**kwargs)
		context['messagez'] = "1111"
		return context
	# return messages in ciomtext requers
    #def render_to_response(self, context, **kwargs):
     #   return super(ContactFormObject, #self).render_to_response(RequestContext(self.request, context)) **kwargs)
	
class ContactFormView(ContactFormObject, FormView):
    pass

class ContactModelFormView(ContactFormObject, CreateView):
    pass
