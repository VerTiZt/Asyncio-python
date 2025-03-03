# -*- coding: utf-8 -*-
import asyncio


async def greet(name):
    await asyncio.sleep(2)  # Задержка на 2 секунды
    print(f"Привет, {name}!")


async def main():
    names = ["Алексей", "Мария", "Дмитрий", "Екатерина"]
    await asyncio.gather(*(greet(name) for name in names))  # Выполнение корутины для каждого имени


if __name__ == "__main__":
    asyncio.run(main())
