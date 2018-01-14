import src.exceptions


class SignalManager:

    def __init__(self, controller):
        self.controller = controller

    def stop(self):
        self.controller.save()
        raise src.exceptions.EndProgramSignal

    def get_signals_available(self):
        return [
            signal_ for signal_ in dir(self)
            if callable(getattr(self, signal_))
            and not signal_.startswith('_')
            and signal_ != "handle_signal"
        ]

    def handle_signal(self, signal):
        try:
            return getattr(self, signal)()
        except AttributeError:
            if self.controller.settings.DEBUG:
                print(f"Le signal {signal} est inconnu.\nSignaux disponnibles : {self.get_signals_available()}")
            raise src.exceptions.InvalidSignalError
