"""PytSite Menu Plugin API Functions
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from plugins import taxonomy as _taxonomy, odm as _odm
from . import _model


def dispense(title: str, alias: str = None, icon: str = None, order: int = None, language: str = None,
             parent: _model.Menu = None) -> _model.Menu:
    """Dispense a new menu item or raise exception if term with specified alias already exists
    """
    menu = _taxonomy.dispense('menu', title, alias, language, parent)  # type: _model.Menu
    menu.order = order
    menu.icon = icon

    return menu


def find(language: str = None) -> _odm.Finder:
    """Get a menu items finder
    """
    return _taxonomy.find('menu', language)


def get(alias: str, language: str = None):
    """Get a menu item
    """
    return _taxonomy.get('menu', alias, language)
