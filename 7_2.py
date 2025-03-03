# -*- coding: utf-8 -*-
import asyncio


async def process_data(data):
    processed = []
    for number in data:
        await asyncio.sleep(0.5)
        processed.append(number ** 2)
        print(f"Processed: {number} -> {number ** 2}")
    return processed


async def main():
    data = [1, 2, 3, 4, 5]
    results = await process_data(data)
    print(f"All processed results: {results}")


if __name__ == "__main__":
    asyncio.run(main())
