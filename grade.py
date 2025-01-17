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
    # num1, num2, expected_result, weight
    test_cases = [
        [0, 0, 0, 0.25],
        [1, 3, 4, 0.25],
        [-1, 2, 1, 0.25],
        [5, 2, 7, 0.25]
    ]

    res = {}

    tests = []

    for num1, num2, expected_result, weight in test_cases:
        result = add(num1, num2)

        test = {}

        test['result'] = 'OK' if result == expected_result else 'FAIL'
        test['weight'] = weight

        tests.append(test)


    res['grade'] = get_grade(tests)
    res['tests'] = tests

    print(json.dumps(res))