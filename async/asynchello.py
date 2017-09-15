import asyncio
from time import sleep
from asyncio.tasks import sleep as sleepw

async def hello_coroutine(hello):
    #sleep(1)
    await sleepw(1)
    msg = 'Hello to {hello}'.format(hello=hello)
    return msg

async def main(urls):
    
    coroutines = [hello_coroutine(url) for url in urls]
    completed, pending = await asyncio.wait(coroutines)
    for item in completed:
        print(item.result())
        
if __name__ == '__main__':
    greeting = ["hello1", "hello2", "hello3", "hello4", "hello5"]
 
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(greeting))
    finally:
        event_loop.close()