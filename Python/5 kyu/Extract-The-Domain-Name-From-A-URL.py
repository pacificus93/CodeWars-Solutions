# -*- coding: utf-8 -*-
"""
DESCRIPTION:
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"
"""

def domain_name(url):
    http_protocols = ['http','https']
    
    #remove http protocol part
    
    url = url.split('//')[len(url.split('//'))-1]
    
    #get fqdn
    
    url = url.split('/')[0]
    
    return url.split('.')[1] if 'www' in url.split('.') else url.split('.')[0]