import asyncio
import sys
from time import perf_counter
from typing import Coroutine

import httpx

BASE_URL = "https://pokeapi.co/api/v2/pokemon/{id_}"


async def async_process(url: str):
    async with httpx.AsyncClient() as client:
        await client.get(url)


async def _run(*tasks: Coroutine):
    start_time = perf_counter()
    await asyncio.gather(*tasks)
    end_time = perf_counter()
    total_time = end_time - start_time
    print(total_time)


def main():
    num = int(sys.argv[2])
    urls: list[str] = [BASE_URL.format(id_=i) for i in range(1, num + 1)]
    if sys.argv[1] == "async":
        tasks: list[Coroutine] = [async_process(url) for url in urls]
        asyncio.run(_run(*tasks))
    else:
        raise NotImplementedError


if __name__ == "__main__":
    main()
