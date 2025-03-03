import aiofiles
import asyncio


async def read_file(file_path):
    async with aiofiles.open(file_path, mode='r') as file:
        contents = await file.read()
    return contents


async def main():
    file_contents = await read_file('pupupu.txt')
    print(file_contents)


if __name__ == '__main__':
    asyncio.run(main())
