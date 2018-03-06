"""PytSite Menu Plugin Models
"""
__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from plugins import taxonomy as _taxonomy, odm as _odm, widget as _widget, form as _form, odm_ui as _odm_ui


class Menu(_taxonomy.Term):
    """Menu Model
    """

    def _setup_fields(self):
        super()._setup_fields()

        self.remove_field('weight')
        self.define_field(_odm.field.Bool('enabled', default=True))
        self.define_field(_odm.field.String('icon'))

    @property
    def icon(self) -> str:
        return self.f_get('icon')

    @icon.setter
    def icon(self, value: str):
        self.f_set('icon', value)

    @property
    def enabled(self) -> bool:
        return self.f_get('enabled')

    @enabled.setter
    def enabled(self, value: bool):
        self.f_set('enabled', value)

    @classmethod
    def odm_ui_browser_widget_class(cls):
        return _widget.misc.TreeTable

    @classmethod
    def odm_ui_browser_setup(cls, browser: _odm_ui.Browser):
        super().odm_ui_browser_setup(browser)

        browser.insert_data_field('enabled', 'menu@enabled')

    def odm_ui_browser_row(self) -> dict:
        r = super().odm_ui_browser_row()

        if self.enabled:
            r['enabled'] = '<span class="label label-primary">{}</span>'.format(self.t('word_yes'))
        else:
            r['enabled'] = '<span class="label label-default">{}</span>'.format(self.t('word_no'))

        return r

    def odm_ui_m_form_setup_widgets(self, frm: _form.Form):
        super().odm_ui_m_form_setup_widgets(frm)

        if self.has_field('enabled'):
            frm.add_widget(_widget.select.Checkbox(
                uid='enabled',
                weight=5,
                label=self.t('enabled'),
                value=self.enabled,
            ))

        if self.has_field('icon'):
            frm.add_widget(_widget.input.Text(
                uid='icon',
                weight=25,
                label=self.t('icon'),
                value=self.icon,
            ))
