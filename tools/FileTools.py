from pathlib import Path


def find_file(file_name: str) -> list[str]:
    """
    Finds a file given a file name

    Args:
        file_name: The file name

    Returns:
        String: File path

    """
    #__file__ means start at this file location in the file tree
    p = Path(__file__).resolve().parent.parent
    print(p.resolve())
    files = (p.glob('*' + file_name + '*' + '.*'))
    file_output = [str(f) for f in files]
    return file_output





