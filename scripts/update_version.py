"""Simple CLI tool to update version of the application."""
from __future__ import  annotations

import argparse
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from argparse import ArgumentParser

BASE = Path(__file__).parent.parent
PYPROJECT_PATH = BASE / 'pyproject.toml'
INIT_PATH = BASE / 'image_secrets/__init__.py'


def update_line_in_file(file: Path, line_start: str, new_value: str) -> None:
    with file.open() as input:
        lines = input.readlines()

    with file.open(mode='w') as output:
        for line in lines:
            if line.startswith(line_start):
                output.write(f'{line_start}{new_value}\n')
            else:
                output.write(line)


def get_parser() -> ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'version',
        type=str,
        help='new application version to set in all configuration files',
    )
    return parser


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()

    version = args.version
    update_line_in_file(PYPROJECT_PATH, 'version = ', f'"{version}"')
    update_line_in_file(INIT_PATH, '__version__ = ', f'"{version}"')
