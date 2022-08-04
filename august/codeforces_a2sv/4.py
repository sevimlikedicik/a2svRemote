from sys import stdin

input = stdin.readline


def solution():
    n = int(input())

    for _ in range(n):
        size, count = [int(num) for num in input().split(' ')]
        s = input()
        transformations = {'a': 'a'}
        i = 0
        while count > 0 and i < size and len(transformations.keys()) != 26:
            c = s[i]
            while count > 0 and c != 'a':
                go_down = min(count, ord(c) - ord('a'))
                final_letter = chr(ord(c) - go_down)
                if final_letter in transformations:
                    final_letter = transformations[final_letter]
                    curr_pos = ord(c)
                    while chr(curr_pos) not in transformations:
                        count -= 1
                        curr_pos -= 1
                else:
                    count -= go_down
                for j in range(go_down):
                    transformations[c] = final_letter
                    c = chr(ord(c) - 1)
            i += 1

        for k, v in transformations.items():
            s = s.replace(k, v)

        print(s)


solution()
