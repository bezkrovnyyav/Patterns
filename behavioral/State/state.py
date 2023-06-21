from abc import ABC, abstractmethod


class Phone:
    def __init__(self, state: 'State') -> None:
        self.state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: 'State') -> None:
        self._state = state
        self._state.phone = self

    def button_click(self) -> None:
        self._state.button_click()

    def switch_off(self) -> None:
        if not isinstance(self._state, SwitchedOff):
            print('Phone switches off')
            self.state = SwitchedOff()


class State(ABC):

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone: Phone):
        self._phone = phone

    @abstractmethod
    def button_click(self):
        pass


class Locked(State):

    def button_click(self):
        print('Unlocking phone')
        self.phone.state = Unlocked()


class Unlocked(State):
    def button_click(self):
        print('Do usefull job')


class SwitchedOff(State):
    def button_click(self):
        print('Phone switches on')
        self.phone.state = Unlocked()


if __name__ == '__main__':
    phone = Phone(Locked())

    phone.button_click()
    phone.button_click()
    phone.button_click()
    phone.button_click()
    phone.button_click()

    phone.switch_off()
    phone.switch_off()
    phone.button_click()
