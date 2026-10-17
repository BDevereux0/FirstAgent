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
    #don't put .* searches like name.pdf won't work with the type added
    files = (p.rglob('*' + file_name + '*'))
    file_output = [str(f) for f in files]
    return file_output

def read_file(file_name:str, file_path:str):
    """

    Reads a file

    Args:
        file_name: The file name
        file_path: The file path to read the file
    Returns:

    """
    file = Path(file_path + file_name)
    content = file.read_text(encoding="utf-8")
    print(content)







