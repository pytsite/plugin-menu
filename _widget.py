"""PytSite Menu Plugin Widgets
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Union as _Union, Iterable as _Iterable
from pytsite import html as _html
from plugins import widget as _widget
from . import _api, _model, _renderer

_MenuEntities = _Union[str, _model.Menu, _Iterable[_model.Menu]]


class Menu(_widget.Abstract):
    def __init__(self, uid: str, menu_entities: _MenuEntities, renderer: _renderer.Abstract = None, **kwargs):
        super().__init__(uid, **kwargs)

        if isinstance(menu_entities, str):
            menu_entities = [_api.get(menu_entities)]
        elif isinstance(menu_entities, _model.Menu):
            menu_entities = menu_entities.children
        elif not isinstance(menu_entities, _Iterable):
            raise TypeError('{} expected, got {}'.format((str, _Iterable, _model.Menu), type(menu_entities)))

        self._has_messages = False

        self._entities = menu_entities
        self._renderer = renderer or _renderer.Bootstrap4()

    def _get_element(self, **kwargs) -> _html.Element:
        return self._renderer.render(self._entities)
