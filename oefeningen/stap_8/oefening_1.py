import asyncio

async def hello_world():
    await asyncio.sleep(3)
    print("hello world")
    return None



asyncio.run(hello_world())