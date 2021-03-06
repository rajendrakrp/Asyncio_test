import asyncio
import aiomysql
import datetime
import time
query = "select payment_method_id from order_prepaidorders inner join order_order on " \
        "(order_prepaidorders.order_id=order_order.id) inner join order_invoice on (order_order.invoice_id=order_invoice.id) where order_invoice.payment_method='payu' " \
        "and order_order.status='in_transit'"


async def create_conn_pool():
    global g_pool
    print ("gpool*******************: %s", g_pool)
    if g_pool is None:
        g_pool = await aiomysql.create_pool(host='127.0.0.1', port=3306, minsize=1,
                                          user='root', password='password', db='db10042015',
                                          )
    return g_pool


async def execute_query():
    #pool = await aiomysql.create_pool(host='127.0.0.1', port=3306, minsize=10,
                                      #user='root', password='password', db='db10042015')
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                  user='root', password='password', db='db10042015')

    #with (await pool) as conn:
    async with conn.cursor() as cur:
        #cur = await conn.cursor()
        await cur.execute(query)
        r = await cur.fetchall()
        await cur.close()
        return r
    #pool.close()
    #await pool.wait_closed()


def get_results(func1, func2):
    try:
        loop = asyncio.get_event_loop()
        print ("loop inside try: %s", loop)
    except RuntimeError:
        loop = asyncio.new_event_loop()
        print ("loop inside except: %s", loop)
        asyncio.set_event_loop(loop)

    print ("loop outside try: %s", loop)
    t1 = datetime.datetime.now()
    functions = [asyncio.ensure_future(func1()), asyncio.ensure_future(func2())]
    responses = loop.run_until_complete(asyncio.gather(*functions))
    print ("time diff:", (datetime.datetime.now() - t1))
    return responses


def cpu_task():
    sd = 242342353425 * (2131234*12)/233234 * 23423
    for i in range(1000):
        v = sd*i
    return 1

async def func1():
    res = await execute_query()
    #await asyncio.sleep(5, result="sleep func1")
    #res = cpu_task()
    return res

async def func2():
    res = await execute_query()
    #await asyncio.sleep(10, result="sleep func1")
    #res = cpu_task()
    return res

