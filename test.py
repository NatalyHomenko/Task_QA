from serverAPI import ServerAPI
import testHelper

success = 200
failed = 400
added = 201

def setup_module():
    pass


def teardown_module():
    pass


# ShowAll
def test_show_all():
    url = ServerAPI()
    assert success == url.showAll().status_code


# ShowId

def test_show_id_1():
    url = ServerAPI()
    assert success == url.showId(1101).status_code


def test_show_id_2():
    url = ServerAPI()
    assert success == url.showId(1092).status_code


def test_show_id_3():
    url = ServerAPI()
    assert success == url.showId(1654).status_code


# Add

def test_add_1():
    url = ServerAPI()
    name = ''
    position = ''
    actual = url.add(name, position)
    assert added == actual.status_code


def test_add_2():
    url = ServerAPI()
    name = 'Nataly'
    position = 'QA_intern'
    actual = url.add(name, position)
    assert added == actual.status_code


def test_add_3():
    url = ServerAPI()
    name = 'Sam'
    position = 'developer'
    actual = url.add(name, position)
    assert added == actual.status_code

def test_add_4():
    url = ServerAPI()
    name = 'Emily'
    position = 'tester'
    actual = url.add(name,position, headers = None)
    assert failed == actual.status_code


#  Delete

def test_delete_1():
    url = ServerAPI()
    assert success != url.delete(' ').status_code


def test_delete_2():
    url = ServerAPI()
    assert success != url.delete("z").status_code


def test_delete_3():
    url = ServerAPI()
    assert success != url.delete('').status_code


