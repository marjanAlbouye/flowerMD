class MissingPotentialError(Exception):
    def __init__(self, connection=None, potential_class=None):
        self.connection = connection
        self.potential_class = potential_class
        msg = self._generate_msg()
        super().__init__(msg)

    def _generate_msg(self):
        return f"Missing potential for {self.connection} {self.potential_type} in {self.potential_class}."

    @property
    def potential_type(self):
        return None


class MissingPairPotentialError(MissingPotentialError):
    @property
    def potential_type(self):
        return "pair"


class MissingBondPotentialError(MissingPotentialError):
    @property
    def potential_type(self):
        return "bond"


class MissingAnglePotentialError(MissingPotentialError):
    @property
    def potential_type(self):
        return "angle"


class MissingDihedralPotentialError(MissingPotentialError):
    @property
    def potential_type(self):
        return "dihedral"


class MissingCoulombPotentialError(MissingPotentialError):
    def _generate_msg(self):
        return f"Missing Coulomb force {self.potential_class} for electrostatic interactions."


class MoleculeLoadError(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class ReferenceUnitError(Exception):
    def __init__(self, msg):
        super().__init__(msg)