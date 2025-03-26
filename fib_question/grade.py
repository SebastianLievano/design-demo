from add import add
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

if __name__ == "__main__":
    # n, expected
    test_cases = [
        [1, 0, "public"],
        [4, 2, "public"],
        [6, 5, "private"],
        [2, 1, "hidden"]
    ]

    res = {}

    tests = []

    for num1, num2, expected_result, weight, kind in test_cases:
        result = add(num1, num2)

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
