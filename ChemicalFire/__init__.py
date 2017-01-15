# -*- coding: utf-8 -*-
"""
/***************************************************************************
 ChemicalFire
                                 A QGIS plugin
 Helps making desicions when a chemical fire appears
                             -------------------
        begin                : 2017-01-09
        copyright            : (C) 2017 by Tu Delft
        email                : e.m.j.stierman@student.tudelft.nl
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
    """Load ChemicalFire class from file ChemicalFire.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .chemical_fire import ChemicalFire
    return ChemicalFire(iface)
