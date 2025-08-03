import hassapi as hass

class BaseControl(hass.Hass):
    def change_state(self, kwargs):
        if isinstance(kwargs, dict):
            new = kwargs.get('new')
        else:
            new = kwargs
        func_dict = {
            "on": self.turn_on,
            "off": self.turn_off
        }
        get_func = func_dict[new]
        for item in self.controlled_units:
            get_func(item)
        self.pending_timers = []