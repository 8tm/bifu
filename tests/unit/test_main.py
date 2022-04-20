def test_application_name_from_package_configuration(package, application_name_candidate):
    assert package.name == application_name_candidate
