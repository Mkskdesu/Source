from threading import Thread
import time
from typing import Optional
import ntcore

from mathutil import mathUtil
from constants import constants

class robot():

    _ntInstance = None #except NetworkTableInstance

    def __init__(this,period:Optional[float]) -> None:
        this.running = False
        
        if period == None:
            period = constants.PERIOD_TIME

        this.periodTime = period

        if robot._ntInstance == None:
            robot.setupNetworktables()

    @classmethod
    def setupNetworktables(this) -> None:
        robot._ntInstance = ntcore.NetworkTableInstance.getDefault()
        robot._ntInstance.setServerTeam(constants.TEAM_NUMBER,constants.NT_SERVER_PORT)
        robot._ntInstance.startDSClient()
        robot._ntInstance.startClient4(constants.CLIENT_IDENTITY)

    @classmethod
    def getNtInstance(this) -> ntcore.NetworkTableInstance:
        return robot._ntInstance
    
    def start(this):
        this.running = True
        this.periodicRunner()

    def pause(this):
        this.running = False

    def periodicRunner(this):
        while this.running:
            try:
                currentTime = time.time()
                this.periodic()
                time.sleep(mathUtil.max(0.0,this.periodTime - (time.time() - currentTime)))
                continue
            except KeyboardInterrupt:
                this.pause()

    def periodic():
        pass
