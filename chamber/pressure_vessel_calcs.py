import math


class PressureVessel:
    # Variables used to calculate wall thickness
    ri = None                 # inner radius, needs a value assigned
    ro = None                 # outer radius, calculated from inner radius and thickness
    r = None                  # Radius defined whether experiencing tension or compression
    t = None                  # initial guess for thickness, needs value assigned
    p_c = None                # chamber pressure, needs value assigned
    p_amb = None              # ambient pressure, needs value assigned
    material_strength = None  # target maximum allowable strength (for example yield or ultimate), needs value assigned
    fs = 2.0                  # factor of safety

    def __init__(self, ri, t, p_c, p_amb, material_strength):
        self.ri = ri
        self.t = t
        self.ro = ri + t
        self.r = ri     # ri in tension and r0 in compression, we're always in tension here, ri = max stress
        self.p_c = p_c
        self.p_amb = p_amb
        self.material_strength = material_strength

    def calculate_wall_thickness(self):
        """Solves for the optimal wall thickness based on the inputs given"""

        step_size = 0.001  # Solver step size to find optimal thickness
        stress_limit = self.material_strength  # TODO: Are these terms really interchangeable like this?

        max_stress = self.fs * max(self.sigma_tan(self.ri, self.ro, self.r, self.p_c, self.p_amb),
                                   self.sigma_rad(self.ri,  self.ro, self.r, self.p_c, self.p_amb)) / 1000.0

        # TODO: Do we want to modify copies of ro and t to keep the originals for reference?
        # TODO: The advantange of modifying the class variables is that you end up with a PressureVessel object with
        # TODO: optimized ro and t values that you can access directly, such as pv.ro and pv.t
        if max_stress < stress_limit:  # Our vessel can handle more stress, so gradually decrease the thickness
            while max_stress < stress_limit:
                self.t -= step_size

                # The new thickness changes our outside radius
                self.ro = self.ri + self.t

                max_stress = self.fs * max(self.sigma_tan(self.ri, self.ro, self.r, self.p_c, self.p_amb),
                                           self.sigma_rad(self.ri, self.ro, self.r, self.p_c, self.p_amb)) / 1000.0
        else:
            while max_stress > stress_limit:  # Our vessel can't handle the stress, gradually increase the thickness
                self.t += step_size

                # The new thickness changes our outside radius
                self.ro = self.ri + self.t

                max_stress = self.fs * max(self.sigma_tan(self.ri, self.ro, self.r, self.p_c, self.p_amb),
                                           self.sigma_rad(self.ri, self.ro, self.r, self.p_c, self.p_amb)) / 1000.0

        return self.t

    def sigma_tan(self, ri, ro, r, pi, po):
        """Calculate the tangential stress in thick walled cylinder"""

        return (pi * math.pow(ri, 2) - po * math.pow(ro, 2) - math.pow(ri, 2) * math.pow(ro, 2) *
                (po - pi) / math.pow(r, 2)) / (math.pow(ro, 2) - math.pow(ri, 2))

    def sigma_rad(self, ri, ro, r, pi, po):
        """Calculate the radial stress in thick walled cylinder"""

        return (pi * math.pow(ri, 2) - po * math.pow(ro, 2) + math.pow(ri, 2) * math.pow(ro, 2) *
                (po - pi) / math.pow(r, 2)) / (math.pow(ro, 2) - math.pow(ri, 2))
