"""PytSite Menu Plugin Renderers
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

import htmler
from typing import Optional, Union, Iterable
from abc import ABC, abstractmethod
from pytsite import router
from . import _model


class Abstract(ABC):
    @abstractmethod
    def render(self, entities: Iterable[_model.Menu]) -> htmler.Element:
        pass


class Bootstrap4(Abstract):
    @staticmethod
    def _item_url(entity: _model.Menu) -> str:
        return router.url(entity.path)

    def _is_item_active(self, entity: _model.Menu):
        return self._item_url(entity) == router.current_url(True)

    def _render_item(self, entity: _model.Menu) -> Optional[htmler.Li]:
        if not entity.enabled:
            return

        root = htmler.Li(css='nav-item {}'.format('active' if self._is_item_active(entity) else ''))
        a = root.append_child(htmler.A(entity.title, href=self._item_url(entity), css='nav-link'))

        if entity.new_window:
            a.set_attr('target', '_blank')

        return root

    def _render_dropdown(self, entity: _model.Menu) -> Optional[htmler.Li]:
        if not entity.enabled:
            return

        # Dropdown's root
        root = htmler.Li(css='nav-item dropdown')

        # Toggler
        root.append_child(htmler.A(entity.title, id=entity.ref, href='#', css='nav-link dropdown-toggle', role='button',
                                   data_toggle='dropdown', aria_haspopup='true', aria_expanded='false'))

        # Dropdown
        dropdown = root.append_child(htmler.Div(css='dropdown-menu', aria_labelledby=entity.ref))
        for e in entity.children:  # type: _model.Menu
            if e.enabled:
                a_css = 'dropdown-item {}'.format('active' if self._is_item_active(e) else '')
                a = dropdown.append_child(htmler.A(e.title, href=self._item_url(e), css=a_css))

                if e.new_window:
                    a.set_attr('target', '_blank')

        return root

    def render(self, entities: Iterable[Union[str, _model.Menu]]) -> htmler.Element:
        # Currently Bootstrap does not support sub-dropdowns, so we too. While.
        # https://github.com/twbs/bootstrap/issues/21026

        root = htmler.TagLessElement()

        for e in entities:  # type: _model.Menu
            child = self._render_dropdown(e) if e.has_children else self._render_item(e)
            if child:
                root.append_child(child)

        return root
