import asyncio
import random
import time
from enum import Enum, unique
from pathlib import Path

import typer
import uvloop

from src.app import work
from src.app.async_task_runner import AsyncTaskRunner
from src.app.sync_task_runner import TaskRunner

HTTP_CLIENTS = ["requests", "httpx", "aiohttp"]


@unique
class Client(str, Enum):
    requests = "requests"
    httpx = "httpx"
    aiohttp = "aiohttp"


app = typer.Typer()


@app.command()
def main(
    client: Client,
    loops: int = 20,
    runner_limit: int = 30,
    timeout: float = 3.0,
    use_uvloop: bool = False,
    proxies_file: Path = Path("proxies.txt"),
) -> None:
    start = time.perf_counter()
    proxies = proxies_file.read_text().strip().splitlines()
    if not proxies:
        print("No proxies found")
        return

    match client:
        case Client.requests:
            test_requests(loops, runner_limit, proxies, timeout)
        case Client.httpx:
            if use_uvloop:
                uvloop.run(test_httpx(loops, runner_limit, proxies, timeout))
            else:
                asyncio.run(test_httpx(loops, runner_limit, proxies, timeout))
        case Client.aiohttp:
            if use_uvloop:
                uvloop.run(test_aiohttp(loops, runner_limit, proxies, timeout))
            else:
                asyncio.run(test_aiohttp(loops, runner_limit, proxies, timeout))

    print(f"done: {time.perf_counter() - start}")


def test_requests(loops: int, runner_limit: int, proxies: list[str], timeout: float) -> None:
    for _ in range(loops):
        runner = TaskRunner(runner_limit)
        for i in range(runner_limit):
            proxy = random.choice(proxies)
            runner.add_task(f"{i}", work.requests_work, (proxy, timeout))
        runner.execute()


async def test_httpx(loops: int, runner_limit: int, proxies: list[str], timeout: float) -> None:
    for _ in range(loops):
        runner = AsyncTaskRunner(runner_limit)
        for i in range(runner_limit):
            proxy = random.choice(proxies)
            runner.add_task(f"{i}", work.httpx_work(proxy, timeout))
        await runner.run()


async def test_aiohttp(loops: int, runner_limit: int, proxies: list[str], timeout: float) -> None:
    for _ in range(loops):
        runner = AsyncTaskRunner(runner_limit)
        for i in range(runner_limit):
            proxy = random.choice(proxies)
            runner.add_task(f"{i}", work.aiohttp_work(proxy, timeout))
        await runner.run()


if __name__ == "__main__":
    app()
