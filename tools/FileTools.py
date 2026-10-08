from pathlib import Path


def find_file(file_name: str) -> list[str]:
    """
    Finds a file given a file name

    Args:
        file_name: The file name

    Returns:
        String: File path

    """
    p = Path('.')
    print(p.resolve())
    files = (p.glob('*' + file_name + '*' + '.*'))
    file_output = [str(f) for f in files]
    return file_output



