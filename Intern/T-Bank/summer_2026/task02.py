def solution():
    input_string = input().strip()
    length = len(input_string)

    leading_a_count = 0
    while leading_a_count < length and input_string[leading_a_count] == 'a':
        leading_a_count += 1

    if leading_a_count == length:
        return "Yes"

    trailing_a_count = 0
    while trailing_a_count < length and input_string[length - 1 - trailing_a_count] == 'a':
        trailing_a_count += 1

    if leading_a_count > trailing_a_count:
        return "No"

    middle_part = input_string[leading_a_count: length - trailing_a_count]

    if middle_part == middle_part[::-1]:
        return "Yes"
    else:
        return "No"


if __name__ == '__main__':
    print(solution())
