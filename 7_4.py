# -*- coding: utf-8 -*-
import asyncio
import aiohttp


async def fetch_status(session, url):
    async with session.get(url) as response:
        return url, response.status


async def main():
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.github.com",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_status(session, url) for url in urls]
        statuses = await asyncio.gather(*tasks)

        for url, status in statuses:
            print(f"URL: {url}, Статус: {status}")


if __name__ == "__main__":
    asyncio.run(main())
