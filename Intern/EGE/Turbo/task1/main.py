def search_expression(string: str) -> int:
    allowed_operations = ['+', '/', '-', '*']
    length = len(string)
    answer = 0
    count = 0
    for index in range(1, length - 1):
        if string[index] in allowed_operations and \
                string[index - 1] in allowed_operations:
            count = 0
        elif string[index] in allowed_operations and \
                string[index + 1] in allowed_operations:
            count += 1
            answer = max(count, answer)
            count = 0
        else:
            count += 1
            answer = max(count, answer)
    return answer


def main():
    string = open('75607_35594199913785041_doc.txt').readline()
    string = '+' + string + '+'
    return search_expression(string)


if __name__ == "__main__":
    print(main())
