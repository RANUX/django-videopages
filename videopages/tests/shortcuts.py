# -*- coding: UTF-8 -*-
from unittest.case import TestCase
from videopages.shortcuts import create_paginated_page


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class ShortcutsTestCase(TestCase):

    def setUp(self):
        self.objects = ['john', 'paul', 'george', 'ringo']
        self.OBJECTS_PER_PAGE = 2
        self.PAGE_NUMBER = 1

    def test_create_paginator(self):
        page = create_paginated_page(query_set=self.objects, page_number=self.PAGE_NUMBER, objects_per_page=self.OBJECTS_PER_PAGE)
        self.assertEqual(len(self.objects), page.paginator.count)
        self.assertEqual(self.PAGE_NUMBER, page.number)

    def test_wrong_page_number(self):
        page = create_paginated_page(query_set=self.objects, page_number='JDJDJD', objects_per_page=self.OBJECTS_PER_PAGE)
        self.assertEqual(self.PAGE_NUMBER, page.number)

    def test_empty_page(self):
        page = create_paginated_page(query_set=[], page_number=10000, objects_per_page=self.OBJECTS_PER_PAGE)
        self.assertEquals(1, page.paginator.num_pages)