import hassapi as hass

class Decidehome(hass.Hass):
    def initialize(self):
        self.listen_state(self.set_presence, "sensor.sm_a145r_wi_fi_connection")
        self.log("Listening for arrivals/departures..")

    def set_presence(self, entity, attribute, old, new, kwargs):
        state = "on" if new == "VM2072540" else "off"
        self.log(f"Setting at_home to {state}")
        self.call_service("input_boolean/turn_" + state, entity_id="input_boolean.at_home")
