import os

def get_sizes(path):
    """
    Возвращает словарь, где ключами являются пути к файлам и директориям в корневой директории,
    а значениями — их размеры в байтах.

    :param path: Путь к корневой директории.
    :return: Словарь с путями и их размерами.
    """
    sizes = {}
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        if os.path.isfile(full_path):
            sizes[full_path] = os.path.getsize(full_path)
        elif os.path.isdir(full_path):
            sizes[full_path] = get_directory_size(full_path)
    return sizes

def get_directory_size(path):
    """
    Возвращает общий размер всех файлов в директории и её поддиректориях.

    :param path: Путь к директории.
    :return: Общий размер в байтах.
    """
    return sum(
        os.path.getsize(os.path.join(dirpath, filename))
        for dirpath, _, filenames in os.walk(path)
        for filename in filenames
    )

def print_sorted_sizes(sizes):
    """
    Выводит отсортированные по размеру пути к файлам и директориям.

    :param sizes: Словарь с путями и их размерами.
    """
    for path, size in sorted(sizes.items(), key=lambda x: x[1], reverse=True):
        print(f"{size} bytes - {path}")

if __name__ == "__main__":
    """
    Точка входа в программу. Получает размеры всех файлов и директорий
    в текущей директории и выводит их отсортированными по размеру.
    """
    current_directory = os.getcwd()
    sizes = get_sizes(current_directory)
    print_sorted_sizes(sizes)
