"""PytSite Menu Plugin Widgets
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import htmler
from typing import Iterable as _Iterable
from plugins import widget as _widget
from . import _model, _renderer


class Menu(_widget.Abstract):
    def __init__(self, uid: str, menu_entities: _Iterable[_model.Menu], renderer: _renderer.Abstract = None, **kwargs):
        super().__init__(uid, **kwargs)

        self._wrap_em = htmler.Ul()
        self._form_group = False
        self._has_messages = False
        self._entities = menu_entities
        self._renderer = renderer or _renderer.Bootstrap4()

    def _get_element(self, **kwargs) -> htmler.Element:
        return self._renderer.render(self._entities)
