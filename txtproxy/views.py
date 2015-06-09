# coding=utf-8
# View to render landing-page

from flask import request, render_template, redirect, abort
from txtproxy import app

@app.route('/', methods=['GET', 'POST'])
def offerIndex():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        req = request.form.get('request')
        if req:
            return redirect('/tp/' + req, code=302)
        else:
            abort(400)
