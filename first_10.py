from typing import List

# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    res = [0 for _ in range(len(nums))]

    for i, num in enumerate(nums):
        for comp in nums:
            if comp < num:
                res[i] += 1

    return res

# https://www.hackerrank.com/challenges/grading/problem
def gradingStudents(grades):
    for i, grade in enumerate(grades):
        if grade > 35 and grade % 5 >= 3:
            grades[i] += 5 - (grade % 5)

    return grades


# https://codeforces.com/problemset/problem/50/A
def fitdominos():
    inputs = [int(num) for num in input().split(' ')]
    print((inputs[0] * inputs[1]) // 2)


# https://practice.geeksforgeeks.org/problems/selection-sort/1
class SelectionSort:
    def select(self, arr, i):
        min_ind = i
        min = arr[i]
        for j in range(i, len(arr)):
            if arr[j] < min:
                min = arr[j]
                min_ind = j

        arr[i], arr[min_ind] = arr[min_ind], arr[i]

    def selectionSort(self, arr, n):
        for i, num in enumerate(arr):
            self.select(arr, i)

        return arr


# https://www.hackerrank.com/challenges/insertionsort1/problem
def insertionSort1(n, arr):
    num = arr[n - 1]
    n = n - 1
    while n > 0 and arr[n - 1] > num:
        arr[n] = arr[n - 1]
        n -= 1
        fake = [str(num) for num in arr]
        print(" ".join(fake))

    arr[n] = num
    fake = [str(num) for num in arr]
    print(" ".join(fake))


# https://www.hackerrank.com/challenges/countingsort1/problem
def countingSort(arr):
    counts = {}
    for i in range(0, 100):
        counts[i] = 0

    for num in arr:
        counts[num] += 1

    return counts.values()


# https://leetcode.com/problems/find-target-indices-after-sorting-array/
def targetIndices(nums: List[int], target: int) -> List[int]:
    target_indexes = []
    nums = sorted(nums)

    for i, num in enumerate(nums):
        if num == target:
            target_indexes.append(i)

    return target_indexes


# https://leetcode.com/problems/sorting-the-sentence/
def sortSentence(s: str) -> str:
    words = s.split(' ')
    content = {}
    for word in words:
        content[int(word[len(word) - 1])] = word[0: len(word) - 1]

    sentence = []
    for i in range(len(words)):
        sentence.append(content[i + 1])

    return " ".join(sentence)


print(sortSentence("is2 sentence4 This1 a3"))
