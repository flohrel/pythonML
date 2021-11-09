import time

def ft_progress(listy):
    bar = ">"
    start = time.perf_counter()
    total = len(listy)
    for i in listy:
        t = time.perf_counter() - start
        i += 1
        eta = (total * t) / i
        percentage = int((i * 100) / total)
        progress = int((percentage * 20) / 100)
        if progress > len(bar):
            bar = bar.strip(">")
            bar += "=>"
        line = "ETA:{0:.2f}s [{1: >3d}%] [{2:<20}] {3}/{4} | elapsed time {5:.2f}s"
        print(line.format(eta, percentage, bar, i, total, t), end="\r")
        yield i