from core.file_manager import FileManager


def get_next_id(filename: str):
    all_rows = FileManager(filename).read()
    if all_rows:
        return int(all_rows[-1][0]) + 1
    return 1