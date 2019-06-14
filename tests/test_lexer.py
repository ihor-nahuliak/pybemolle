# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import os

from pygments import highlight
from pygments.lexers import load_lexer_from_file
from pygments.formatters import get_formatter_by_name


class TestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        root_path = os.path.dirname(os.path.dirname(__file__))
        lexer_filename = os.path.join(root_path, 'pybemolle', 'lexers.py')
        cls.lexer = load_lexer_from_file(lexer_filename,
                                         lexername='BemolleLexer',
                                         stripall=True)
        cls.formatter = get_formatter_by_name('html', style='bemolle')

    def highlight(self, s):
        return highlight(s, self.lexer, self.formatter).replace('\n', '')

    def test_becuadro_major_latin_chords(self):
        result = self.highlight(':: C D E F G A H')

        self.assertEqual(
            '<div class="highlight">'
            '<pre>'
            '<span></span>'
            '<span class="kn">::</span> '
            '<span class="mus-c mus-maj">C</span> '
            '<span class="mus-d mus-maj">D</span> '
            '<span class="mus-e mus-maj">E</span> '
            '<span class="mus-f mus-maj">F</span> '
            '<span class="mus-g mus-maj">G</span> '
            '<span class="mus-a mus-maj">A</span> '
            '<span class="mus-b mus-maj">H</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_becuadro_minor_latin_chords(self):
        result = self.highlight(':: Cm Dm Em Fm Gm Am Hm')

        self.assertEqual(
            '<div class="highlight">'
            '<pre>'
            '<span></span>'
            '<span class="kn">::</span> '
            '<span class="mus-c mus-min">Cm</span> '
            '<span class="mus-d mus-min">Dm</span> '
            '<span class="mus-e mus-min">Em</span> '
            '<span class="mus-f mus-min">Fm</span> '
            '<span class="mus-g mus-min">Gm</span> '
            '<span class="mus-a mus-min">Am</span> '
            '<span class="mus-b mus-min">Hm</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_bemole_major_latin_chords(self):
        result = self.highlight(':: Cb Db Eb Fb Gb Ab B')

        self.assertEqual(
            '<div class="highlight">'
            '<pre>'
            '<span></span>'
            '<span class="kn">::</span> '
            '<span class="mus-cb mus-maj">Cb</span> '
            '<span class="mus-db mus-maj">Db</span> '
            '<span class="mus-eb mus-maj">Eb</span> '
            '<span class="mus-fb mus-maj">Fb</span> '
            '<span class="mus-gb mus-maj">Gb</span> '
            '<span class="mus-ab mus-maj">Ab</span> '
            '<span class="mus-bb mus-maj">B</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_bemole_minor_latin_chords(self):
        result = self.highlight(':: Cbm Dbm Ebm Fbm Gbm Abm Bm')

        self.assertEqual(
            '<div class="highlight">'
            '<pre>'
            '<span></span>'
            '<span class="kn">::</span> '
            '<span class="mus-cb mus-min">Cbm</span> '
            '<span class="mus-db mus-min">Dbm</span> '
            '<span class="mus-eb mus-min">Ebm</span> '
            '<span class="mus-fb mus-min">Fbm</span> '
            '<span class="mus-gb mus-min">Gbm</span> '
            '<span class="mus-ab mus-min">Abm</span> '
            '<span class="mus-bb mus-min">Bm</span>'
            '</pre>'
            '</div>',
            result
        )


if __name__ == '__main__':
    unittest.main()
