# -*- coding: utf-8 -*-
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
        cls.lexer = load_lexer_from_file(lexer_filename, 'BemolleLexer')
        cls.formatter = get_formatter_by_name('html', style='bemolle',
                                              noclasses=True)

    def highlight(self, s):
        return highlight(s, self.lexer, self.formatter).replace('\n', '')

    def test_becuadro_major_latin_chords(self):
        result = self.highlight(':: C D E F G A H')

        self.assertEqual(
            '<div class="highlight" style="background: #f8f8f8">'
            '<pre style="line-height: 125%">'
            '<span></span>'
            '<span style="color: #d0d0d0">::</span> '
            '<span style="color: #00e800">C</span> '
            '<span style="color: #006bff">D</span> '
            '<span style="color: #8100ce">E</span> '
            '<span style="color: #3d015b">F</span> '
            '<span style="color: #d10400">G</span> '
            '<span style="color: #ff8800">A</span> '
            '<span style="color: #9af400">H</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_becuadro_minor_latin_chords(self):
        result = self.highlight(':: Cm Dm Em Fm Gm Am Hm')

        self.assertEqual(
            '<div class="highlight" style="background: #f8f8f8">'
            '<pre style="line-height: 125%">'
            '<span></span>'
            '<span style="color: #d0d0d0">::</span> '
            '<span style="color: #00e800">Cm</span> '
            '<span style="color: #006bff">Dm</span> '
            '<span style="color: #8100ce">Em</span> '
            '<span style="color: #3d015b">Fm</span> '
            '<span style="color: #d10400">Gm</span> '
            '<span style="color: #ff8800">Am</span> '
            '<span style="color: #9af400">Hm</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_bemole_major_latin_chords(self):
        result = self.highlight(':: Cb Db Eb Fb Gb Ab B')

        self.assertEqual(
            '<div class="highlight" style="background: #f8f8f8">'
            '<pre style="line-height: 125%">'
            '<span></span>'
            '<span style="color: #d0d0d0">::</span> '
            '<span style="color: #9af400">Cb</span> '
            '<span style="color: #05feaa">Db</span> '
            '<span style="color: #2e01f0">Eb</span> '
            '<span style="color: #8100ce">Fb</span> '
            '<span style="color: #680351">Gb</span> '
            '<span style="color: #e44202">Ab</span> '
            '<span style="color: #ebff07">B</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_bemole_minor_latin_chords(self):
        result = self.highlight(':: Cbm Dbm Ebm Fbm Gbm Abm Bm')

        self.assertEqual(
            '<div class="highlight" style="background: #f8f8f8">'
            '<pre style="line-height: 125%">'
            '<span></span>'
            '<span style="color: #d0d0d0">::</span> '
            '<span style="color: #9af400">Cbm</span> '
            '<span style="color: #05feaa">Dbm</span> '
            '<span style="color: #2e01f0">Ebm</span> '
            '<span style="color: #8100ce">Fbm</span> '
            '<span style="color: #680351">Gbm</span> '
            '<span style="color: #e44202">Abm</span> '
            '<span style="color: #ebff07">Bm</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_diesis_major_latin_chords(self):
        result = self.highlight(':: C# D# E# F# G# A# H#')

        self.assertEqual(
            '<div class="highlight" style="background: #f8f8f8">'
            '<pre style="line-height: 125%">'
            '<span></span>'
            '<span style="color: #d0d0d0">::</span> '
            '<span style="color: #05feaa">C#</span> '
            '<span style="color: #2e01f0">D#</span> '
            '<span style="color: #3d015b">E#</span> '
            '<span style="color: #680351">F#</span> '
            '<span style="color: #e44202">G#</span> '
            '<span style="color: #ebff07">A#</span> '
            '<span style="color: #00e800">H#</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_diesis_minor_latin_chords(self):
        result = self.highlight(':: C#m D#m E#m F#m G#m A#m H#m')

        self.assertEqual(
            '<div class="highlight" style="background: #f8f8f8">'
            '<pre style="line-height: 125%">'
            '<span></span>'
            '<span style="color: #d0d0d0">::</span> '
            '<span style="color: #05feaa">C#m</span> '
            '<span style="color: #2e01f0">D#m</span> '
            '<span style="color: #3d015b">E#m</span> '
            '<span style="color: #680351">F#m</span> '
            '<span style="color: #e44202">G#m</span> '
            '<span style="color: #ebff07">A#m</span> '
            '<span style="color: #00e800">H#m</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_becuadro_major_latin_alt_chords(self):
        for alt in ('2', '6', '7', '7+', '9', 'add6', 'dim', 'sus4', '6/B'):
            result = self.highlight(
                ':: C{0} D{0} E{0} F{0} G{0} A{0} H{0}'
                .format(alt))

            self.assertEqual(
                '<div class="highlight" style="background: #f8f8f8">'
                '<pre style="line-height: 125%">'
                '<span></span>'
                '<span style="color: #d0d0d0">::</span> '
                '<span style="color: #00e800">C{0}</span> '
                '<span style="color: #006bff">D{0}</span> '
                '<span style="color: #8100ce">E{0}</span> '
                '<span style="color: #3d015b">F{0}</span> '
                '<span style="color: #d10400">G{0}</span> '
                '<span style="color: #ff8800">A{0}</span> '
                '<span style="color: #9af400">H{0}</span>'
                '</pre>'
                '</div>'.format(alt),
                result
            )

    def test_becuadro_minor_latin_alt_chords(self):
        for alt in ('2', '6', '7', '7+', '9', 'add6', 'dim', 'sus4', '6/B'):
            result = self.highlight(
                ':: Cm{0} Dm{0} Em{0} Fm{0} Gm{0} Am{0} Hm{0}'
                .format(alt))

            self.assertEqual(
                '<div class="highlight" style="background: #f8f8f8">'
                '<pre style="line-height: 125%">'
                '<span></span>'
                '<span style="color: #d0d0d0">::</span> '
                '<span style="color: #00e800">Cm{0}</span> '
                '<span style="color: #006bff">Dm{0}</span> '
                '<span style="color: #8100ce">Em{0}</span> '
                '<span style="color: #3d015b">Fm{0}</span> '
                '<span style="color: #d10400">Gm{0}</span> '
                '<span style="color: #ff8800">Am{0}</span> '
                '<span style="color: #9af400">Hm{0}</span>'
                '</pre>'
                '</div>'.format(alt),
                result
            )

    def test_bemolle_major_latin_alt_chords(self):
        for alt in ('2', '6', '7', '7+', '9', 'add6', 'dim', 'sus4', '6/B'):
            result = self.highlight(
                ':: Cb{0} Db{0} Eb{0} Fb{0} Gb{0} Ab{0} B{0}'
                .format(alt))

            self.assertEqual(
                '<div class="highlight" style="background: #f8f8f8">'
                '<pre style="line-height: 125%">'
                '<span></span>'
                '<span style="color: #d0d0d0">::</span> '
                '<span style="color: #9af400">Cb{0}</span> '
                '<span style="color: #05feaa">Db{0}</span> '
                '<span style="color: #2e01f0">Eb{0}</span> '
                '<span style="color: #8100ce">Fb{0}</span> '
                '<span style="color: #680351">Gb{0}</span> '
                '<span style="color: #e44202">Ab{0}</span> '
                '<span style="color: #ebff07">B{0}</span>'
                '</pre>'
                '</div>'.format(alt),
                result
            )

    def test_bemolle_minor_latin_alt_chords(self):
        for alt in ('2', '6', '7', '7+', '9', 'add6', 'dim', 'sus4', '6/B'):
            result = self.highlight(
                ':: Cbm{0} Dbm{0} Ebm{0} Fbm{0} Gbm{0} Abm{0} Bm{0}'
                .format(alt))

            self.assertEqual(
                '<div class="highlight" style="background: #f8f8f8">'
                '<pre style="line-height: 125%">'
                '<span></span>'
                '<span style="color: #d0d0d0">::</span> '
                '<span style="color: #9af400">Cbm{0}</span> '
                '<span style="color: #05feaa">Dbm{0}</span> '
                '<span style="color: #2e01f0">Ebm{0}</span> '
                '<span style="color: #8100ce">Fbm{0}</span> '
                '<span style="color: #680351">Gbm{0}</span> '
                '<span style="color: #e44202">Abm{0}</span> '
                '<span style="color: #ebff07">Bm{0}</span>'
                '</pre>'
                '</div>'.format(alt),
                result
            )

    def test_diesis_major_latin_alt_chords(self):
        for alt in ('2', '6', '7', '7+', '9', 'add6', 'dim', 'sus4', '6/B'):
            result = self.highlight(
                ':: C#{0} D#{0} E#{0} F#{0} G#{0} A#{0} H#{0}'
                .format(alt))

            self.assertEqual(
                '<div class="highlight" style="background: #f8f8f8">'
                '<pre style="line-height: 125%">'
                '<span></span>'
                '<span style="color: #d0d0d0">::</span> '
                '<span style="color: #05feaa">C#{0}</span> '
                '<span style="color: #2e01f0">D#{0}</span> '
                '<span style="color: #3d015b">E#{0}</span> '
                '<span style="color: #680351">F#{0}</span> '
                '<span style="color: #e44202">G#{0}</span> '
                '<span style="color: #ebff07">A#{0}</span> '
                '<span style="color: #00e800">H#{0}</span>'
                '</pre>'
                '</div>'.format(alt),
                result
            )

    def test_diesis_minor_latin_alt_chords(self):
        for alt in ('2', '6', '7', '7+', '9', 'add6', 'dim', 'sus4', '6/B'):
            result = self.highlight(
                ':: C#m{0} D#m{0} E#m{0} F#m{0} G#m{0} A#m{0} H#m{0}'
                .format(alt))

            self.assertEqual(
                '<div class="highlight" style="background: #f8f8f8">'
                '<pre style="line-height: 125%">'
                '<span></span>'
                '<span style="color: #d0d0d0">::</span> '
                '<span style="color: #05feaa">C#m{0}</span> '
                '<span style="color: #2e01f0">D#m{0}</span> '
                '<span style="color: #3d015b">E#m{0}</span> '
                '<span style="color: #680351">F#m{0}</span> '
                '<span style="color: #e44202">G#m{0}</span> '
                '<span style="color: #ebff07">A#m{0}</span> '
                '<span style="color: #00e800">H#m{0}</span>'
                '</pre>'
                '</div>'.format(alt),
                result
            )

    def test_becuadro_major_english_chords(self):
        result = self.highlight(';; C D E F G A B')

        self.assertEqual(
            '<div class="highlight" style="background: #f8f8f8">'
            '<pre style="line-height: 125%">'
            '<span></span>'
            '<span style="color: #d0d0d0">;;</span> '
            '<span style="color: #00e800">C</span> '
            '<span style="color: #006bff">D</span> '
            '<span style="color: #8100ce">E</span> '
            '<span style="color: #3d015b">F</span> '
            '<span style="color: #d10400">G</span> '
            '<span style="color: #ff8800">A</span> '
            '<span style="color: #9af400">B</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_becuadro_minor_english_chords(self):
        result = self.highlight(';; Cm Dm Em Fm Gm Am Bm')

        self.assertEqual(
            '<div class="highlight" style="background: #f8f8f8">'
            '<pre style="line-height: 125%">'
            '<span></span>'
            '<span style="color: #d0d0d0">;;</span> '
            '<span style="color: #00e800">Cm</span> '
            '<span style="color: #006bff">Dm</span> '
            '<span style="color: #8100ce">Em</span> '
            '<span style="color: #3d015b">Fm</span> '
            '<span style="color: #d10400">Gm</span> '
            '<span style="color: #ff8800">Am</span> '
            '<span style="color: #9af400">Bm</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_bemole_major_english_chords(self):
        result = self.highlight(';; Cb Db Eb Fb Gb Ab Bb')

        self.assertEqual(
            '<div class="highlight" style="background: #f8f8f8">'
            '<pre style="line-height: 125%">'
            '<span></span>'
            '<span style="color: #d0d0d0">;;</span> '
            '<span style="color: #9af400">Cb</span> '
            '<span style="color: #05feaa">Db</span> '
            '<span style="color: #2e01f0">Eb</span> '
            '<span style="color: #8100ce">Fb</span> '
            '<span style="color: #680351">Gb</span> '
            '<span style="color: #e44202">Ab</span> '
            '<span style="color: #ebff07">Bb</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_bemole_minor_english_chords(self):
        result = self.highlight(';; Cbm Dbm Ebm Fbm Gbm Abm Bbm')

        self.assertEqual(
            '<div class="highlight" style="background: #f8f8f8">'
            '<pre style="line-height: 125%">'
            '<span></span>'
            '<span style="color: #d0d0d0">;;</span> '
            '<span style="color: #9af400">Cbm</span> '
            '<span style="color: #05feaa">Dbm</span> '
            '<span style="color: #2e01f0">Ebm</span> '
            '<span style="color: #8100ce">Fbm</span> '
            '<span style="color: #680351">Gbm</span> '
            '<span style="color: #e44202">Abm</span> '
            '<span style="color: #ebff07">Bbm</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_diesis_major_english_chords(self):
        result = self.highlight(';; C# D# E# F# G# A# B#')

        self.assertEqual(
            '<div class="highlight" style="background: #f8f8f8">'
            '<pre style="line-height: 125%">'
            '<span></span>'
            '<span style="color: #d0d0d0">;;</span> '
            '<span style="color: #05feaa">C#</span> '
            '<span style="color: #2e01f0">D#</span> '
            '<span style="color: #3d015b">E#</span> '
            '<span style="color: #680351">F#</span> '
            '<span style="color: #e44202">G#</span> '
            '<span style="color: #ebff07">A#</span> '
            '<span style="color: #00e800">B#</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_diesis_minor_english_chords(self):
        result = self.highlight(';; C#m D#m E#m F#m G#m A#m B#m')

        self.assertEqual(
            '<div class="highlight" style="background: #f8f8f8">'
            '<pre style="line-height: 125%">'
            '<span></span>'
            '<span style="color: #d0d0d0">;;</span> '
            '<span style="color: #05feaa">C#m</span> '
            '<span style="color: #2e01f0">D#m</span> '
            '<span style="color: #3d015b">E#m</span> '
            '<span style="color: #680351">F#m</span> '
            '<span style="color: #e44202">G#m</span> '
            '<span style="color: #ebff07">A#m</span> '
            '<span style="color: #00e800">B#m</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_becuadro_major_english_alt_chords(self):
        for alt in ('2', '6', '7', '7+', '9', 'add6', 'dim', 'sus4', '6/B'):
            result = self.highlight(
                ';; C{0} D{0} E{0} F{0} G{0} A{0} B{0}'
                .format(alt))

            self.assertEqual(
                '<div class="highlight" style="background: #f8f8f8">'
                '<pre style="line-height: 125%">'
                '<span></span>'
                '<span style="color: #d0d0d0">;;</span> '
                '<span style="color: #00e800">C{0}</span> '
                '<span style="color: #006bff">D{0}</span> '
                '<span style="color: #8100ce">E{0}</span> '
                '<span style="color: #3d015b">F{0}</span> '
                '<span style="color: #d10400">G{0}</span> '
                '<span style="color: #ff8800">A{0}</span> '
                '<span style="color: #9af400">B{0}</span>'
                '</pre>'
                '</div>'.format(alt),
                result
            )

    def test_becuadro_minor_english_alt_chords(self):
        for alt in ('2', '6', '7', '7+', '9', 'add6', 'dim', 'sus4', '6/B'):
            result = self.highlight(
                ';; Cm{0} Dm{0} Em{0} Fm{0} Gm{0} Am{0} Bm{0}'
                .format(alt))

            self.assertEqual(
                '<div class="highlight" style="background: #f8f8f8">'
                '<pre style="line-height: 125%">'
                '<span></span>'
                '<span style="color: #d0d0d0">;;</span> '
                '<span style="color: #00e800">Cm{0}</span> '
                '<span style="color: #006bff">Dm{0}</span> '
                '<span style="color: #8100ce">Em{0}</span> '
                '<span style="color: #3d015b">Fm{0}</span> '
                '<span style="color: #d10400">Gm{0}</span> '
                '<span style="color: #ff8800">Am{0}</span> '
                '<span style="color: #9af400">Bm{0}</span>'
                '</pre>'
                '</div>'.format(alt),
                result
            )

    def test_bemolle_major_english_alt_chords(self):
        for alt in ('2', '6', '7', '7+', '9', 'add6', 'dim', 'sus4', '6/B'):
            result = self.highlight(
                ';; Cb{0} Db{0} Eb{0} Fb{0} Gb{0} Ab{0} Bb{0}'
                .format(alt))

            self.assertEqual(
                '<div class="highlight" style="background: #f8f8f8">'
                '<pre style="line-height: 125%">'
                '<span></span>'
                '<span style="color: #d0d0d0">;;</span> '
                '<span style="color: #9af400">Cb{0}</span> '
                '<span style="color: #05feaa">Db{0}</span> '
                '<span style="color: #2e01f0">Eb{0}</span> '
                '<span style="color: #8100ce">Fb{0}</span> '
                '<span style="color: #680351">Gb{0}</span> '
                '<span style="color: #e44202">Ab{0}</span> '
                '<span style="color: #ebff07">Bb{0}</span>'
                '</pre>'
                '</div>'.format(alt),
                result
            )

    def test_bemolle_minor_english_alt_chords(self):
        for alt in ('2', '6', '7', '7+', '9', 'add6', 'dim', 'sus4', '6/B'):
            result = self.highlight(
                ';; Cbm{0} Dbm{0} Ebm{0} Fbm{0} Gbm{0} Abm{0} Bbm{0}'
                .format(alt))

            self.assertEqual(
                '<div class="highlight" style="background: #f8f8f8">'
                '<pre style="line-height: 125%">'
                '<span></span>'
                '<span style="color: #d0d0d0">;;</span> '
                '<span style="color: #9af400">Cbm{0}</span> '
                '<span style="color: #05feaa">Dbm{0}</span> '
                '<span style="color: #2e01f0">Ebm{0}</span> '
                '<span style="color: #8100ce">Fbm{0}</span> '
                '<span style="color: #680351">Gbm{0}</span> '
                '<span style="color: #e44202">Abm{0}</span> '
                '<span style="color: #ebff07">Bbm{0}</span>'
                '</pre>'
                '</div>'.format(alt),
                result
            )

    def test_diesis_major_english_alt_chords(self):
        for alt in ('2', '6', '7', '7+', '9', 'add6', 'dim', 'sus4', '6/B'):
            result = self.highlight(
                ';; C#{0} D#{0} E#{0} F#{0} G#{0} A#{0} B#{0}'
                .format(alt))

            self.assertEqual(
                '<div class="highlight" style="background: #f8f8f8">'
                '<pre style="line-height: 125%">'
                '<span></span>'
                '<span style="color: #d0d0d0">;;</span> '
                '<span style="color: #05feaa">C#{0}</span> '
                '<span style="color: #2e01f0">D#{0}</span> '
                '<span style="color: #3d015b">E#{0}</span> '
                '<span style="color: #680351">F#{0}</span> '
                '<span style="color: #e44202">G#{0}</span> '
                '<span style="color: #ebff07">A#{0}</span> '
                '<span style="color: #00e800">B#{0}</span>'
                '</pre>'
                '</div>'.format(alt),
                result
            )

    def test_diesis_minor_english_alt_chords(self):
        for alt in ('2', '6', '7', '7+', '9', 'add6', 'dim', 'sus4', '6/B'):
            result = self.highlight(
                ';; C#m{0} D#m{0} E#m{0} F#m{0} G#m{0} A#m{0} B#m{0}'
                .format(alt))

            self.assertEqual(
                '<div class="highlight" style="background: #f8f8f8">'
                '<pre style="line-height: 125%">'
                '<span></span>'
                '<span style="color: #d0d0d0">;;</span> '
                '<span style="color: #05feaa">C#m{0}</span> '
                '<span style="color: #2e01f0">D#m{0}</span> '
                '<span style="color: #3d015b">E#m{0}</span> '
                '<span style="color: #680351">F#m{0}</span> '
                '<span style="color: #e44202">G#m{0}</span> '
                '<span style="color: #ebff07">A#m{0}</span> '
                '<span style="color: #00e800">B#m{0}</span>'
                '</pre>'
                '</div>'.format(alt),
                result
            )


if __name__ == '__main__':
    unittest.main()
