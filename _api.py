"""PytSite Menu Plugin API Functions
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Union
from pytsite import util
from plugins import taxonomy, odm
from . import _model


def register_model(model: str, cls, admin_menu_title: str = None, admin_menu_weight: int = 0,
                   admin_menu_icon: str = 'fa fas fa-bars', admin_menu_sid: str = 'menu',
                   admin_menu_roles: Union[str, list, tuple] = ('admin', 'dev'),
                   admin_menu_permissions: Union[str, list, tuple] = None):
    """Register a menu ODM model
    """
    if isinstance(cls, str):
        cls = util.get_module_attr(cls)

    if not issubclass(cls, _model.Menu):
        raise TypeError('Subclass of {} expected'.format(_model.Menu))

    taxonomy.register_model(model, cls, admin_menu_title, admin_menu_weight, admin_menu_icon, admin_menu_sid,
                            admin_menu_roles, admin_menu_permissions)


def dispense(title: str, icon: str = None, order: int = None, enabled: bool = True, language: str = None,
             parent: _model.Menu = None, model: str = 'menu') -> _model.Menu:
    """Dispense a new menu item
    """
    entity = taxonomy.dispense(model, title, None, language, parent)  # type: _model.Menu
    entity.enabled = enabled
    entity.order = order
    entity.icon = icon

    return entity


def find(model: str, language: str = None) -> odm.SingleModelFinder:
    """Get a menu items finder
    """
    return taxonomy.find(model, language)
