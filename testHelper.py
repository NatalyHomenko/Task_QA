import re
import serverAPI


def find_id(myStr):
    patern = re.compile('.id.:.(\d*).')
    result = patern.search(myStr).groups()
    return result


def count_all(myStr):
    patern = re.compile('.id.:[\d]*')
    count = len(patern.findall(str(myStr)))
    return count