from django.urls import path
from . import views
from .views import QuoteRequestView

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('our-process/', views.our_process, name='our_process'),
    path('client-success-stories/', views.client_success_stories, name='client_success_stories'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('request-quote/', QuoteRequestView.as_view(), name='request_quote'),
    path('faq/', views.faq, name='faq'),
    path('solution-comparison/', views.solution_comparison, name='solution_comparison'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('contact-submissions/', views.contact_submissions, name='contact_submissions'),
    path('quote-requests/', views.quote_requests, name='quote_requests'),
]

