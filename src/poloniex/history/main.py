import os
import time

from poloniex.rest.ticker import get_ticks

folder = 'logs'
space_taken = 0
space_limit = 300 * 2 ** 20  # 300 MB


def file_size(path: str) -> int:
    return os.stat(path=path).st_size


def init():
    global space_taken
    if os.path.isdir(folder):
        for file in os.listdir(folder):
            space_taken += file_size(path=os.path.join(folder, file))
    else:
        os.mkdir(path=folder)
    print(f'started logging, disk space taken already: {space_taken} bytes')


def save_ticks():
    global space_taken
    ticks = get_ticks()
    filename = f'{folder}/{time.strftime("%Y-%m-%d_%H:%M:%S", time.gmtime())}.txt'
    with open(filename, 'w') as f:
        if space_taken < space_limit:
            f.write(str(ticks))
            f.close()
            space_taken += file_size(path=filename)
            print(f'logged current tickers to {filename}, disk space taken: {space_taken}')
        else:
            # delete old files?
            raise RuntimeWarning(f'exceeded disk space of {space_limit} bytes')


def repeat(delay: int, action):
    while True:
        time.sleep(delay)
        action()


def main():
    init()
    repeat(delay=60, action=save_ticks)


if __name__ == '__main__':
    main()
