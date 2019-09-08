from requests_html import HTMLSession
from urllib.parse import urlparse, parse_qs
import time

# initial conditions
lat = 51.6498
lon = 0.0982
token = 'gAAAAABdcygtAxwDaKiuDbdfzbzaYYZBzQtDHFQd3F7hLQIVjqakI8mD23L8wEqBj0fI8FtrAVYomK25YwFPcsn4wRWRYNecBdbGefh-GOAHGoRuNYywGxlLInMwUSdatM2w9LHbgMMQ'
url = 'https://drivetothetarget.web.ctfcompetition.com'
inc = 0.0001

session = HTMLSession()
search = True

lat_done = False
lon_done = False

nlat = lat - inc
nlon = lon

while(search):
    time.sleep(0.5)
    query = {'lat': "{0:.4f}".format(nlat), 'lon': "{0:.4f}".format(nlon), 'token': token}

    r = session.get(url,params=query) #builds url

    response = urlparse(r.url)
    response_query = parse_qs(response.query)

    token = r.html.find('input')[2].attrs['value']
    # print (token)

    text = r.html.find('p')[1].text
    print (text)

    if text.endswith('this is too fast!'):
        time.sleep(1)

    if text.endswith('You are getting away…'):
        if not lon_done:
            nlon += inc
            lon_done = True
        elif not lat_done:
            nlat += inc
            lat_done = True
        elif lon_done and lat_done:
            print(query)
            exit()


    if lat_done:
        nlon -= inc
    else:
        nlat -= inc
