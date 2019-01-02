"""PytSite Menu Plugin Widgets
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Union as _Union
from pytsite import html as _html
from plugins import widget as _widget
from . import _api, _model, _renderer


class Menu(_widget.Abstract):
    def __init__(self, uid: str, menu_entity: _Union[str, _model.Menu], renderer: _renderer.Abstract = None, **kwargs):
        super().__init__(uid, **kwargs)

        if isinstance(menu_entity, str):
            menu_entity = _api.get(menu_entity)

        if not menu_entity:
            raise ValueError('menu_entity cannot be empty')

        self._has_messages = False

        self._entity = menu_entity
        self._renderer = renderer or _renderer.Bootstrap4()

    def _get_element(self, **kwargs) -> _html.Element:
        return self._renderer.render(self._entity)
