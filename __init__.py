"""PytSite Menu Plugin
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

# Public API
from ._api import dispense, find, get
from ._model import Menu


def plugin_load():
    from pytsite import lang
    from plugins import taxonomy
    from . import _model

    lang.register_package(__name__)
    taxonomy.register_model('menu', _model.Menu, __name__ + '@menu', menu_icon='fa fa-bars')


def plugin_load_wsgi():
    pass
