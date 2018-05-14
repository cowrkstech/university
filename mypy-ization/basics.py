from typing import Dict, Any


def simple_schedule(msg, email, time):
    return {'status': 'success'}


def schedule_with_types(msg: str, email: str, time: float) -> Dict[str, str]:
    return {'status': 'success'}


def greeting_scheduler(email: str, time: float) -> dict:
    status: dict
    name: str = email.split('@')[0]
    msg = f'GoodMorning {name}'
    status = simple_schedule(msg, email, time)
    return status


def another_greeting_scheduler(email: str, time: float) -> Dict[int, str]:
    name: str = email.split('@')[0]
    msg = f'GoodMorning {name}'
    status = simple_schedule(msg, email, time)  # change to below line to see the error
    # status = schedule_with_types(msg, email, time)
    return status


if __name__ == '__main__':
    # return type from functions
    status1 = greeting_scheduler('someone@somecompany.com', 1526367671.0644903)
    status2 = another_greeting_scheduler('someone@somecompany.com', 1526367671.0644903)

    # auto inferring of types
    a = 'a'
    a = 1  # this will fail
    i, j = 0, 'str'
    j, i = i, j  # this will fail

    # introduction of Any
    first: Any = None
    second: str = ''
    first = 2
    second = a
