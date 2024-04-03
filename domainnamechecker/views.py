from django.shortcuts import render, redirect
from . forms import DomainSearchForm
from whois import whois
from difflib import get_close_matches
import re

# Create your views here.
def domain_search(request):
    form = DomainSearchForm(request.POST or None)
    whois_info = None
    suggestions = []
    domain_name=""
    expiration_dates_text=""
    name_servers = []
    result=None
    domain_suggestions=[]
    invalid_message=None
    suggestion_result=None

    if form.is_valid():
        domain_name= form.cleaned_data['domain_name']
        pattern = r'^[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(\.[a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$'


        domain_extentions = ['.com', '.net', '.org', '.io', '.ai', '.co']
        domain_parts = domain_name.split('.')
        base_domain = domain_parts[0]
        domain_suggestions = [base_domain + ext for ext in domain_extentions]


        if bool(re.match(pattern, domain_name)):
            try:
                whois_info = whois(domain_name)
                if whois_info is not None:
                     
                     result = ({
                          'isAvailable':False
                     })

                else:
                     result=({
                          'isAvailable':True
                     })
                expiration_dates = whois_info.expiration_date
                expiration_dates_text = [date.strftime("%Y-%m-%d %H:%M:%S") for date in expiration_dates]
                  
            except Exception as e:
                    if str(e).__contains__("No match for"):
                        result=({
                          'isAvailable':True
                     })
                    else:
                        result=({
                          'isAvailable':None
                     })

            available_domains=[domain_name]
            matches = get_close_matches(domain_name, available_domains)
            suggestions.append(matches)
            print(suggestions)
            print(result)
            print(domain_suggestions)
        else:
             
             invalid_message = "Please enter a valid domain name"

  
    context={
        'form' : form,
        'whois_info' : whois_info,
        'suggestions':suggestions,
        'domain_name':domain_name,
        'expiration_dates_text':expiration_dates_text,
        'result':result,
        'domain_suggestions':domain_suggestions,
        'invalid_message':invalid_message,
        
    }

    return render(request, 'domainnamechecker/domainsearch.html', context)
