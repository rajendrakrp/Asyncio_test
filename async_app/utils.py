import asyncio
import time
import datetime

def get_results(func1, func2):
    result = []
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    t1 = datetime.datetime.now()
    functions = [asyncio.ensure_future(func1()), asyncio.ensure_future(func2())]
    print ("functions:", functions)
    responses = loop.run_until_complete(asyncio.gather(*functions))
    print ("time diff:", (datetime.datetime.now() - t1))
    return responses

async def func1():
    return await asyncio.sleep(5, result="sleep func1")

async def func2():
    return await asyncio.sleep(10, result="sleep func2")

