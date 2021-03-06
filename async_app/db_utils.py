import asyncio
import time
import datetime
from concurrent.futures import ThreadPoolExecutor
from async_app.models import *

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
    functions = [loop.run_in_executor(executor, func) for func in funcs]
    print ("functions:", functions)
    responses = loop.run_until_complete(asyncio.gather(*functions))
    print ("time diff:", (datetime.datetime.now() - t1))
    return responses

def cpu_task():
    sd = 242342353425 * (2131234*12)/233234 * 23423
    for i in range(1000):
        v = sd*i
    return 1

def order_details():
    #count = AsyncOrder.objects.count()
    #latest = AsyncOrder.objects.latest('id')
    #data = {"count": count, "latest": latest.id}
    data = list(PrepaidOrders.objects.filter(order__invoice__payment_method='payu', order__status='in_transit').values_list('payment_method_id'))
    #data = cpu_task()
    return data

def member_details():
    #count = AsyncMember.objects.count()
    #latest = AsyncMember.objects.latest('id')
    #data = {"count": count, "latest": latest.id}
    data = list(PrepaidOrders.objects.filter(order__invoice__payment_method='payu', order__status='in_transit').values_list('payment_method_id'))
    #data = cpu_task()
    return data
