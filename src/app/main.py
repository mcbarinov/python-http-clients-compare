import asyncio
import random
import sys
import time
from pathlib import Path

from src.app import work
from src.app.async_task_runner import AsyncTaskRunner
from src.app.sync_task_runner import TaskRunner

HTTP_CLIENTS = ["requests", "httpx", "aiohttp"]


def main() -> None:
    if len(sys.argv) > 1:
        library = sys.argv[1]
        if library not in HTTP_CLIENTS:
            print(f"invalid library: {library}, use any from {HTTP_CLIENTS}")
            sys.exit(1)
    else:
        print("no library specified")
        sys.exit(1)

    start = time.perf_counter()
    proxies = Path("proxies.txt").read_text().strip().splitlines()
    loops = 20
    runner_limit = 30
    timeout = 3.0
    if not proxies:
        print("No proxies found")
        return

    match library:
        case "requests":
            test_requests(loops, runner_limit, proxies, timeout)
        case "httpx":
            asyncio.run(test_httpx(loops, runner_limit, proxies, timeout))
        case "aiohttp":
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
    main()
