from chaoslib.exceptions import InterruptExecution
from chaoslib.types import Activity, Run


def before_activity_control(context: Activity, **kwargs):
    raise InterruptExecution("let's blow this up")
