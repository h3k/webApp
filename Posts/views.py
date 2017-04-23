from django.conf import settings
from django.views import generic
from django.shortcuts import render
from django.core.mail import send_mail
from django.views.generic import View
from .forms import ContactForm
from .models import News
# Create your views here.


class home(View):
    def get(self, request, *args, **kwargs):
        title = "Welcome summoner"
        context = {
            "title": title,
        }

        return render(request, "home.html", context)


class about(View):
    def get(self, request, *args, **kwargs):
        return render(request, "about.html", {})


class NewsView(generic.ListView):
    template_name = 'news_list.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.all().order_by('-timestamp')

class NewsDetailView(generic.DeleteView):
    model = News
    template_name = 'news_detail.html'
    context_object_name = 'news'


def contact(request):
        title = "Contact Us"
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form_name = form.cleaned_data.get("full_name")
            form_email = form.cleaned_data.get("email")
            form_message = form.cleaned_data.get("message")
            subject = "Site contact form"
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email]
            contact_message = "%s: %s via %s"%(form_name, form_message, form_email)

            send_mail(subject, contact_message, form_email, to_email, fail_silently=False)

        context = {
            "form": form,
            "title": title
        }

        return render(request, "contact.html", context)


