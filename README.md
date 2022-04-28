# json_cold_storage_comparison

Comparing cold storage solutions for 1000 ~1Mb JSONs

## Results

The test folder had 1772 files, half being matches and the others timelines.

The table is ordered by raw storage used.

| Method | Dump time | Read time | Raw storage used | ZSTD on filesystem |
|---|---|---|---|---|
| raw | | | 513M | 77M |
| diskcache - default | 5.8s | 1.6s | 515M | 150M |
| diskcache - FanoutCache | 6s | 1.6s | 339M | 98M |
| mongo | 23s | 6.8s | 110M | 94M |
| zsdt - individual files level 3 | 1s | 0.5s | 53M |  |
| zsdt - full folder  | 1s | 0.5s | 52M |  |
| zsdt - individual files level 15 | 18s | 0.5s | 36M |  |
| lzma - python, individual files  | 64s | 1.9s | 34M |  |
| lzma - tar, full folder  | 92s | 3s | 31M | |

## Conclusion

- ZSTD is heavily customisable and is the best performer in all use cases