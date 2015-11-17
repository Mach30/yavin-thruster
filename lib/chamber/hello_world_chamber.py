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
from lib.pint_ext import PintExtUnitRegistry
import pressure_vessel_calcs
import cadquery as cq

# Pint units used
# units.meter
# units.pascal

# Use this everywhere for Pint integration from now on
units = PintExtUnitRegistry()


def mm(value):
    """
    A helper function to provide a clean way to convert meters to mm
    """
    if value.units == 'meter':
        return value.to(units.millimeter).magnitude
    else:
        raise ValueError('Must be a length unit type to convert to mm.')


class HelloWorldChamber(object):
    def build(self, ri, t_guess, p_c, p_amb, material_strength, fs, step_size):
        pv = pressure_vessel_calcs.PressureVessel(ri, t_guess, p_c, p_amb, material_strength, fs, step_size)
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

        chamber_points = [(mm(theta_start), 0),
                          (mm(dtheta), mm(theta_end_point)),
                          (mm(dtheta), mm(pointY2)),
                          (mm(dtheta - diffX), mm(pointY2 - diffY)),
                          (mm(theta_start), mm(-t)),
                          (0, mm(-t))]

        outline = cq.Workplane('XY').polyline(chamber_points).close()

        chamber = outline.revolve(360.0, (0, ri.to(units.millimeter).magnitude, 0),
                                  (1, ri.to(units.millimeter).magnitude, 0))

        # Rotate the chamber so that it's properly aligned for 3D printing
        chamber = chamber.rotate((0, 0, 0), (0, 1, 0), -90)

        return chamber
