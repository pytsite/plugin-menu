"""PytSite Menu Plugin Models
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from plugins import taxonomy as _taxonomy, odm as _odm, widget as _widget, form as _form


class Menu(_taxonomy.Term):
    """Menu Model
    """

    def _setup_fields(self):
        super()._setup_fields()

        self.remove_field('weight')
        self.define_field(_odm.field.String('icon'))

    @property
    def icon(self) -> str:
        return self.f_get('icon')

    @icon.setter
    def icon(self, value: str):
        self.f_set('icon', value)

    @classmethod
    def odm_ui_browser_widget_class(cls):
        return _widget.misc.TreeTable

    def odm_ui_m_form_setup_widgets(self, frm: _form.Form):
        super().odm_ui_m_form_setup_widgets(frm)

        if self.has_field('icon'):
            frm.add_widget(_widget.input.Text(
                uid='icon',
                weight=25,
                label=self.t('icon'),
                value=self.icon,
            ))
