"""Top-level package for NetBox ADC Plugin."""

__author__ = """Bob Longmore"""
__email__ = "bob.longmore@wwt.com"
__version__ = "0.1.0"


from extras.plugins import PluginConfig


class ADCConfig(PluginConfig):
    name = "netbox_adc_plugin"
    verbose_name = "NetBox ADC Plugin"
    description = "NetBox plugin for ADC."
    version = "version"
    base_url = "netbox_adc_plugin"


config = ADCConfig
