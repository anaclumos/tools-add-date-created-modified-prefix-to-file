import sys
import os
import datetime
import pathlib


def getTimeStamp(file_name, date_format="%y%m%d"):
    name = pathlib.Path(file_name)
    assert name.exists(), f'No such file: {name}'
    return datetime.date.fromtimestamp(name.stat().st_mtime).strftime(date_format)


for file in sys.argv[1:]:
    normalized_path = os.path.normpath(file)
    basename = os.path.basename(normalized_path)
    dirname = os.path.dirname(normalized_path)
    timestamp = getTimeStamp(file)
    print(normalized_path)
    print(basename)
    print(dirname)
    os.rename(normalized_path, dirname + '/' + timestamp + ' ' + basename)
