loops = 20, runner_limit = 30, timeout = 3.0

aiohttp: 27.25 seconds
requests: 28.82 seconds
httpx: 45.53 seconds

python3 -m app.main requests  4.49s user 1.15s system 11% cpu 48.905 total
python3 -m app.main httpx  22.59s user 0.86s system 50% cpu 46.771 total
python3 -m app.main aiohttp  3.77s user 0.93s system 16% cpu 27.860 total