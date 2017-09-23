import json
import re
import sys
from json import JSONDecodeError

from model.LinkedList import LinkedList


def read_file(score_file):
    score_list = LinkedList()
    try:
        read = open(score_file, 'r')
        for line in read:
            if not re.match('\n', line):
                try:
                    score_list.insert_in_descending_order(validate_score_and_id(line))
                except (JSONDecodeError, KeyError, ValueError):
                    read.close()
                    sys.exit(2)
        read.close()
    except FileNotFoundError:
        sys.exit(1)

    sorted_list = score_list.get_as_list()
    print(json.dumps(sorted_list, indent=4))
    sys.exit(0)


def validate_score_and_id(record):
    split_record = record.split(':', 1)
    if not re.match('[0-9]+', split_record[0]):
        raise ValueError
    id_dict = json.loads(split_record[1])
    return {'score': split_record[0], 'id':id_dict['id']}


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file = sys.argv[1]
    else:
        file = 'tests.txt'
    read_file(file)
