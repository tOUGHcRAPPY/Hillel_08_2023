import asyncio
import sys
from time import perf_counter
from typing import Coroutine

import httpx

BASE_URL = "https://pokeapi.co/api/v2/pokemon/{id_}"


def sync(urls: list[str]):
    import requests

    start_time = perf_counter()

    for url in urls:
        _ = requests.get(url)
    print(f"{len(urls)} pokemons received.")
    end_time = perf_counter()
    total_time = end_time - start_time
    print(total_time)


def gsync(urls: list[str]):
    import grequests

    start_time = perf_counter()

    rs = (grequests.get(u) for u in urls)
    grequests.map(rs)
    print(f"{len(urls)} pokemons received.")
    end_time = perf_counter()
    total_time = end_time - start_time
    print(total_time)


async def async_process(url: str):
    async with httpx.AsyncClient() as client:
        client.get(url)


async def _run(*tasks: Coroutine):
    await asyncio.gather(*tasks)


def main():
    num = int(sys.argv[2])
    urls: list[str] = [BASE_URL.format(id_=i) for i in range(1, num + 1)]
    if sys.argv[1] == "sync":
        sync(urls)
    elif sys.argv[1] == "gsync":
        gsync(urls)
    elif sys.argv[1] == "async":
        tasks: list[Coroutine] = [async_process(url) for url in urls]
        asyncio.run(_run(*tasks))
        # asyncio.run(asyncio.gather(*tasks))
    else:
        raise NotImplementedError


if __name__ == "__main__":
    main()
