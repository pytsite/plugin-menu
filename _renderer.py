"""PytSite Menu Plugin Renderers
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from typing import Optional as _Optional, Union as _Union, Iterable as _Iterable
from abc import ABC as _ABC, abstractmethod as _abstractmethod
from pytsite import html as _html, router as _router
from . import _api, _model


class Abstract(_ABC):
    @_abstractmethod
    def render(self, entities: _Iterable[_Union[str, _model.Menu]]) -> _html.Element:
        pass


class Bootstrap4(Abstract):
    @staticmethod
    def _item_url(entity: _model.Menu) -> str:
        return _router.url(entity.path)

    def _is_item_active(self, entity: _model.Menu):
        return self._item_url(entity) == _router.current_url(True)

    def _render_item(self, entity: _model.Menu) -> _Optional[_html.Li]:
        if not entity.enabled:
            return

        root = _html.Li(css='nav-item {}'.format('active' if self._is_item_active(entity) else ''))
        a = root.append(_html.A(entity.title, href=self._item_url(entity), css='nav-link'))

        if entity.new_window:
            a.set_attr('target', '_blank')

        return root

    def _render_dropdown(self, entity: _model.Menu) -> _Optional[_html.Li]:
        if not entity.enabled:
            return

        # Dropdown's root
        root = _html.Li(css='nav-item dropdown')

        # Toggler
        root.append(_html.A(entity.title, uid=entity.ref, href='#', css='nav-link dropdown-toggle', role='button',
                            data_toggle='dropdown', aria_haspopup='true', aria_expanded='false'))

        # Dropdown
        dropdown = root.append(_html.Div(css='dropdown-menu', aria_labelledby=entity.ref))
        for e in entity.children:  # type: _model.Menu
            if e.enabled:
                a_css = 'dropdown-item {}'.format('active' if self._is_item_active(e) else '')
                a = dropdown.append(_html.A(e.title, href=self._item_url(e), css=a_css))

                if e.new_window:
                    a.set_attr('target', '_blank')

        return root

    def render(self, entities: _Iterable[_Union[str, _model.Menu]]) -> _html.Element:
        # Currently Bootstrap does not support sub-dropdowns, so we too. While.
        # https://github.com/twbs/bootstrap/issues/21026

        root = _html.Ul(css='navbar-nav mr-auto')

        for e in entities:  # type: _model.Menu
            if isinstance(e, str):
                e = _api.get(e)
            child = self._render_dropdown(e) if e.has_children else self._render_item(e)
            if child:
                root.append(child)

        return root
