from pathlib import Path

root_dir = Path('files\dados')
file_paths = root_dir.iterdir()

for path in file_paths:
    new_filename = f'new-{path.stem}{path.suffix}'
    print(new_filename)
    new_file_path = path.with_name(new_filename)
    print(new_file_path)
    path.rename(new_file_path)
    