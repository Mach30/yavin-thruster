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
    t_guess = None                  # initial guess for thickness, needs value assigned
    p_c = None                # chamber pressure, needs value assigned
    p_amb = None              # ambient pressure, needs value assigned
    material_strength = None  # target maximum allowable strength (for example yield or ultimate), needs value assigned
    fs = None                 # factor of safety
    step_size = None

    def __init__(self, ri, t_guess, p_c, p_amb, material_strength, fs, step_size):
        self.ri = ri
        # TODO: look at automatically selecting a guess, maybe based on thick-walled theory (ri/t >= 10)
        self.t_guess = t_guess
        self.t_calc = t_guess
        self.ro = ri + t_guess
        self.r = ri
        self.p_c = p_c
        self.p_amb = p_amb
        self.material_strength = material_strength
        self.fs = fs
        self.step_size = step_size

        if self.step_size is None or self.step_size == 0:
            raise ValueError("step size must be non-zero")

    def calculate_wall_thickness(self):
        """Solves for the desired wall thickness based on the inputs given"""

        stress_limit = self.material_strength  # TODO: Are these terms really interchangeable like this?

        # TODO: Do we want to modify copies of ro and t to keep the originals for reference?
        # TODO: The advantange of modifying the class variables is that you end up with a PressureVessel object with
        # TODO: optimized ro and t values that you can access directly, such as pv.ro and pv.t
        # TODO: Replace this solver process with something like a binary search
        if self.max_stress() < stress_limit:
            #  Our vessel can handle more stress, so gradually decrease the thickness
            while self.max_stress() < stress_limit:
                self.t_calc -= self.step_size

                # The new thickness changes our outside radius
                self.ro = self.ri + self.t_calc

            self.t_calc += self.step_size  # the while look exits after one too many steps, add one back

        else:
            # Our vessel can't handle the stress, gradually increase the thickness
            while self.max_stress() > stress_limit:
                self.t_calc += self.step_size

                # The new thickness changes our outside radius
                self.ro = self.ri + self.t_calc

        return self.t_calc

    def sigma_tan(self):
        """Calculate the tangential stress in thick walled cylinder"""

        return (self.p_c * self.ri**2 - self.p_amb * self.ro**2 - self.ri**2 * self.ro**2 *
               (self.p_amb - self.p_c) / self.r**2) / (self.ro**2 - self.ri**2)

    def sigma_rad(self):
        """Calculate the radial stress in thick walled cylinder"""

        return (self.p_c * self.ri**2 - self.p_amb * self.ro**2 + self.ri**2 * self.ro**2 *
               (self.p_amb - self.p_c) / self.r**2) / (self.ro**2 - self.ri**2)

    def max_stress(self):
        """Calculates the max stress including the factor of safety """

        return max(self.sigma_tan(), self.sigma_rad()) * self.fs
