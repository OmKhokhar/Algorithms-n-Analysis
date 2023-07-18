import random


def make_set(data_set, size, file_name):
    entries = list()
    with open(data_set, 'r') as data:
        for entry in data:
            entries.append(entry)

    random_set = random.choices(entries, k=size)
    write_file = ""
    for element in random_set:
        write_file = write_file + element

    with open(f"data/{file_name}.txt", 'w') as file:
        file.write(write_file)


if __name__ == '__main__':
    sizes = [10, 50, 500, 1000, 5000, 10000, 50000, 100000, 200000]
    for size in sizes:
        make_set(data_set='sampleData200k.txt', size=size,
                 file_name="data" + str(size if size < 1000 else f"{int(size / 1000)}k"))
