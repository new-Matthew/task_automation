from pathlib import Path

root_dir = Path('files')
# iterando sobre os caminhos de todos os arq do diretório files
# file_paths = root_dir.iterdir()
# for path in file_paths:
#     print(path)
#     for filepath in path.iterdir():
#         print(filepath)
file_paths = root_dir.glob('**/*')
for path in file_paths:
    #print(path)
    if path.is_file():
        parent_folder = path.parts[-2]
        new_filename = f'{parent_folder}-{path.name}'
        new_filepath = path.with_name(new_filename)
        path.rename(new_filepath)