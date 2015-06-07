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

import math


class PressureVessel:
    # Variables used to calculate wall thickness
    ri = None                 # inner radius, needs a value assigned
    ro = None                 # outer radius, calculated from inner radius and thickness
    r = None                  # radius of interest in the stress calculations, generally set to position of max stress (ri for tension, r0 for compression)
    t = None                  # initial guess for thickness, needs value assigned
    p_c = None                # chamber pressure, needs value assigned
    p_amb = None              # ambient pressure, needs value assigned
    material_strength = None  # target maximum allowable strength (for example yield or ultimate), needs value assigned
    fs = 2.0                  # factor of safety

    def __init__(self, ri, t, p_c, p_amb, material_strength):
        self.ri = ri
        self.t = t            # TODO: look at automatically selecting a guess, maybe based on thick-walled theory (ri/t >= 10)
        self.ro = ri + t
        self.r = ri
        self.p_c = p_c
        self.p_amb = p_amb
        self.material_strength = material_strength

    def calculate_wall_thickness(self):
        """Solves for the desired wall thickness based on the inputs given"""

        step_size = 0.001  # Solver step size to find optimal thickness
        stress_limit = self.material_strength  # TODO: Are these terms really interchangeable like this?

        # TODO: Do we want to modify copies of ro and t to keep the originals for reference?
        # TODO: The advantange of modifying the class variables is that you end up with a PressureVessel object with
        # TODO: optimized ro and t values that you can access directly, such as pv.ro and pv.t
        # TODO: Replace this solver process with something like a binary search
        if max_stress() < stress_limit:
            #  Our vessel can handle more stress, so gradually decrease the thickness
            while max_stress() < stress_limit:
                self.t -= step_size

                # The new thickness changes our outside radius
                self.ro = self.ri + self.t
             
            self.t += step_size  # the while look exits after one too many steps, add one back

        else:
            # Our vessel can't handle the stress, gradually increase the thickness
            while max_stress() > stress_limit:  
                self.t += step_size

                # The new thickness changes our outside radius
                self.ro = self.ri + self.t

        return self.t

    def sigma_tan(self, ri, ro, r, pi, po):
        """Calculate the tangential stress in thick walled cylinder"""

        return (pi * math.pow(ri, 2) - po * math.pow(ro, 2) - math.pow(ri, 2) * math.pow(ro, 2) *
                (po - pi) / math.pow(r, 2)) / (math.pow(ro, 2) - math.pow(ri, 2))

    def sigma_rad(self, ri, ro, r, pi, po):
        """Calculate the radial stress in thick walled cylinder"""

        return (pi * math.pow(ri, 2) - po * math.pow(ro, 2) + math.pow(ri, 2) * math.pow(ro, 2) *
                (po - pi) / math.pow(r, 2)) / (math.pow(ro, 2) - math.pow(ri, 2))
    
    def max_stress(self):
        return self.fs * max(self.sigma_tan(self.ri, self.ro, self.r, self.p_c, self.p_amb),
                                            self.sigma_rad(self.ri, self.ro, self.r, self.p_c, self.p_amb))
