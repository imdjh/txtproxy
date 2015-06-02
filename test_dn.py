#!/usr/bin/env python
# coding=utf-8
# Test specified domain names
# ver 0.1.0
# Author: dye Jarhoo

import txtproxy
import unittest


class dnTestCase(unittest.TestCase):
    def setUp(self):
        self.app = txtproxy.app.test_client()

    def tearDown(self):
        pass

    def test_index(self):
        rv = self.app.get('/', follow_redirects=False)
        assert 'Not Found' in rv.data

    # invalid tests
    def test_tp_invalidDN_singleDot(self):
        rv = self.app.get('/tp/.', follow_redirects=False)
        assert 'Bad Request' in rv.data

    def test_tp_invalidDN_doubleDot(self):
        rv = self.app.get('/tp/..', follow_redirects=False)
        assert 'Bad Request' in rv.data

    def test_tp_invalidDN_TDLWithDot(self):
        rv = self.app.get('/tp/c.', follow_redirects=False)
        assert 'Bad Request' in rv.data

    def test_tp_invalidDN_TDL(self):
        rv = self.app.get('/tp/c', follow_redirects=False)
        assert 'Bad Request' in rv.data

    def test_tp_invalidDN_noDomain(self):
        rv = self.app.get('/tp/.cc.', follow_redirects=False)
        assert 'Bad Request' in rv.data

    # valid tests
    def test_tp_validDN_trailingspace(self):
        rv = self.app.get('/tp/example.cn   ', follow_redirects=False)
        assert 'Not Found' in rv.data

    def test_tp_validDN_trailngDoubleDot(self):
        rv = self.app.get('/tp/example.cn..', follow_redirects=False)
        assert 'Not Found' in rv.data

    def test_tp_validDN_trailingDot(self):
        rv = self.app.get('/tp/never-does-eexxcc.cc.', follow_redirects=False)
        assert 'Not Found' in rv.data

    def test_tp_validDN_subdomain(self):
        rv = self.app.get('/tp/aa.bb.cc', follow_redirects=False)
        assert 'Not Found' in rv.data

    def test_tp_validDN_inRealWorld(self):
        rv = self.app.get('/tp/espresso.djh.im', follow_redirects=False)
        assert 'refresh' in rv.data





if __name__ == '__main__':
    unittest.main()
