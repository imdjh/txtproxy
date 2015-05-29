#!/usr/bin/env python
# coding=utf-8
# Domainname redirect according it's TXT record
# version 0.1.0
# Author: dye Jarhoo

from flask import Flask, render_template, send_from_directory, abort
import dnsq

# Fireup our little app ;)
app = Flask(__name__)


def checkdn(str):
    """return True if str is valid domain"""
    str = str.strip()
    if not str:
        return False
    if str[0] == '.':
        return False
    if str[-1] == '.':
        if not checkdn(str[:-1]):
            return False
    if len(str.split('.')) <= 1:
        return False
    return True


@app.route('/tp/<req>')
def textproxy(req):
    """Input url, return redirect html"""
    if checkdn(req):
        # since req is valid, format to TXT record standard
        record = req.strip().strip('.') + '.'
        arrayQry = dnsq.query_dns(record, 'TXT')
        if arrayQry:
            return render_template('redirect.html', url=arrayQry[0])
        else:
            # domain name is correct, but no TXT record found return 404 err
            abort(404)
    # the request domain name is error
    abort(400)


@app.route('/favicon.ico')
def offerFavicon():
    """Offer Favicon file"""
    return send_from_directory('static', 'favicon.ico')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
