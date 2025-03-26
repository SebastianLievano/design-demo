from num_islands import num_islands
import json

def get_grade(tests):
    grade = 0
    for test in tests:
        weight = test['weight']
        if test['result'] == 'OK':
            grade += weight
        else:
            # Other results: 'TIMEOUT' 'INTERRUPT' 'SKIP' 'FAIL' 'EXPECTEDFAIL'
            #                'UNEXPECTEDPASS' 'ERROR'
            if weight == 0:
                grade = 0
                break
    return grade

grid_with_2 = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1]
]

grid_with_4 = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [1, 0, 0, 1, 1]
]

grid_with_0 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

all_islands = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

if __name__ == "__main__":
    # n, expected
    test_cases = [
        [grid_with_2, 2, 1, "public"],
        [grid_with_4, 4, 1, "public"],
        [grid_with_0, 0, 1, "private"],
        [all_islands, 1, 1, "hidden"]
    ]

    res = {}

    tests = []

    for grid, expected_result, weight, kind in test_cases:
        result = num_islands(grid)

        test = {}

        test['result'] = 'OK' if result == expected_result else 'FAIL'
        test['weight'] = weight
        test['kind'] = kind
        test['expected_result'] = expected_result
        test['actual_result'] = result

        tests.append(test)


    res['grade'] = get_grade(tests)
    res['tests'] = tests

    print(json.dumps(res))
