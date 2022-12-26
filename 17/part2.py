start = 434
end = 2173
cycle_len = 1740
start_height = 644
end_height = 3310
cycle_delta = end_height - start_height
cycles = (1000000000000 - start) // cycle_len

ans = cycles * cycle_delta + start_height + 1166
print(ans)