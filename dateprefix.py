#!/usr/bin/env python

import sys
import os
import datetime
import pathlib
from pytz import timezone


class termcolor:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


tzlong = "America/Los_Angeles"
tz = "PDT"


def getTimeStamp(file_name, date_format="%y%m%d %H%M%S"):
    name = pathlib.Path(file_name)
    return (
        tz
        + " "
        + datetime.datetime.fromtimestamp(
            name.stat().st_mtime, timezone(tzlong)
        ).strftime(date_format)
    )


def run():
    for file in sys.argv[1:]:
        normalized_path = os.path.abspath(file)
        if not pathlib.Path(normalized_path).exists():
            print(termcolor.FAIL + "× " + termcolor.ENDC + normalized_path)
            continue
        basename = os.path.basename(normalized_path)
        dirname = os.path.dirname(normalized_path)
        timestamp = getTimeStamp(file)
        print(
            termcolor.OKGREEN
            + "✓ "
            + termcolor.ENDC
            + dirname
            + "/"
            + termcolor.OKGREEN
            + timestamp
            + termcolor.ENDC
            + " "
            + basename
        )
        os.rename(normalized_path, dirname + "/" + timestamp + " " + basename)
