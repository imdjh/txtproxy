#!/usr/bin/env python
# coding=utf-8
# Domainname redirect according it's TXT record
# version 0.1.0
# Author: dye Jarhoo

from flask import Flask, send_from_directory

# Fireup our little app ;)
app = Flask(__name__)

import txtproxy.views
import txtproxy.models


@app.route('/favicon.ico')
def offerFavicon():
    """Offer Favicon file"""
    return send_from_directory('static', 'favicon.ico')
