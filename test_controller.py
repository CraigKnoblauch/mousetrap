from controller import Controller

ctl = Controller()

def test_selectRoster():
    assert ctl.selectRoster(1)

# TODO, uhhhh, I don't know how to test this thing without maybe mock objects?