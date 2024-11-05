class Satellite:
    """Class to represent a satellite object in the records."""

    # (Lisa M.)
    def __init__(
        self,
        name=None,
        orbit_type=None,
        orbit_height=None,
        cycle=None,
        date=None,
        oos_date=None,
        org=None,
    ):
        self.name = name  # satellite name (Peter V)
        self.orbit_type = orbit_type  # satellite orbit type (Peter V)
        self.orbit_height = orbit_height  # satellite orbit height (Peter V)
        self.cycle = cycle  # Satellite cycle
        self.date = date  # Date satellite was sent into space
        self.oos_date = oos_date  # Date satellite became out of service
        self.org = org  # Name of organization that sent satellite

    @staticmethod  # (Gabriel C.)
    def _validate_non_empty_string(value, field_name):
        if value is None:
            return ""
        return value

    @staticmethod  # (Gabriel C.)
    def _parse_optional_int(value, field_name):
        if value is None or value == "":
            return None
        try:
            return int(value)
        except ValueError:
            raise ValueError(
                f"{field_name} must be an integer or empty string."
            )

    @staticmethod  # (Gabriel C.)
    def _parse_optional_float(value, field_name):
        if value is None or value == "":
            return None
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"{field_name} must be a float or empty string.")

    # getter & setter for oos date (Lisa M.)
    @property
    def oos_date(self):
        return self._oos_date

    @oos_date.setter
    def oos_date(self, oos_date):
        self._oos_date = self._parse_optional_int(oos_date, "oos_date")

    # getter & setter for org (Lisa M.)
    @property
    def org(self):
        return self._org

    @org.setter
    def org(self, org):
        self._org = self._validate_non_empty_string(org, "org")

    # getter and setter for name of satellite (Peter V)
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = self._validate_non_empty_string(name, "Name")

    # getter and setter for satellite's orbit type (Peter V)
    @property
    def orbit_type(self):
        return self._orbit_type

    @orbit_type.setter
    def orbit_type(self, orbit_type):
        self._orbit_type = self._validate_non_empty_string(
            orbit_type, "Orbit Type"
        )

    # getter and setter for Satellite orbit height (Peter V)
    @property
    def orbit_height(self):
        return self._orbit_height

    @orbit_height.setter
    def orbit_height(self, orbit_height):
        self._orbit_height = self._parse_optional_int(
            orbit_height, "Orbit Height"
        )

    @property  # (Gabriel C.)
    def cycle(self):
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        self._cycle = self._parse_optional_float(cycle, "Cycle")

    @property  # (Gabriel C.)
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = self._parse_optional_int(date, "Date")

    # magic string method (Peter V)
    def __str__(self):
        """String representation of the satellite object"""
        return f"Name: {self._name}, Orbit Type: {self._orbit_type}, Orbit Height: {self._orbit_height}, Cycle: {self._cycle}, Date: {self._date}, Oos Date: {self._oos_date}, Org: {self._org}"
