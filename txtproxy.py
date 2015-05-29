#!/usr/bin/env python
# coding=utf-8
# Domainname redirect according it's TXT record
# version 0.0.1
# Author: dye Jarhoo

from flask import Flask, render_template, send_from_directory, abort
import dnsq

# Fireup our little app ;)
app = Flask(__name__)


def checkdn(str):
    """return True if str is a domain"""

    if str[-1] == '.':
        str = str[:-1]
    if len(str.split('.')) > 1:
        return True


@app.route('/tp/<req>')
def textproxy(req):
    """Input url, return redirect html"""
    if checkdn(req):
        arrayQry = dnsq.query_dns(req, 'TXT')
        if arrayQry:
            return render_template('redirect.html', url=arrayQry[0])

    return abort(400)


@app.route('/favicon.ico')
def offerFavicon():
    """Offer Favicon file"""
    return send_from_directory('static', 'favicon.ico')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
