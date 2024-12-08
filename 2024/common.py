import glob


def run_day(day, fn, suffix=''):
    for path in sorted(glob.glob('data/%02d/*%s.txt' % (day, suffix))):
        print(path)
        fn(open(path))
        print()