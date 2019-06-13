# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest

from pygments import highlight
from pygments.lexers import get_lexer_for_filename
from pygments.formatters import get_formatter_by_name


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.lexer = get_lexer_for_filename('pybemolle.lexers.py', stripall=True)
        cls.formatter = get_formatter_by_name('html', style='bemolle',
                                              cssclass='bemolle')

    def highlight(self, s):
        return highlight(s, self.lexer, self.formatter).replace('\n', '')

    def test_becuadro_major_latin_chords(self):
        result = self.highlight('C D E F G A H')

        self.assertEqual(
            '<div class="bemolle">'
            '<pre>'
            '<span></span>'
            '<span class="c">C</span> '
            '<span class="d">D</span> '
            '<span class="e">E</span> '
            '<span class="f">F</span> '
            '<span class="g">G</span> '
            '<span class="a">A</span> '
            '<span class="b">H</span>'
            '</pre>'
            '</div>',
            result
        )


if __name__ == '__main__':
    unittest.main()
