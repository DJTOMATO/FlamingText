import aiohttp
import asyncio
from urllib.parse import urlencode


class FlamingText:
    _url = "https://example.com/flamingtext?"  # Replace with your actual URL
    url = "https://flamingtext.com/net-fu/image_output.cgi?_comBuyRedirect=false&imageWidth=400&imageHeight=150"

    def __init__(self, **kwargs):
        self._kwargs = kwargs

    async def _generateParams(self):
        if len(self._kwargs) == 0:
            raise Exception("Parameter name and script are required")
        return "&" + urlencode(dict(self._kwargs))

    async def _generateURL(self):
        params = await self._generateParams()
        return self._url + params

    async def process(self):
        url = await self._generateURL()
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()


async def main():
    obj = FlamingText(text="Firdavs-coder", script="fluffy-logo")
    result = await obj.process()
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
