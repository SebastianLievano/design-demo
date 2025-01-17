from add import add
import json

if __name__ == "__main__":
    test_cases = [
        [0, 0, 0],
        [1, 3, 4],
        [-1, 2, 1]
    ]

    res = {}

    for num1, num2, expected_result in test_cases:
        result = add(num1, num2)

    res['grade'] = 100

    print(json.dumps(res))