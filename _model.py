"""PytSite Menu Plugin Models
"""
__author__ = 'Oleksandr Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'

from plugins import taxonomy as _taxonomy, odm as _odm, widget as _widget, form as _form, odm_ui as _odm_ui


class Menu(_taxonomy.Term):
    """Menu Model
    """

    def _setup_fields(self):
        super()._setup_fields()

        self.remove_field('weight')
        self.remove_field('image')
        self.define_field(_odm.field.Bool('enabled', default=True))
        self.define_field(_odm.field.Bool('new_window'))
        self.define_field(_odm.field.String('path', required=True, max_length=512, default='#'))
        self.define_field(_odm.field.String('icon'))

    @property
    def enabled(self) -> bool:
        return self.f_get('enabled')

    @enabled.setter
    def enabled(self, value: bool):
        self.f_set('enabled', value)

    @property
    def new_window(self) -> bool:
        return self.f_get('new_window')

    @new_window.setter
    def new_window(self, value: bool):
        self.f_set('new_window', value)

    @property
    def path(self) -> str:
        return self.f_get('path')

    @path.setter
    def path(self, value: str):
        self.f_set('path', value)

    @property
    def icon(self) -> str:
        return self.f_get('icon')

    @icon.setter
    def icon(self, value: str):
        self.f_set('icon', value)

    @classmethod
    def odm_ui_browser_widget_class(cls):
        return _widget.misc.TreeTable

    def odm_ui_browser_setup(self, browser: _odm_ui.Browser):
        super().odm_ui_browser_setup(browser)

        browser.insert_data_field('path', 'menu@path')
        browser.insert_data_field('enabled', 'menu@enabled')

    def odm_ui_browser_row(self) -> dict:
        r = super().odm_ui_browser_row()

        r['path'] = self.path

        if self.enabled:
            r['enabled'] = '<span class="label label-primary">{}</span>'.format(self.t('word_yes'))
        else:
            r['enabled'] = '<span class="label label-default">{}</span>'.format(self.t('word_no'))

        return r

    def odm_ui_m_form_setup_widgets(self, frm: _form.Form):
        super().odm_ui_m_form_setup_widgets(frm)

        if frm.has_widget('order'):
            frm.remove_widget('order')

        if self.has_field('enabled'):
            frm.add_widget(_widget.select.Checkbox(
                uid='enabled',
                weight=10,
                label=self.t('enabled'),
                value=self.enabled,
            ))

        if self.has_field('new_window'):
            frm.add_widget(_widget.select.Checkbox(
                uid='new_window',
                weight=20,
                label=self.t('new_window'),
                value=self.new_window,
            ))

        if self.has_field('path'):
            frm.add_widget(_widget.input.Text(
                uid='path',
                weight=210,
                label=self.t('path'),
                required=self.get_field('path').required,
                value=self.path,
            ))

        if self.has_field('icon'):
            frm.add_widget(_widget.input.Text(
                uid='icon',
                weight=310,
                label=self.t('icon'),
                required=self.get_field('icon').required,
                value=self.icon,
            ))
