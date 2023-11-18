import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon/88")
data = response.json()
# print(data["name"])


class ApiClient:
    ALLOWED_METHODS: list[str] = ["get"]

    def __init__(self, base_url: str) -> None:
        self.base_url: str = base_url

    def get_response(self, method: str, endpoint: str) -> dict:
        if method not in self.ALLOWED_METHODS:
            raise NotImplementedError(f"Method {method} is not implemented")

        callback = getattr(requests, method)
        url = "".join([self.base_url, endpoint])
        response = callback(url)

        try:
            return response.json()
        except Exception:
            raise Exception("HTTP reques ERROR")


class ApiClientContext:
    def __init__(self, base_url: str) -> None:
        self._client: ApiClient | None = None
        self.base_url: str = base_url

    def __enter__(self):
        self._client = ApiClient(base_url=self.base_url)
        return self._client

    def __exit__(self, exc_type, exc_value, tb):
        # try:
        #   print("Exiting from Api client...")
        #   print(exc_type)
        #   print(exc_value)
        # except Exception:
        #   return
        print(f"Unexpected client's response: {exc_value}")
        print("Closing the Client...")
        # self._client.close()


# poke_api_client = ApiClient(base_url="https://pokeapi.co/api/v2")
# pokemon_data = poke_api_client.get_response(
#   method="get", endpoint="/pokemon/88"
# )
# print(pokemon_data)

with ApiClientContext(base_url="https://pokeapi.co/api/v2") as client:
    pokemon_data = client.get_response(method="get", endpoint="/pokemon/88")
    print(f"Fetched pokemon: {pokemon_data['name']}")
