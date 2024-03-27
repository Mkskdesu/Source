import robot


class main(robot.robot):
    def __init__(this,period:float) -> None:
        super().__init__(period=period)

    def periodic(this):
        #do something
        pass

instance = main(5.0)

instance.start()