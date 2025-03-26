import asyncio
import json
import time

import aiohttp
import httpx
import requests
from aiohttp_socks import ProxyConnector


def requests_work(proxy: str, timeout: float) -> None:
    start = time.perf_counter()
    result, error = None, None
    proxies = {"http": proxy, "https": proxy}
    try:
        r = requests.get("https://httpbin.org/ip", proxies=proxies, timeout=timeout)
        result = json.loads(r.text)["origin"]
    except requests.exceptions.Timeout:
        error = "timeout"
    except requests.exceptions.ProxyError:
        error = "proxy"
    except requests.exceptions.RequestException as err:
        error = f"connection_error: {err}"
    except Exception as err:
        error = f"exception: {err}"
    print(f"requests: done: {time.perf_counter() - start:.2f}, result: {result}, error: {error}")


async def httpx_work(proxy: str, timeout: float) -> None:
    start = time.perf_counter()
    result, error = None, None
    async with asyncio.timeout(timeout):
        try:
            async with httpx.AsyncClient(
                proxy=proxy,
                timeout=timeout,
            ) as client:
                r = await client.get("https://httpbin.org/ip")
                result = json.loads(r.text)["origin"]

        except httpx.TimeoutException:
            error = "timeout"
        except httpx.ProxyError:
            error = "proxy"
        except httpx.RequestError as err:
            error = f"connection_error: {err}"
        except Exception as err:
            error = f"exception: {err}"
    print(f"requests: done: {time.perf_counter() - start:.2f}, result: {result}, error: {error}")


async def aiohttp_work(proxy: str, timeout: float) -> None:
    start = time.perf_counter()
    result, error = None, None

    try:
        # Ensure proxy has correct format
        if not proxy.startswith(("http://", "https://", "socks5://")):
            # Assume HTTP if no scheme specified
            proxy = f"http://{proxy}"

        # Create a connector with the proxy
        connector = ProxyConnector.from_url(proxy)

        async with asyncio.timeout(timeout):
            async with aiohttp.ClientSession(connector=connector) as session:
                async with session.get("https://httpbin.org/ip") as response:
                    if response.status == 200:
                        data = await response.json()
                        result = data["origin"]
                    else:
                        error = f"HTTP error: {response.status}"

    except TimeoutError:
        error = "timeout"
    except aiohttp.ClientProxyConnectionError:
        error = "proxy"
    except aiohttp.ClientConnectorError:
        error = "proxy"  # Often indicates proxy connection issues
    except aiohttp.ClientError as err:
        error = f"connection_error: {err}"
    except Exception as err:
        error = f"exception: {err}"
    print(f"requests: done: {time.perf_counter() - start:.2f}, result: {result}, error: {error}")
