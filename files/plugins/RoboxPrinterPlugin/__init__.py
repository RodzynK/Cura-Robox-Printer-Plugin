# Copyright (c) 2015 Ultimaker B.V.
# Cura is released under the terms of the LGPLv3 or higher.

from . import RoboxPrinterPlugin

from UM.i18n import i18nCatalog
catalog = i18nCatalog("cura")

def getMetaData():
    return {
        "mesh_writer": {
            "output": [{
                "extension": "rbcode",
                "description": catalog.i18nc("@item:inlistbox", "rbcode File"),
                "mime_type": "application/x-rbcode",
                "mode": RoboxPrinterPlugin.RoboxPrinterPlugin.OutputMode.BinaryMode
            }]
        }
    }

def register(app):
    plugin = RoboxPrinterPlugin.RoboxPrinterPlugin()
    return { "mesh_writer": plugin,
             "extension": plugin}
