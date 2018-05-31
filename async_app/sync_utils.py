import asyncio
import time
import datetime
from concurrent.futures import ThreadPoolExecutor

to_date = datetime.datetime.now()
from_date = to_date - datetime.timedelta(days=365)

def get_results(func1, func2):
    executor = ThreadPoolExecutor(10)
    result = []
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    t1 = datetime.datetime.now()
    funcs = [func1, func2]

    #functions = [loop.run_in_executor(executor, func1), loop.run_in_executor(executor, func2)]
    functions = [loop.run_in_executor(executor, func) for func in funcs]
    print ("functions:", functions)
    responses = loop.run_until_complete(asyncio.gather(*functions))
    print ("time diff:", (datetime.datetime.now() - t1))
    return responses

def func1():
    time.sleep(5)
    return "func1"

def func2():
    time.sleep(10)
    return "func2"

def get_orders():
    pass

def get_payus():
    pass

def get_paytms():
    pass

