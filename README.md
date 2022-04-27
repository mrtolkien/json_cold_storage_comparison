# json_cold_storage_comparison

Comparing cold storage solutions for 1000 ~1Mb JSONs

## Results

The test folder had 1772 files, half being matches and the others timelines.

| Method | Write time | Read time | Raw storage used | ZSTD on ZFS |
|---|---|---|---|---|
| raw | | | 513Mb | 77Mb |
| diskcache | 6s | 1.6s | 339Mb | 98Mb |
| mongo | 23s | 6.8s | 110Mb | 94Mb |
| lzma  | 64s | 1.9s | 34Mb | 34Mb |
