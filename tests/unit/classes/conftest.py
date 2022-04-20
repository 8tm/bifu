from munch import DefaultMunch  # type: ignore
import pytest


@pytest.fixture
def prepare_user_configuration():

    return DefaultMunch.fromDict(
        {
            'pre-commit': {
                'master': {},
                'main': {},
                '': {},
            },
            'pre-push': {},
            'tasks': {},
            'theme': {},
        },
    )
