import sys
import requests
from time import perf_counter


BASE_URL = "https://pokeapi.co/api/v2/pokemon/{id_}"


def sync(urls: list[str]):
    start_time = perf_counter()

    for url in urls:
        _ = requests.get(url)
    print(f"{len(urls)} pokemons received.")
    end_time = perf_counter()
    total_time = end_time - start_time
    print(total_time)


def main():
    num = int(sys.argv[2])
    urls: list[str] = [BASE_URL.format(id_=i) for i in range(1, num + 1)]
    if sys.argv[1] == "sync":
        sync(urls)
    else:
        raise NotImplementedError


if __name__ == "__main__":
    main()
