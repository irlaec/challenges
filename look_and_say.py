def generate_look_and_say_seq(num_elements):
    sequence = ["1"]
    for i in range(1, num_elements):
        occurrences = 1
        next_num = ""
        current_num = sequence[i - 1]
        for j, digit in enumerate(current_num):
            if j == len(current_num) - 1:
                next_num += str(occurrences) + digit
                sequence.append(next_num)
            elif digit != current_num[j + 1]:
                next_num += str(occurrences) + digit
                occurrences = 1
            else:
                occurrences += 1
    return sequence


if __name__ == "__main__":
    a = generate_look_and_say_seq(30 + 1)
    print(f"The length of the element at position 30 is {len(a[30])}")
