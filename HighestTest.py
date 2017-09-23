import unittest

from HighestScore import read_file
from model.LinkedList import LinkedList


def get_zero():
    return {'id': 'myZeroScore', 'score': 0}


def get_small():
    return {'id': 'mySmallScore', 'score': 1234}


def get_medium():
    return {'id': 'myMediumScore', 'score': 4321}


def get_large():
    return {'id': 'myLargeScore', 'score': 420000}


def get_jumbo():
    return {'id': 'myJumboScore', 'score': 2**31 - 1}


def get_ascending_list():
    return [get_zero(), get_small(), get_medium(), get_large(), get_jumbo()]


def get_descending_list():
    return [get_jumbo(), get_large(), get_medium(), get_small(), get_zero()]


def get_random_list():
    return [get_medium(), get_large(), get_zero(), get_jumbo(), get_small()]


class HighestTester(unittest.TestCase):
    def test_read_file_no_file(self):
        with self.assertRaises(SystemExit) as ec:
            read_file('not a file.txt')
        self.assertEqual(ec.exception.code, 1)

    def test_read_file_no_id(self):
        with self.assertRaises(SystemExit) as ec:
            read_file('resources/noID.txt')
        self.assertEqual(ec.exception.code, 2)

    def test_read_file_bad_json(self):
        with self.assertRaises(SystemExit) as ec:
            read_file('resources/badJSON.txt')
        self.assertEqual(ec.exception.code, 2)

    def test_read_file_bad_score(self):
        with self.assertRaises(SystemExit) as ec:
            read_file('resources/badScore.txt')
        self.assertEqual(ec.exception.code, 2)

    def test_read_file_no_score(self):
        with self.assertRaises(SystemExit) as ec:
            read_file('resources/noScore.txt')
        self.assertEqual(ec.exception.code, 2)

    def test_read_file_good_file(self):
        with self.assertRaises(SystemExit) as ec:
            read_file('resources/goodFile.txt')
        self.assertEqual(ec.exception.code, 0)

    def test_read_file_blank_line(self):
        with self.assertRaises(SystemExit) as ec:
            read_file('resources/blankLine.txt')
        self.assertEqual(ec.exception.code, 0)

    def test_linkedlist_insert_descending(self):
        lst = LinkedList()
        scores = get_ascending_list()
        lst.insert_in_descending_order(scores[1])
        self.assertEqual(lst.get_as_list()[0]['id'], scores[1]['id'])
        self.assertEqual(lst.get_as_list()[0]['score'], scores[1]['score'])

    def test_ascending_order(self):
        lst = LinkedList()
        asc = get_ascending_list()
        correct = get_descending_list()
        for score in asc:
            lst.insert_in_descending_order(score)
        self.assertEqual(lst.get_as_list(), correct)

    def test_descending_order(self):
        lst = LinkedList()
        asc = get_descending_list()
        correct = get_descending_list()
        for score in asc:
            lst.insert_in_descending_order(score)
        self.assertEqual(lst.get_as_list(), correct)

    def test_random_order(self):
        lst = LinkedList()
        asc = get_random_list()
        correct = get_descending_list()
        for score in asc:
            lst.insert_in_descending_order(score)
        self.assertEqual(lst.get_as_list(), correct)
