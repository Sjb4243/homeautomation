import hassapi as hass
from Basecontrol import BaseControl
from Controllableobjsoff import controllable

class Checkleft(BaseControl):
    def initialize(self):
        self.pending_timers = []
        self.controlled_units = controllable
        self.listen_state(self.check_status, "input_boolean.at_home")
        self.parameters = self.args['parameters']

    def check_status(self, entity, attribute, old, new, kwargs):
        if new == "on":
            self.log("Sam has returned home or wifi has returned. Cancelling all existing timers and turning on lights")
            self.cancel_all()
            self.pending_timers.append(self.run_in(self.change_state, 0, new = "on"))
        if new == "off":
            self.log("Sam has left home or wifi has dropped. Beginning turn off prep")
            self.pending_timers.append(self.run_in(self.change_state, self.parameters["time"], new = "off"))


    def cancel_all(self):
        if len(self.pending_timers) == 0:
            self.log(f"No timers to cancel")
            return
        for timer in self.pending_timers:
            self.log(f"Cancelling timer:{timer}")
            self.cancel_timer(timer)
        self.pending_timers = []



