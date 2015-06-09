# coding=utf-8
# Model to accept requests

from txtproxy import app
from flask import render_template, abort
import dnsq


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
