import hassapi as hass
from Basecontrol import BaseControl
from Controllableobjsoff import controllable

class Detectcharging(BaseControl):
    def initialize(self):
        self.log("Listening for charging..")
        self.controlled_units = controllable
        self.listen_state(self.check_status, "binary_sensor.sm_a145r_is_charging")

    def check_status(self, entity, attribute, old, new, kwargs):
        if self.get_state("input_boolean.at_home") != "on":
            self.log("Sam not home - passing")
            return
        #We pass the opposite because if its charging, we want stuff to turn off and vice versa
        if new == "on":
            self.change_state("off")
        if new == "off":
            self.change_state("on")