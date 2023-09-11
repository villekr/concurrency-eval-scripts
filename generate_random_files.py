import os
import random
import string


def generate_random_files(
    subfolder: str,
    num_files: int,
    min_size: int,
    max_size: int,
    prefix: str,
    magic_string: str,
):
    os.makedirs(subfolder, exist_ok=True)

    magic_index = random.randint(0, num_files)
    prefix_len = len(f"{num_files}")
    for i in range(num_files):
        file_name = f"{prefix}_{str(i + 1).zfill(prefix_len)}.txt"
        file_path = os.path.join(subfolder, file_name)

        file_size = random.randint(min_size, max_size)
        if i == magic_index:
            print(f"Magic file! {file_name=}")
            file_content = generate_random_content(file_size, magic_string)
        else:
            file_content = generate_random_content(file_size)

        with open(file_path, "w") as file:
            file.write(file_content)


def generate_random_content(size, magic_word=None):
    content = "".join(random.choices(string.ascii_letters, k=size))
    if magic_word is not None:
        index = random.randint(0, len(content))
        content = content[:index] + magic_word + content[index:]
    return content


if __name__ == "__main__":
    number_of_files = 1000
    min_size = 1000
    max_size = 50000
    sub_folder = f".temp/{number_of_files}"
    prefix = "myprefix"
    magic_string = "MyMagicString"
    print(f"Generating random files: {number_of_files=} {min_size=} {max_size=}")

    generate_random_files(
        sub_folder, number_of_files, min_size, max_size, prefix, magic_string
    )
