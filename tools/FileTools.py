from pathlib import Path


def find_file(file_directory: str, file_name: str) -> list[str]:
    """
    Finds a file given a directory and file name

    Args:
        file_directory: The directory to search
        file_name: The file name

    Returns:
        String: File path

    """
    search_dir = Path(file_directory)
    text_file = [
        str(path) for path in search_dir.rglob(file_name)
    ]

    return text_file