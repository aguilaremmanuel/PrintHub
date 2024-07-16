from . import views
from django.urls import path

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path('about/',views.about_page, name='about_page'),                     # About
    path('pricing/',views.pricing_page, name='pricing_page'),               # Pricing
    path('contact/',views.contact_page, name='contact_page'),               # Contact
    path('faqs/',views.faqs_page, name='faqs_page'),                        # FAQs
]