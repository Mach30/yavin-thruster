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


# Bell DeLaval nozzle by Mach 30
# Based on the OpenSCAD design by @buback here - https://github.com/Buback/ParametricDeLavalModel/blob/master/BellDeLavalNozzle.scad
import math
import FreeCAD

# Radii
throat_radius = 1.5   # Wierd shapes can happen at low expansion ratios
chamber_radius = 5.0  # Combution chamber radius

expan_ratio = 30.0    # Expansion ratio

# Define exit radius by expansion ratio
exit_radius = throat_radius * math.sqrt(expan_ratio)
print("Radius of Exit:\t\t" + str(exit_radius))

# The areas to back out the expansion ratio
area_of_exit = math.pi * math.pow(exit_radius, 2)
area_of_throat = math.pi * math.pow(throat_radius, 2)

# Expansion ratio is Area of Exit/Area of Throat
expan_ratio = area_of_exit / area_of_throat

# Do a sanity check of the expansion ratio
print("Area of Exit:\t\t" + str(area_of_exit))
print("Area of Throat:\t\t" + str(area_of_throat))
print("Expansion Ratio:\t\t" + str(expan_ratio))

# Angles
diver_angle = 35  # Divergent section angle
conver_angle = 35  # Convergent section angle typ 20-45 deg Not as critical

# Other dimensions
conic_approx = 15  # Conic approximation nozzle at 15 deg typ 12-18 deg
diver_length = (exit_radius - throat_radius) * \
               (math.sin(math.radians(90)) /
                math.sin(math.radians(conic_approx)))  # Conic nozzle divergent sect length

conver_length = (chamber_radius - throat_radius) * \
                (math.sin(math.radians(90)) /
                 math.sin(math.radians(conver_angle)))  # Conic nozzle convergent sect length

fract_length = 80 / 100  # Fractional length of bell compared to conic nozzle

#chamber_length = math.exp( (.029 * ln(math.pow(throat_radius * 2, 2))) + (.47*ln(Rt*2)) + 1.94 )
