import sys
import math
import json

def solve_from_lines(lines):
    it = iter(lines)
    try:
        T = int(next(it).strip())
    except StopIteration:
        return []

    outputs = []
    for _ in range(T):
        try:
            X = int(next(it).strip())
        except StopIteration:
            break
        k = (math.isqrt(1 + 4*X) - 1) // 2
        outputs.append(str(X - k))
    return outputs

def main():
    # Default test files (can be overridden via CLI args)
    input_path = "/home/jain/Downloads/tc1/in1.txt"
    expected_path = "/home/jain/Downloads/tc1/out1.txt"
    if len(sys.argv) >= 2:
        input_path = sys.argv[1]
    if len(sys.argv) >= 3:
        expected_path = sys.argv[2]

    with open(input_path, 'r') as f:
        in_lines = [ln.rstrip('\n') for ln in f]

    with open(expected_path, 'r') as f:
        expected_lines = [ln.rstrip('\n') for ln in f if ln.strip() != ""]

    outputs = solve_from_lines(in_lines)

    correct_count = 0
    incorrect_instances = []

    for i, out in enumerate(outputs):
        expected = expected_lines[i].strip() if i < len(expected_lines) else ""
        if out.strip() == expected:
            correct_count += 1
        else:
            # input for this test case is the (i+1)-th line after the T line
            case_input = in_lines[i+1].strip() if (i+1) < len(in_lines) else ""
            incorrect_instances.append({
                "in": case_input,
                "correct_output": expected,
                "your_output": out
            })

    incorrect_count = len(outputs) - correct_count

    # Print program outputs (one per line) followed by the summary
    for o in outputs:
        print(o)

    print()
    print("correct_count:", correct_count)
    print("incorrect_count:", incorrect_count)
    print("Dumping incorrect_instances...")

    with open('/home/jain/Downloads/report.json', 'w') as f:
        json.dump(incorrect_instances, f, indent=2)
    print("Report generated.")
    # print(json.dumps(incorrect_instances, indent=2))

if __name__ == '__main__':
    main()

