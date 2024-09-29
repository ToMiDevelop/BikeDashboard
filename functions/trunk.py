from machine import Pin

class Trunk:
    def __init__(self, _switch_left_nc: Pin, _switch_right_nc: Pin):
        """
        This class initializes the logic of switches connected to the the board and
        provides a function used to check and return the state of each switch.\n
        _switch_left_nc - a specified machine Pin object\n
        _switch_right_nc - a specified machine Pin object\n
        Provided Pin objects should be configured as inputs with internal pull down activated.
        """
        self.switch_1_nc = _switch_left_nc
        self.switch_2_nc = _switch_right_nc

    def TrunkState(self, _trunk: str = 'left'):
        """
        This functions read and returns the state of a the trunk lid,
        which is in fact the state of the limit switch installed next to the trunk lid.\n
        By default the left is chosed by setting:\n
        _trunk = 'left'.\n
        If you want to shoose the other one provide\n
        'right' or _trunk = 'right'\n
        as the argument.\n
        If the chosen trunk is open 'OTWARTY' string is returned, of the trunk is open 'ZAMK.' string is returned.
        """
        nc = self.switch_1_nc
        if _trunk == 'right':
            nc = self.switch_2_nc
        #print(_trunk + ': nc = ' + str(nc.value()) + ', no = ' + str(nc.value()))
        if nc.value() == 1:
            return 'OTWARTY'
        if nc.value() == 0:
            return ' ZAMK. '