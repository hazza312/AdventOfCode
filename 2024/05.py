from common import run_day


def row_ok(row, preds):
    for i, a in enumerate(row):
        for b in row[i + 1:]:
            if a in preds and b in preds[a]:
                return False

    return True


def reorder(row, preds):
    to_place = list(row)
    ret = []

    while len(to_place) > 0:
        next = to_place.pop(0)
        if next not in preds or all(x in ret for x in preds[next] if x in row):
            ret.append(next)
        else:
            to_place.append(next)

    return ret


def main(f):
    preds = {}
    while line := f.readline().strip():
        pred, page = [int(x) for x in line.split('|')]
        if page not in preds:
            preds[page] = set()
        preds[page].add(pred)

    middle_sum_1 = 0
    middle_sum_2 = 0
    while line := f.readline():
        row = [int(x) for x in line.split(',')]
        if row_ok(row, preds):
            middle_sum_1 += row[len(row) // 2]
        else:
            row = reorder(row, preds)
            middle_sum_2 += row[len(row) // 2]

    print(middle_sum_1)
    print(middle_sum_2)


if __name__ == '__main__':
    run_day(5, main)
