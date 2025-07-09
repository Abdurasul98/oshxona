from core.file_manager import CSVFileManager


def get_next_id(filename: str):
    all_rows = CSVFileManager(filename).read()
    if all_rows:
        return int(all_rows[-1][0]) + 1
    return 1