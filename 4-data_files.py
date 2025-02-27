from pathlib import Path
from datetime import datetime

path = Path('files', 'dados2', 'dados2-test.txt')

stats = path.stat()
second_created = stats.st_birthtime
date_created = datetime.fromtimestamp(second_created)
date_created_str = date_created.strftime('%Y-%m-%d_%H_%M_%S')
print(date_created_str)