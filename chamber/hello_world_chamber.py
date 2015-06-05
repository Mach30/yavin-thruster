# Copyright (C) 2015 Mach 30 - http://www.mach30.org
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# IMPORTANT: You must install FreeCAD and the CadQuery module for FreeCAD to
# run this script. https://github.com/jmwright/cadquery-freecad-module

import math
import cadquery as cq
from Helpers import show

# TODO: Integrate Pint: http://www.google.com/url?q=http%3A%2F%2Fopendesignengine.net%2Fdmsf_files%2F478%3Fdownload%3D&sa=D&sntz=1&usg=AFQjCNF8piQ2QOI9d1x9YfKzfeyqgaa0Bg

# TODO: Change angle name to theta

angle_degrees = 45  # The chamber taper angle in degrees
angle_radians = math.radians(angle_degrees)  # The chamber taper angle in radians
t = 1.5  # TODO: Get this from MTK library
ri = 20  # TODO: Get this from MTK library
total_length = 100.0  # The entire length of the exterion or the chamber
converg_sect_length = total_length * 0.35  # TODO: Figure out the real-world value of this - is a design choice

# Where our taper starts at the business end of the chamber
angle_start = total_length - converg_sect_length

angle_end_point = converg_sect_length * math.tan(angle_radians)

# Points to construct our polyline so we can revolve it
# chamber_points = [(0, 0),
#                   (angle_start, 0),
#                   (angle_start + converg_sect_length, angle_end_point),
#                   (angle_start + converg_sect_length, angle_end_point + t),
#                   (angle_start, t),
#                   (0, t),
#                   (0, 0)]

# Set up some of our re-usable dimensions
dtheta = angle_start + converg_sect_length

pointX = dtheta - math.cos(angle_radians) * math.tan(angle_radians) * t
pointY = angle_end_point - math.sin(angle_radians) * math.tan(angle_radians) * t
diffX = pointX - angle_start
diffY = pointY - 0

chamber_points = [(0, 0),
                  (angle_start, 0),
                  (dtheta, angle_end_point),
                  (dtheta, angle_end_point - t / math.cos(angle_radians)),
                  ((dtheta - diffX), (angle_end_point - t / math.cos(angle_radians) - diffY)),
                  (angle_start, -t),
                  (0, -t),
                  (0, 0)
                  ]

outline = cq.Workplane('XY').polyline(chamber_points)

chamber = outline.revolve(360.0, (0, angle_end_point + t + ri, 0),
                          (1, angle_end_point + t + ri, 0))

# Use the following to render your model with grey RGB and no transparency
#show(outline, (204, 204, 204, 0.0))
show(chamber, (204, 204, 204, 0.0))
