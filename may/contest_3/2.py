def solution():
    n = int(input())

    for _ in range(n):
        m = input()
        inputs = [int(num) for num in input().split(' ')]
        inputs.sort()
        sum_ = sum(inputs)
        avg_ = sum_ / len(inputs)
        pair_count = 0
        l = 0
        r = len(inputs) - 1
        counts = {}
        for num in inputs:
            if num not in counts:
                counts[num] = 0
            counts[num] += 1

        while l < r:
            left_num = inputs[l]
            right_num = inputs[r]
            curr_avg = (sum_ - left_num - right_num) / (len(inputs) - 2)
            if curr_avg == avg_ and left_num in counts:
                if left_num == inputs[r]:
                    pair_count += (counts[left_num] * (counts[left_num] - 1)) / 2
                    del counts[left_num]
                else:
                    pair_count += counts[left_num] * counts[right_num]
                    del counts[left_num]
                    del counts[right_num]
                l += 1
            elif curr_avg < avg_:
                r -= 1
            else:
                l += 1
        print(int(pair_count))


solution()
