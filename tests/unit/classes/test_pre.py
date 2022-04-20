from bifu.classes.pre import PreCommit, PrePush


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                                            P R E    C O M M I T
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def test_pre_commit_object():
    pre_commit = PreCommit()
    assert pre_commit


def test_pre_commit_hook_name():
    pre_commit = PreCommit()
    assert pre_commit.hook_name == 'pre-commit'


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#                                            P R E    P U S H
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def test_pre_push_object():
    pre_push = PrePush()
    assert pre_push


def test_pre_push_hook_name():
    pre_push = PrePush()
    assert pre_push.hook_name == 'pre-push'
