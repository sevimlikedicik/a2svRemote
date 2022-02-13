from typing import List


def countStudents(students: List[int], sandwiches: List[int]) -> int:
    stu = [len(students) - sum(students), sum(students)]

    for sandwich in sandwiches:
        if stu[sandwich] == 0:
            return sum(stu)

        stu[sandwich] -= 1

    return 0
