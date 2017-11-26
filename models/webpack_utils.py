#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from os.path import join
from gluon.globals import current
from gluon.html import URL

def load_json(f):
    # passthru dict
    if isinstance(f, dict):
        return f
    try:
        # load from file like object
        string = f.read()
    except AttributeError:
        # load from filename
        with open(f) as fp:
            string = fp.read()
    return json.loads(string)


def WEBPACK(js_file, public_root='dist', manifest_file='static/dist/webpack-manifest.json', application_folder = None):

    """
        Returns actual url for the transpiled javascript, according to webpack log
    """
    if not application_folder:
        try:
            application_folder = current.request.folder
        except AttributeError:
            raise SyntaxError('Not enough information to find manifest file %s' % manifest_file)

    manifest = load_json(join(application_folder, manifest_file))
    try:
        file_key = join(public_root, manifest[js_file]).encode("utf-8")
    except KeyError:
        raise SyntaxError('Requested %s file has not been created by webpack' % js_file)

    return URL('static', file_key)
