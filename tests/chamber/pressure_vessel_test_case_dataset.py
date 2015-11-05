from pressure_vessel_calcs import *
from pint import UnitRegistry

class PressureVesselTestCaseDataset():
    _datatable = []

    def __init__(self):
        units = UnitRegistry()

        t_guess = 0.1 * units.inch
        p_amb = 0.001 * units.psi
        fs = 1.5
        step_size = 0.001 * units.inch

        ## populatng data without using the PressureVessel class so that any errors with the class,
        ## or any of its methods, will be uncovered during test execution and not during dataset
        ## initialization

        ## Inputs and expected values based upon dissertation by J. Simmons

        data = self._Data()
        data.name = 'INCONEL 718, run 63'
        data.ri = 5.2399 * units.inch
        data.t_guess = t_guess
        data.p_c = 1333.29 * units.psi
        data.p_amb = p_amb
        data.material_strength = 156e3 * units.psi
        data.fs = fs
        data.step_size = step_size
        data.t_expected = 0.067 * units.inch
        self._datatable.append(data)

        data = self._Data()
        data.name = 'INCONEL 718, run 57'
        data.ri = 5.2399 * units.inch
        data.t_guess = t_guess
        data.p_c = 4236.04 * units.psi
        data.p_amb = p_amb
        data.material_strength = 156e3 * units.psi
        data.fs = fs
        data.step_size = step_size
        data.t_expected = 0.218 * units.inch
        self._datatable.append(data)

        data = self._Data()
        data.name = 'INCONEL 718, run 55' 
        data.ri = 9.5433 * units.inch
        data.t_guess = t_guess
        data.p_c = 4125.37 * units.psi
        data.p_amb = p_amb
        data.material_strength = 156e3 * units.psi
        data.fs = fs
        data.step_size = step_size
        data.t_expected = 0.387 * units.inch
        self._datatable.append(data)

        data = self._Data()
        data.name = 'Alloy 188, run 45'
        data.ri = 5.2399 * units.inch
        data.t_guess = t_guess
        data.p_c = 1333.29 * units.psi
        data.p_amb = p_amb
        data.material_strength = 42e3 * units.psi
        data.fs = fs
        data.step_size = step_size
        data.t_expected = 0.256 * units.inch
        self._datatable.append(data)

        data = self._Data()
        data.name = 'Alloy 188, run 40' 
        data.ri = 9.5433 * units.inch
        data.t_guess = t_guess
        data.p_c = 2583.42 * units.psi
        data.p_amb = p_amb
        data.material_strength = 42e3 * units.psi
        data.fs = fs
        data.step_size = step_size
        data.t_expected = 0.926 * units.inch
        self._datatable.append(data)

        data = self._Data()
        data.name = 'Alloy 188, run 37'
        data.ri = 9.5433 * units.inch
        data.t_guess = t_guess
        data.p_c = 4125.37 * units.psi
        data.p_amb = p_amb
        data.material_strength = 42e3 * units.psi
        data.fs = fs
        data.step_size = step_size
        data.t_expected = 1.527 * units.inch
        self._datatable.append(data)

        data = self._Data()
        data.name = 'Ox-Free Copper, run 18'
        data.ri = 5.2399 * units.inch
        data.t_guess = t_guess
        data.p_c = 1333.29 * units.psi
        data.p_amb = p_amb
        data.material_strength = 56.6e3 * units.psi
        data.fs = fs
        data.step_size = step_size
        data.t_expected = 0.189 * units.inch
        self._datatable.append(data)

        data = self._Data()
        data.name = 'Ox-Free Copper, run 11'
        data.ri = 7.745 * units.inch
        data.t_guess = t_guess
        data.p_c = 4351.64 * units.psi
        data.p_amb = p_amb
        data.material_strength = 46.4e3 * units.psi
        data.fs = fs
        data.step_size = step_size
        data.t_expected = 1.179 * units.inch
        self._datatable.append(data)

        data = self._Data()
        data.name = 'Ox-Free Copper, run 13'
        data.ri = 9.5433 * units.inch
        data.t_guess = t_guess
        data.p_c = 2583.42 * units.psi
        data.p_amb = p_amb
        data.material_strength = 17.4e3 * units.psi
        data.fs = fs
        data.step_size = step_size
        data.t_expected = 2.426 * units.inch
        self._datatable.append(data)

    def __getitem__(self, key):
        data = self._datatable[key]
        return PressureVesselTestCase(
            data.name,
            data.ri,
            data.t_guess,
            data.p_c,
            data.p_amb,
            data.material_strength,
            data.fs,
            data.step_size,
            data.t_expected)

    class _Data:
        pass
 
class PressureVesselTestCase(PressureVessel):
    name = None
    t_expected = None

    def __init__(self, name, ri, t_guess, p_c, p_amb, material_strength, fs, step_size, t_expected):
        super(PressureVesselTestCase, self).__init__(ri, t_guess, p_c, p_amb, material_strength, fs, step_size)
        self.name = name
        self.t_expected = t_expected
        self.calculate_wall_thickness()
