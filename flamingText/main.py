import aiohttp
import asyncio
from urllib.parse import urlencode
import json


class FlamingText:
    def __init__(self, **kwargs):
        self._base_url = "https://flamingtext.com/net-fu/image_output.cgi"
        self._kwargs = kwargs

    def _generateURL(self):
        if not self._kwargs:
            raise Exception("Parameter name and script are required")

        # Add common parameters
        params = {
            "_comBuyRedirect": "false",
            "imageWidth": "400",
            "imageHeight": "150",
        }

        # Add user-provided parameters
        params.update(self._kwargs)

        # Construct the URL with query parameters
        return f"{self._base_url}?{urlencode(params)}"

    async def process(self):
        url = self._generateURL()
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()


async def main():
    obj = FlamingText(text="Firdavs-coder", script="fluffy-logo")
    result = await obj.process()

    # Parse the result as JSON
    try:
        result_json = json.loads(result)
        # Print the "src" value
        print(result_json.get("src"))
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")


if __name__ == "__main__":
    asyncio.run(main())
