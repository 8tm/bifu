from bifu.classes.config import GitConfiguration, PackageConfiguration


def test_git_configuration_object():
    git_configuration = GitConfiguration()
    assert git_configuration


def test_package_configuration():
    package_configuration = PackageConfiguration()
    assert package_configuration
