# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SDSSplugin
                                 A QGIS plugin
 This is the plugin for the SDSS course
                             -------------------
        begin                : 2016-11-23
        copyright            : (C) 2016 by AA
        email                : aa@hotmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load SDSSplugin class from file SDSSplugin.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .SDSS_plugin import SDSSplugin
    return SDSSplugin(iface)
