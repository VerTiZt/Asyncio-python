# -*- coding: utf-8 -*-
import asyncio
import aiohttp


async def fetch_status(session, url):
    try:
        async with session.get(url) as response:
            return url, response.status
    except aiohttp.ClientError as e:
        return url, f"Ошибка сети: {e}"
    except asyncio.TimeoutError:
        return url, "Ошибка: время ожидания истекло"
    except Exception as e:
        return url, f"Неизвестная ошибка: {e}"


async def main():
    urls = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.github.com",
        "https://www.invalid-url.com",  # Неверный URL для проверки
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_status(session, url) for url in urls]
        statuses = await asyncio.gather(*tasks)

        for url, status in statuses:
            print(f"URL: {url}, Статус: {status}")


if __name__ == "__main__":
    asyncio.run(main())
