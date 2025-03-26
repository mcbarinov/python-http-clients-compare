loops = 20, runner_limit = 30, timeout = 3.0

1) requests
Command being timed: "uv run python -m app.main requests"
User time (seconds): 4.04
System time (seconds): 0.63
Percent of CPU this job got: 19%
Elapsed (wall clock) time (h:mm:ss or m:ss): 0:24.13
Average shared text size (kbytes): 0
Average unshared data size (kbytes): 0
Average stack size (kbytes): 0
Average total size (kbytes): 0
Maximum resident set size (kbytes): 43884
Average resident set size (kbytes): 0
Major (requiring I/O) page faults: 514
Minor (reclaiming a frame) page faults: 12684
Voluntary context switches: 14646
Involuntary context switches: 198
Swaps: 0
File system inputs: 108248
File system outputs: 0
Socket messages sent: 0
Socket messages received: 0
Signals delivered: 0
Page size (bytes): 4096
Exit status: 0


2) httpx
Command being timed: "uv run python -m app.main httpx"
User time (seconds): 38.34
System time (seconds): 0.52
Percent of CPU this job got: 63%
Elapsed (wall clock) time (h:mm:ss or m:ss): 1:00.77
Average shared text size (kbytes): 0
Average unshared data size (kbytes): 0
Average stack size (kbytes): 0
Average total size (kbytes): 0
Maximum resident set size (kbytes): 102132
Average resident set size (kbytes): 0
Major (requiring I/O) page faults: 514
Minor (reclaiming a frame) page faults: 24645
Voluntary context switches: 2576
Involuntary context switches: 234
Swaps: 0
File system inputs: 110384
File system outputs: 2456
Socket messages sent: 0
Socket messages received: 0
Signals delivered: 0
Page size (bytes): 4096
Exit status: 0

3) aiohttp
Command being timed: "uv run python -m app.main aiohttp"
User time (seconds): 3.02
System time (seconds): 0.51
Percent of CPU this job got: 13%
Elapsed (wall clock) time (h:mm:ss or m:ss): 0:27.05
Average shared text size (kbytes): 0
Average unshared data size (kbytes): 0
Average stack size (kbytes): 0
Average total size (kbytes): 0
Maximum resident set size (kbytes): 91448
Average resident set size (kbytes): 0
Major (requiring I/O) page faults: 7
Minor (reclaiming a frame) page faults: 22507
Voluntary context switches: 2935
Involuntary context switches: 40
Swaps: 0
File system inputs: 208
File system outputs: 0
Socket messages sent: 0
Socket messages received: 0
Signals delivered: 0
Page size (bytes): 4096
Exit status: 0