from cat import db

class MeowCat(db.Model):
    """ DB model to store the results from the cat api call."""
    key = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(50))
    cid = db.Column(db.Integer)
    src_url = db.Column(db.String(50))
    
    def __init__(self, url, cid, src_url):
        self.url = url
        self.cid = cid
        self.src_url = src_url
