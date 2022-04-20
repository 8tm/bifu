import argparse

import pytest


def test_parse_arguments_basics(parser, install):
    arguments = parser.parse_args(['--install', 'pre-commit'])

    assert arguments == argparse.Namespace(
        init=False,
        install=install,
        number=0,
        run=None,
        uninstall=None,
    )


@pytest.mark.parametrize(
    'init, install, number, run, uninstall',
    [
        (False, 'pre-commit', 0, None, None),
        (False, 'pre-push', 0, None, None),
    ],
    ids=['pre-commit installation', 'pre-push installation'],
)
def test_parse_arguments_install_options(parser, init, install, number, run, uninstall):
    arguments = parser.parse_args(['--install', install])

    assert arguments == argparse.Namespace(
        init=init,
        install=install,
        number=number,
        run=run,
        uninstall=uninstall,
    )


@pytest.mark.parametrize(
    'init, install, number, run, uninstall',
    [
        (False, None, 0, None, 'pre-commit'),
        (False, None, 0, None, 'pre-push'),
    ],
    ids=['pre-commit uninstallation', 'pre-push uninstallation'],
)
def test_parse_arguments_uninstall_options(parser, init, install, number, run, uninstall):
    arguments = parser.parse_args(['--uninstall', uninstall])

    assert arguments == argparse.Namespace(
        init=init,
        install=install,
        number=number,
        run=run,
        uninstall=uninstall,
    )


def generate_numbers():
    stages = []
    for value in (0, 1, 2, 10, 100):
        for stage in ('pre-commit', 'pre-push'):
            stages.append((False, None, str(value), stage, None))
    return stages


@pytest.mark.parametrize(
    'init, install, number, run, uninstall',
    [
        *generate_numbers(),
    ],
)
def test_parse_arguments_run_options(parser, init, install, number, run, uninstall):
    arguments = parser.parse_args(['--run', run, '--number', number])

    assert arguments == argparse.Namespace(
        init=init,
        install=install,
        number=int(number),
        run=run,
        uninstall=uninstall,
    )
