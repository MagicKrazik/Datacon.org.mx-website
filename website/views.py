from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import QuoteRequest
from .forms import QuoteRequestForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import ContactMessage, QuoteRequest
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout
from django.views.decorators.http import require_http_methods




# Create your views here.

def home(request):
    return render(request, 'home.html')

def services(request):
    return render(request, 'services.html')

def our_process(request):
    return render(request, 'our_process.html')

def client_success_stories(request):
    return render(request, 'client_success_stories.html')

def about_us(request):
    return render(request, 'about_us.html')

def contact(request):
    return render(request, 'contact.html')

def request_quote(request):
    return render(request, 'request_quote.html')

def faq(request):
    return render(request, 'faq.html')

def insights(request):
    return render(request, 'insights.html')

def solution_comparison(request):
    return render(request, 'solution_comparison.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your message! We will get back to you shortly.')
            return redirect('contact')
        else:
            messages.error(request, 'There was an error with your submission. Please check the form and try again.')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


class QuoteRequestView(CreateView):
    model = QuoteRequest
    form_class = QuoteRequestForm
    template_name = 'request_quote.html'
    success_url = reverse_lazy('request_quote')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your quote request has been successfully submitted. We'll be in touch with you soon!")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "There was an error processing your quote request. Please review your information and try again.")
        return super().form_invalid(form)    
    

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to contact submissions after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@require_http_methods(["GET", "POST"])
def logout_view(request):
    logout(request)
    messages.success(request, "You have been successfully logged out.")
    return redirect('home')

@login_required
def contact_submissions(request):
    contacts_list = ContactMessage.objects.all().order_by('-created_at')
    paginator = Paginator(contacts_list, 10)  # Show 10 contacts per page
    page_number = request.GET.get('page')
    contacts = paginator.get_page(page_number)
    return render(request, 'contact_submissions.html', {'contacts': contacts})

@login_required
def quote_requests(request):
    quotes_list = QuoteRequest.objects.all().order_by('-created_at')
    paginator = Paginator(quotes_list, 10)  # Show 10 quote requests per page
    page_number = request.GET.get('page')
    quotes = paginator.get_page(page_number)
    return render(request, 'quote_requests.html', {'quotes': quotes})