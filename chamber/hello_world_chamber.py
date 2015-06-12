# Copyright (C) 2015 Mach 30 - http://www.mach30.org
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# IMPORTANT: You must install FreeCAD and the CadQuery module for FreeCAD to
# run this script. https://github.com/jmwright/cadquery-freecad-module

import math
from pint import UnitRegistry
import pressure_vessel_calcs
import cadquery as cq
from Helpers import show

# Units used
# units.meter
# units.pascal
# Use this everywhere for Pint integration from now on
units = UnitRegistry()

# Declare before using pressure vessel calculation library
ri = 20.0e-3 * units.meter

pv = pressure_vessel_calcs.PressureVessel(ri,
                                          2e-3 * units.meter,
                                          3.5e6 * units.pascal,
                                          101325 * units.pascal,
                                          40e6 * units.pascal,
                                          2.0,
                                          0.0001 * units.meter)
t = pv.calculate_wall_thickness()

theta = 45 * units.degree  # The chamber taper angle in degrees
total_length = 50.0e-3 * units.meter  # The full length of the chamber exterior
converg_sect_length = total_length * 0.35  # Converging section length

# Where our taper starts at the business end of the chamber
theta_start = total_length - converg_sect_length

theta_end_point = converg_sect_length * math.tan(theta.to(units.radian))

# Set up some of our re-usable dimensions
dtheta = theta_start + converg_sect_length

# Temp math to get our chamber outline points
pointX = dtheta - math.cos(theta.to(units.radian)) * \
    math.tan(theta.to(units.radian)) * t
pointY = theta_end_point - math.sin(theta.to(units.radian)) * \
    math.tan(theta.to(units.radian)) * t
pointY2 = (theta_end_point - t / math.cos(theta.to(units.radian)))
diffX = pointX - theta_start
diffY = pointY - 0

chamber_points = [
    (0, 0),
    (theta_start.to(units.millimeter).magnitude, 0),
    (dtheta.to(units.millimeter).magnitude, theta_end_point.to(units.millimeter).magnitude),
    (dtheta.to(units.millimeter).magnitude, pointY2.to(units.millimeter).magnitude),
    ((dtheta - diffX).to(units.millimeter).magnitude, (pointY2 - diffY).to(units.millimeter).magnitude),
    (theta_start.to(units.millimeter).magnitude, -t.to(units.millimeter).magnitude),
    (0, -t.to(units.millimeter).magnitude),
    (0, 0)
    ]

outline = cq.Workplane('XY').polyline(chamber_points)

chamber = outline.revolve(360.0, (0, ri.to(units.millimeter).magnitude, 0),
                          (1, ri.to(units.millimeter).magnitude, 0))

# Show the outline and/or shell
# show(outline, (204, 204, 204, 0.0))
show(chamber, (204, 204, 204, 0.0))
