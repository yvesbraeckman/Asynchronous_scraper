import asyncio

async def counter(j):
    for i in range(j):
        print(i)
        await asyncio.sleep(2)
    return None


async def taak_2():
    while True:
        await asyncio.sleep(3)
        print("taak 2")


async def taak_3():
    while True:
        await asyncio.sleep(5)
        print("taak 3")


async def main():
    batch = asyncio.gather(counter(10), taak_2(), taak_3())
    await batch


if __name__ == "__main__":
    asyncio.run(main())