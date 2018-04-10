import re
import serverAPI


def check_add():
    url = serverAPI()
    countBefr = count_all(url.showAll().text)
    # add is not used after assignment
    add = url.add('name', 'position')
    countAftr = count_all(url.text)[0]
    assert countBefr != countAftr


def check_show_id():
    url = serverAPI()
    add = url.add('name', 'position')
    show = url.showId(find_id(add.text))[0]
    url.delete(find_id(add.text)[0])
    assert find_id(add.text)[0] == find_id(show.text)[0]

def test_check_delete():
     url = serverAPI()
     add = url.add('name', 'position')
     idAdd = url.find_id(add.text)[0]
     url.delete(idAdd)
     result = url.find_id(url.showAll().text)[0]
     for i in range(len(result)):
      assert idAdd != result[i]

def find_id(myStr):
    patern = re.compile('.id.:.(\d*).')
    result = patern.search(myStr).groups()
    return result


def count_all(myStr):
    patern = re.compile('.id.:[\d]*')
    count = len(patern.findall(str(myStr)))
    return count