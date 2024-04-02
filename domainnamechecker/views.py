from django.shortcuts import render
from . forms import DomainSearchForm
from whois import whois
from difflib import get_close_matches

# Create your views here.
def domain_search(request):
    form = DomainSearchForm(request.POST or None)
    whois_info = None
    suggestions = []
    domain_name=""
    expiration_dates_text=""
    name_servers = []
    

    if form.is_valid():
        domain_name= form.cleaned_data['domain_name']

        try:
            whois_info = whois(domain_name)
            expiration_dates = whois_info.expiration_date
            expiration_dates_text = [date.strftime("%Y-%m-%d %H:%M:%S") for date in expiration_dates]
            for name_server in whois_info.name_servers:
                 name_servers.append(name_server)

                
        except Exception as e:
                pass

        available_domains=[domain_name]
        matches = get_close_matches(domain_name, available_domains)
        suggestions.append(matches)
        print(suggestions)
    
    context={
        'form' : form,
        'whois_info' : whois_info,
        'suggestions':suggestions,
        'domain_name':domain_name,
        'expiration_dates_text':expiration_dates_text,
        'name_servers':name_servers,
    }

    return render(request, 'domainnamechecker/domainsearch.html', context)
