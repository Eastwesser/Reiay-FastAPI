import pytest
from celery.celery import add


@pytest.mark.celery
def test_add():
    result = add.apply_async((4, 6))
    assert result.get(timeout=10) == 10
