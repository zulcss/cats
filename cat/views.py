from collections import OrderedDict

from flask import jsonify

from cat import app
from cat.model import MeowCat

from cat.utils import fetch_kitty

@app.route('/cat')
def index():
    return jsonify(fetch_kitty())

@app.route('/history')
def history():
    data = MeowCat.query.all()
    data = [OrderedDict(id=r.cid, url=r.url, source_url=r.src_url) 
            for r in data]
    return jsonify({'images': data})
