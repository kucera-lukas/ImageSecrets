import pytest
from pytest_mock import MockFixture


@pytest.mark.asyncio
async def test_get_session(mocker: MockFixture, async_context_manager):
    from imagesecrets.database import base

    begin = mocker.patch(
        "imagesecrets.database.base.async_sessionmaker.begin",
        return_value=async_context_manager,
    )

    async with base.get_session() as result:
        ...

    begin.assert_called_once_with()
    assert result is None
