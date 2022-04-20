import pytest

from bifu.main import parse_arguments, PackageConfiguration


@pytest.fixture
def parser():
    return parse_arguments()


@pytest.fixture
def install():
    return 'pre-commit'


@pytest.fixture
def application_name_candidate():
    package = PackageConfiguration()
    return package.name


@pytest.fixture
def package():
    package = PackageConfiguration()
    return package
