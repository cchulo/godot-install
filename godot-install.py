#!/usr/bin/env python3

import argparse
import platform
import re
import urllib.request

supported_systems = {
    "Linux": "linux"
}

cache_paths = {
    "Linux": "~/.cache/godot-install"
}

default_url = "https://downloads.tuxfamily.org/godotengine/"


def construct_parser() -> argparse.ArgumentParser:
    arg_parser = argparse.ArgumentParser(
        prog='godot-install',
        description='CLI tool for installing/managing Godot Engine'
    )

    return arg_parser


def fetch_versions():
    contents = str(urllib.request.urlopen(url=default_url).read())
    row_pattern = r"(<tr>(.+?)<\/tr>)+"
    metadata_pattern = r'<td class="n"><a href=".+\/">(?P<Version>\d(.\d)+)<\/a>\/<\/td><td class="m">(.+)<\/td>' \
                       r'<td class="s">.+$'
    rows = re.findall(row_pattern, contents)
    for row in rows:
        result = re.search(metadata_pattern, row[1])
        if result is None:
            continue
        print(result.groupdict())


def get_godot_versions():
    pass


def get_godot_binaries():
    pass


def get_os_and_arch():
    system = platform.system()
    arch = platform.architecture()


if __name__ == '__main__':
    parser = construct_parser()
    parser.parse_args()
    fetch_versions()
