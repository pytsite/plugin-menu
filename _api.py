"""PytSite Menu Plugin API Functions
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from plugins import taxonomy as _taxonomy, odm as _odm
from . import _model


def create(title: str, alias: str = None, icon: str = None, order: int = None, language: str = None) -> _model.Menu:
    """Create a new menu
    """
    menu = _taxonomy.create('menu', title, alias, language)  # type: _model.Menu
    menu.order = order
    menu.icon = icon

    return menu


def find(language: str = None) -> _odm.Finder:
    """Get a menu finder
    """
    return _taxonomy.find('menu', language)


def get(alias: str, language: str = None):
    """Get a menu
    """
    return _taxonomy.find_by_alias('menu', alias, language)
