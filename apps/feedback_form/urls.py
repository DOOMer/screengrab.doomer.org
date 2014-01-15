
from django.conf.urls import patterns, include, url

from feedback_form import views, forms

urlpatterns = patterns('',
    url(r'^$', views.ContactFormView.as_view(
        template_name="feedback_form/feedback.html",
        form_class=forms.ContactForm,
    ), name="contact"),
	url(r'^$', views.ContactFormView.as_view(
        template_name="feedback_form/feedback.html",
        form_class=forms.ContactForm,
        
    ), name="completed"),
)