from typing import Optional

from constants import constants
from robot import robot

class main(robot):
    def __init__(this,period:float) -> None:
        if period == None:
            period = constants.PERIOD_TIME
        super().__init__(period=period)

    def periodic(this):
        #type something
        pass

instance = main(0.02)

instance.start()
