def number_generator(limit):
    number = 0
    while number < limit:
        yield number
        number += 1


for n in number_generator(3):
    print(n)

my_list = list(number_generator(10))
print(my_list)


def even_number_generator(limit):
    number = 0
    while number < limit:
        if number % 2 == 0:
            yield number
        number += 1


for n in even_number_generator(100):
    print(n, end=" ")
print()


# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
def fibonacci_generator(sequence_length):
    a, b = 0, 1
    count = 0
    while count < sequence_length:
        yield a
        a, b = b, a + b
        count += 1


for fib_n in fibonacci_generator(20):
    print(fib_n, end=" ")


def file_line_reader(file_name):
    with open(file_name, "r", encoding="utf-8") as file_object:
        for line in file_object:
            yield line.strip()


for line in file_line_reader("sample.txt"):
    print(line)

import random


def random_even_number_generator(limit, low, high):
    count = 0
    while count < limit:
        random_number = random.randint(low, high)
        if random_number % 2 == 0:
            yield random_number
        else:
            continue
        count += 1


for number in random_even_number_generator(30, 100, 999):
    print(number, end=" ")
print()


def shuffled_sequence_generator(*sequences):
    combined_seq = []
    for sequence in sequences:
        combined_seq += sequence

    random.shuffle(combined_seq)

    for element in combined_seq:
        yield element


seq1 = [123, 3232, 434, 55, 22]
seq2 = [76, 67, 25, 52]
seq3 = [x for x in range(10000, 11000, 13)]

for number in shuffled_sequence_generator(seq1, seq2, seq3):
    print(number, end=" ")
print()


import requests


def download_lines(url, max_line):
    response = requests.get(url, stream=True)
    response.raise_for_status()

    line_count = 0
    for line in response.iter_lines(decode_unicode=True):
        if line_count >= max_line:
            break
        yield line
        line_count += 1


my_url = "https://en.wikipedia.org/wiki/Turkey"
max_line_to_download = 10

for url_line in download_lines(my_url, max_line_to_download):
    print("[LINE]", url_line)
