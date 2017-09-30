from collections import OrderedDict
import urllib2

import bs4

from cat import db
from cat.model import MeowCat
from cat import URL

def fetch_kitty():
    cat_data = urllib2.urlopen(URL)
    cat_response = cat_data.read()

    # Pare the XML that has been returned by the cat api
    xml = bs4.BeautifulSoup(cat_response, 'xml')
    url = xml.find_all('url')[0].get_text()
    id_ = xml.find_all('id')[0].get_text()
    source_url = xml.find_all('source_url')[0].get_text()

    db.create_all()
    cat = MeowCat(url, id_, source_url)
    db.session.add(cat)
    db.session.commit()

    data = OrderedDict(
                id=id_, url=url, source_url=source_url)
    return {'image': data}
