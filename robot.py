from threading import Thread
import time
import ntcore

from mathutil import mathUtil
from variables import variables

class robot():

    _ntInstance = None #except NetworkTableInstance

    def __init__(this,period:float) -> None:
        this._mainLoopThread = None #except thread
        this.running = False
        
        if period == None:
            period = 0.02

        this.periodTime = period

        if robot._ntInstance == None:
            robot.setupNetworktables()

    @classmethod
    def setupNetworktables(this) -> None:
        robot._ntInstance = ntcore.NetworkTableInstance.getDefault()
        robot._ntInstance.setServerTeam(variables.TEAM_NUMBER,variables.NT_SERVER_PORT)
        robot._ntInstance.startDSClient()
        robot._ntInstance.startClient4()

    @classmethod
    def getNtInstance(this) -> ntcore.NetworkTableInstance:
        return robot._ntInstance
    
    def start(this):
        this.running = True
        this._mainLoopThread = Thread(target=this.periodicRunner)
        this._mainLoopThread.run()

    def stop(this):
        this.running = False

    def periodicRunner(this):
        while this.running:
            try:
                currentTime = time.time()
                this.periodic()
                time.sleep(mathUtil.max(0.0,this.periodTime - (time.time() - currentTime)))
                continue
            except KeyboardInterrupt:
                this.stop()

    def periodic():
        pass
