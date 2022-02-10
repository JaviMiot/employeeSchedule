import datetime
from schedule.models import DayOfWork
"""
         10:00 ------------------- 12:00 Base de comparación
!  9:00 ------------------- 11:00 comparo con el tiempo ingresado
!  9:00 ---------------------------------- 13:00 comparo con el tiempo ingresado
?                11:00 -------- 11:30
?               11:00 --------------- 12:30
"""


def isTimeintoRange(timeRange: DayOfWork, time: datetime.time) -> bool:
    if timeRange.startTime <= time and time <= timeRange.finishTime:
        return True
    else:
        return False


def matchRangeTime(time1: DayOfWork, time2: DayOfWork) -> bool:
    isStartInto = False
    isFinishInto = False

    if time1.startTime > time2.startTime:
        isStartInto = isTimeintoRange(time2, time1.startTime)
        isFinishInto = isTimeintoRange(time2, time1.finishTime)
    else:
        isStartInto = isTimeintoRange(time1, time2.startTime)
        isFinishInto = isTimeintoRange(time1, time2.finishTime)

    return isStartInto or isFinishInto
