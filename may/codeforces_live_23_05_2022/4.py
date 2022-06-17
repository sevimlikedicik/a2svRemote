def condition(layer, target):
    for elem in layer:
        if len(elem) == target:
            return True

    return False


def solution():
    n, x = input().split(' ')
    target = int(n)
    layer = {x}
    oper = 0
    cond = condition(layer, target)

    while not cond and oper < 200:
        oper += 1
        copy_layer = list(layer)
        layer = set()
        while copy_layer:
            curr = copy_layer.pop(0)
            for d in curr:
                layer.add(str(int(curr) * int(d)))

        cond = condition(layer, target)

    print(oper if oper != 200 else -1)


solution()
