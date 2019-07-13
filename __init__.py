"""PytSite Menu Plugin
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from . import _renderer as renderer, _widget as widget
from ._api import register_model, dispense, find
from ._model import Menu

# Locally needed imports
from semaver import Version as _Version


def plugin_load():
    from pytsite import reg
    from plugins import admin
    from . import _api

    admin.sidebar.add_section('menu', __name__ + '@menu')

    if reg.get('menu.register_default_model', True):
        _api.register_model('menu', _model.Menu, __name__ + '@menu')


def plugin_update(v_from: _Version):
    if v_from < '3.0':
        from plugins import odm
        odm.reindex()
