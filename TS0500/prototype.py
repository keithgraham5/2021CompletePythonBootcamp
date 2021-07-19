
import glob
from pathlib import Path

src_path = Path.cwd() /'input_folder'
print(src_path)

def inventory_files_to_process(folder):
    """
    loop Returns a list of filepaths

    :parameter
        source_folder: root directory to search

    :returns
        files_for_processing : list of filepath to .csv/.txt./.tsv files in
        directory
    """
    extension = [".txt", ".tsv", ".csv"]
    filepaths = [path for path in folder.glob(f"*{extension}")]
    return filepaths

filepaths = inventory_files_to_process(src_path)
