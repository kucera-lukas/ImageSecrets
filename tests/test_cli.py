"""Test the command line interface."""
import pytest
from click.testing import CliRunner

from image_secrets.cli import image_secrets


@pytest.fixture()
def runner() -> CliRunner:
    """Return the CLI runner instance."""
    return CliRunner()


def test_main(runner: CliRunner) -> None:
    result = runner.invoke(image_secrets)
    assert not result.exception


def test_encode(runner: CliRunner) -> None:
    result = runner.invoke(image_secrets, ["encode", "--help"])
    assert "inplace" in result.stdout


def test_encode_file(runner: CliRunner) -> None:
    result = runner.invoke(image_secrets, ["encode", "--filename", "image.png"])
    assert "Path 'image.png' does not exist." in result.stdout

    with runner.isolated_filesystem():
        with open("test.txt", "w") as f:
            f.write("testing...")

        result = runner.invoke(image_secrets, ["encode", "--filename", "test.txt"])
        assert "is not a .PNG image." in result.stdout


def test_decode(runner: CliRunner) -> None:
    result = runner.invoke(image_secrets, ["decode", "--help"])
    assert "Decode a message from <file>." in result.stdout
