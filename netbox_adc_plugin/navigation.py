from extras.plugins import PluginMenuButton, PluginMenuItem
from utilities.choices import ButtonColorChoices

plugin_buttons = [
    PluginMenuButton(
        link="plugins:netbox_adc_plugin:adc_add",
        title="Add",
        icon_class="mdi mdi-plus-thick",
        color=ButtonColorChoices.GREEN,
    )
]

menu_items = (PluginMenuItem(link="plugins:netbox_adc_plugin:adc_list", link_text="ADC", buttons=plugin_buttons),)
