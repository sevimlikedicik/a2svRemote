def get_known_topic_count(topics, idx, knowledge, mentors):
    child_count = 1
    if idx in mentors:
        for child in mentors[idx]:
            c_count, known = get_known_topic_count(topics, child, knowledge, mentors)
            child_count += c_count

    for topic in knowledge[idx]:
        topics[topic] = child_count
    print(idx, child_count, topics)
    return child_count


def solution():
    inputs = [int(num) for num in input().split(' ')]
    n = int(inputs[0])
    m = int(inputs[1])
    mentors = [int(num) for num in input().split(' ')]
    del mentors[0]
    graph = {}
    for i, ment in enumerate(mentors):
        if ment not in graph:
            graph[ment] = []
        graph[ment].append(i + 1)

    knowledge = {}
    for i in range(n):
        arr = [int(num) for num in input().split(' ')]
        del arr[0]
        knowledge[i] = set(arr)

    topics = {}
    for i in range(m):
        topics[i] = 0

    get_known_topic_count(topics, 0, knowledge, graph)

    print(' '.join([str(val) for val in topics.values()]))


solution()
