from django.shortcuts import render

def main_page(request):
    return render(request, "main-page.html")

def faqs_page (request):
    return render(request, 'faqs.html')

def contact_page (request):
    return render(request, 'contact.html')

def pricing_page (request):
    return render(request, 'pricing.html')

def about_page (request):
    return render(request, 'about.html')