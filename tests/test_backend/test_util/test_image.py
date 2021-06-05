"""Test the image_util module."""
from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest

from image_secrets.backend.util.image import data, png_filetype, read_bytes, save_array


@pytest.mark.parametrize(
    "bytes_",
    [b"", b"qwerty", b"123456789", b"~!@#$%^&**()", b"   <>   "],
)
def test_read_bytes(bytes_: bytes) -> None:
    """Test the read_image_bytes function.

    :param bytes_: Bytes to read

    """
    assert read_bytes(bytes_).read(5) == bytes_[:5]


def test_data(test_image_path: Path) -> None:
    """Test the image_data function."""
    shape, arr = data(test_image_path)

    assert arr.ndim == 3
    assert arr.dtype == np.uint8
    assert np.logical_and(arr >= 0, arr <= 255).all()

    assert shape[-1] == 3


def test_save(tmpdir, test_image_array) -> None:
    """Test the save function."""
    tmp_dir = Path(tmpdir.mkdir("tmp/"))

    fp = save_array(test_image_array, image_dir=tmp_dir)
    assert fp.is_file()


def test_png_filetype(test_image_path) -> None:
    """Test the png_filetype function."""
    with open(test_image_path, mode="rb") as image_data:
        result = png_filetype(image_data.read())
    assert result


def test_png_filetype_fail() -> None:
    """Test that png_filetype returns False if not a png file is passed in."""
    with open(Path(__file__), mode="rb") as image_data:
        result = png_filetype(image_data.read())
    assert not result
