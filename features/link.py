from urlparse import urlparse
import re
import urllib2
import urllib
import json
from xml.dom import minidom
import requests
from urlparse import urlparse
from urlparse import urlsplit
import seolib as seo

nf=-1
def sitepopularity(url):
    alexa_rank = seo.get_alexa(url)
    if alexa_rank==None:
        return alexa_rank
    else:
        return 100000000

def pagespeed_rank(url):
    #The input url must end with a / character.
    r=urllib2.urlopen('https://www.googleapis.com/pagespeedonline/v2/runPagespeed?url='+url+ '&filter_third_party_resources=true&locale=en_US&screenshot=false&strategy=desktop&key=AIzaSyDa2L0i-oPVgsry9HlW5R7BLpDTL9b0Oz8')
    data=json.load(r)
    return data['ruleGroups']["SPEED"]["score"]
def time(url):
    requests.get(url).elapsed.total_seconds()
