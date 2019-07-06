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

    def test_diesis_major_latin_chords(self):
        result = self.highlight(':: C# D# E# F# G# A# H#')

        self.assertEqual(
            '<div class="highlight">'
            '<pre>'
            '<span></span>'
            '<span class="kn">::</span> '
            '<span class="mus-cs mus-maj">C#</span> '
            '<span class="mus-ds mus-maj">D#</span> '
            '<span class="mus-es mus-maj">E#</span> '
            '<span class="mus-fs mus-maj">F#</span> '
            '<span class="mus-gs mus-maj">G#</span> '
            '<span class="mus-as mus-maj">A#</span> '
            '<span class="mus-bs mus-maj">H#</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_diesis_minor_latin_chords(self):
        result = self.highlight(':: C#m D#m E#m F#m G#m A#m H#m')

        self.assertEqual(
            '<div class="highlight">'
            '<pre>'
            '<span></span>'
            '<span class="kn">::</span> '
            '<span class="mus-cs mus-min">C#m</span> '
            '<span class="mus-ds mus-min">D#m</span> '
            '<span class="mus-es mus-min">E#m</span> '
            '<span class="mus-fs mus-min">F#m</span> '
            '<span class="mus-gs mus-min">G#m</span> '
            '<span class="mus-as mus-min">A#m</span> '
            '<span class="mus-bs mus-min">H#m</span>'
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
                '<div class="highlight">'
                '<pre>'
                '<span></span>'
                '<span class="kn">::</span> '
                '<span class="mus-c mus-maj">C</span>'
                '<span class="mus-c mus-alt">{0}</span> '
                '<span class="mus-d mus-maj">D</span>'
                '<span class="mus-d mus-alt">{0}</span> '
                '<span class="mus-e mus-maj">E</span>'
                '<span class="mus-e mus-alt">{0}</span> '
                '<span class="mus-f mus-maj">F</span>'
                '<span class="mus-f mus-alt">{0}</span> '
                '<span class="mus-g mus-maj">G</span>'
                '<span class="mus-g mus-alt">{0}</span> '
                '<span class="mus-a mus-maj">A</span>'
                '<span class="mus-a mus-alt">{0}</span> '
                '<span class="mus-b mus-maj">H</span>'
                '<span class="mus-b mus-alt">{0}</span>'
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
                '<div class="highlight">'
                '<pre>'
                '<span></span>'
                '<span class="kn">::</span> '
                '<span class="mus-c mus-min">Cm</span>'
                '<span class="mus-c mus-alt">{0}</span> '
                '<span class="mus-d mus-min">Dm</span>'
                '<span class="mus-d mus-alt">{0}</span> '
                '<span class="mus-e mus-min">Em</span>'
                '<span class="mus-e mus-alt">{0}</span> '
                '<span class="mus-f mus-min">Fm</span>'
                '<span class="mus-f mus-alt">{0}</span> '
                '<span class="mus-g mus-min">Gm</span>'
                '<span class="mus-g mus-alt">{0}</span> '
                '<span class="mus-a mus-min">Am</span>'
                '<span class="mus-a mus-alt">{0}</span> '
                '<span class="mus-b mus-min">Hm</span>'
                '<span class="mus-b mus-alt">{0}</span>'
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
                '<div class="highlight">'
                '<pre>'
                '<span></span>'
                '<span class="kn">::</span> '
                '<span class="mus-cb mus-maj">Cb</span>'
                '<span class="mus-cb mus-alt">{0}</span> '
                '<span class="mus-db mus-maj">Db</span>'
                '<span class="mus-db mus-alt">{0}</span> '
                '<span class="mus-eb mus-maj">Eb</span>'
                '<span class="mus-eb mus-alt">{0}</span> '
                '<span class="mus-fb mus-maj">Fb</span>'
                '<span class="mus-fb mus-alt">{0}</span> '
                '<span class="mus-gb mus-maj">Gb</span>'
                '<span class="mus-gb mus-alt">{0}</span> '
                '<span class="mus-ab mus-maj">Ab</span>'
                '<span class="mus-ab mus-alt">{0}</span> '
                '<span class="mus-bb mus-maj">B</span>'
                '<span class="mus-bb mus-alt">{0}</span>'
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
                '<div class="highlight">'
                '<pre>'
                '<span></span>'
                '<span class="kn">::</span> '
                '<span class="mus-cb mus-min">Cbm</span>'
                '<span class="mus-cb mus-alt">{0}</span> '
                '<span class="mus-db mus-min">Dbm</span>'
                '<span class="mus-db mus-alt">{0}</span> '
                '<span class="mus-eb mus-min">Ebm</span>'
                '<span class="mus-eb mus-alt">{0}</span> '
                '<span class="mus-fb mus-min">Fbm</span>'
                '<span class="mus-fb mus-alt">{0}</span> '
                '<span class="mus-gb mus-min">Gbm</span>'
                '<span class="mus-gb mus-alt">{0}</span> '
                '<span class="mus-ab mus-min">Abm</span>'
                '<span class="mus-ab mus-alt">{0}</span> '
                '<span class="mus-bb mus-min">Bm</span>'
                '<span class="mus-bb mus-alt">{0}</span>'
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
                '<div class="highlight">'
                '<pre>'
                '<span></span>'
                '<span class="kn">::</span> '
                '<span class="mus-cs mus-maj">C#</span>'
                '<span class="mus-cs mus-alt">{0}</span> '
                '<span class="mus-ds mus-maj">D#</span>'
                '<span class="mus-ds mus-alt">{0}</span> '
                '<span class="mus-es mus-maj">E#</span>'
                '<span class="mus-es mus-alt">{0}</span> '
                '<span class="mus-fs mus-maj">F#</span>'
                '<span class="mus-fs mus-alt">{0}</span> '
                '<span class="mus-gs mus-maj">G#</span>'
                '<span class="mus-gs mus-alt">{0}</span> '
                '<span class="mus-as mus-maj">A#</span>'
                '<span class="mus-as mus-alt">{0}</span> '
                '<span class="mus-bs mus-maj">H#</span>'
                '<span class="mus-bs mus-alt">{0}</span>'
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
                '<div class="highlight">'
                '<pre>'
                '<span></span>'
                '<span class="kn">::</span> '
                '<span class="mus-cs mus-min">C#m</span>'
                '<span class="mus-cs mus-alt">{0}</span> '
                '<span class="mus-ds mus-min">D#m</span>'
                '<span class="mus-ds mus-alt">{0}</span> '
                '<span class="mus-es mus-min">E#m</span>'
                '<span class="mus-es mus-alt">{0}</span> '
                '<span class="mus-fs mus-min">F#m</span>'
                '<span class="mus-fs mus-alt">{0}</span> '
                '<span class="mus-gs mus-min">G#m</span>'
                '<span class="mus-gs mus-alt">{0}</span> '
                '<span class="mus-as mus-min">A#m</span>'
                '<span class="mus-as mus-alt">{0}</span> '
                '<span class="mus-bs mus-min">H#m</span>'
                '<span class="mus-bs mus-alt">{0}</span>'
                '</pre>'
                '</div>'.format(alt),
                result
            )

    def test_becuadro_major_english_chords(self):
        result = self.highlight(';; C D E F G A B')

        self.assertEqual(
            '<div class="highlight">'
            '<pre>'
            '<span></span>'
            '<span class="kn">;;</span> '
            '<span class="mus-c mus-maj">C</span> '
            '<span class="mus-d mus-maj">D</span> '
            '<span class="mus-e mus-maj">E</span> '
            '<span class="mus-f mus-maj">F</span> '
            '<span class="mus-g mus-maj">G</span> '
            '<span class="mus-a mus-maj">A</span> '
            '<span class="mus-b mus-maj">B</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_becuadro_minor_english_chords(self):
        result = self.highlight(';; Cm Dm Em Fm Gm Am Bm')

        self.assertEqual(
            '<div class="highlight">'
            '<pre>'
            '<span></span>'
            '<span class="kn">;;</span> '
            '<span class="mus-c mus-min">Cm</span> '
            '<span class="mus-d mus-min">Dm</span> '
            '<span class="mus-e mus-min">Em</span> '
            '<span class="mus-f mus-min">Fm</span> '
            '<span class="mus-g mus-min">Gm</span> '
            '<span class="mus-a mus-min">Am</span> '
            '<span class="mus-b mus-min">Bm</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_bemole_major_english_chords(self):
        result = self.highlight(';; Cb Db Eb Fb Gb Ab Bb')

        self.assertEqual(
            '<div class="highlight">'
            '<pre>'
            '<span></span>'
            '<span class="kn">;;</span> '
            '<span class="mus-cb mus-maj">Cb</span> '
            '<span class="mus-db mus-maj">Db</span> '
            '<span class="mus-eb mus-maj">Eb</span> '
            '<span class="mus-fb mus-maj">Fb</span> '
            '<span class="mus-gb mus-maj">Gb</span> '
            '<span class="mus-ab mus-maj">Ab</span> '
            '<span class="mus-bb mus-maj">Bb</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_bemole_minor_english_chords(self):
        result = self.highlight(';; Cbm Dbm Ebm Fbm Gbm Abm Bbm')

        self.assertEqual(
            '<div class="highlight">'
            '<pre>'
            '<span></span>'
            '<span class="kn">;;</span> '
            '<span class="mus-cb mus-min">Cbm</span> '
            '<span class="mus-db mus-min">Dbm</span> '
            '<span class="mus-eb mus-min">Ebm</span> '
            '<span class="mus-fb mus-min">Fbm</span> '
            '<span class="mus-gb mus-min">Gbm</span> '
            '<span class="mus-ab mus-min">Abm</span> '
            '<span class="mus-bb mus-min">Bbm</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_diesis_major_english_chords(self):
        result = self.highlight(';; C# D# E# F# G# A# B#')

        self.assertEqual(
            '<div class="highlight">'
            '<pre>'
            '<span></span>'
            '<span class="kn">;;</span> '
            '<span class="mus-cs mus-maj">C#</span> '
            '<span class="mus-ds mus-maj">D#</span> '
            '<span class="mus-es mus-maj">E#</span> '
            '<span class="mus-fs mus-maj">F#</span> '
            '<span class="mus-gs mus-maj">G#</span> '
            '<span class="mus-as mus-maj">A#</span> '
            '<span class="mus-bs mus-maj">B#</span>'
            '</pre>'
            '</div>',
            result
        )

    def test_diesis_minor_english_chords(self):
        result = self.highlight(';; C#m D#m E#m F#m G#m A#m B#m')

        self.assertEqual(
            '<div class="highlight">'
            '<pre>'
            '<span></span>'
            '<span class="kn">;;</span> '
            '<span class="mus-cs mus-min">C#m</span> '
            '<span class="mus-ds mus-min">D#m</span> '
            '<span class="mus-es mus-min">E#m</span> '
            '<span class="mus-fs mus-min">F#m</span> '
            '<span class="mus-gs mus-min">G#m</span> '
            '<span class="mus-as mus-min">A#m</span> '
            '<span class="mus-bs mus-min">B#m</span>'
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
                '<div class="highlight">'
                '<pre>'
                '<span></span>'
                '<span class="kn">;;</span> '
                '<span class="mus-c mus-maj">C</span>'
                '<span class="mus-c mus-alt">{0}</span> '
                '<span class="mus-d mus-maj">D</span>'
                '<span class="mus-d mus-alt">{0}</span> '
                '<span class="mus-e mus-maj">E</span>'
                '<span class="mus-e mus-alt">{0}</span> '
                '<span class="mus-f mus-maj">F</span>'
                '<span class="mus-f mus-alt">{0}</span> '
                '<span class="mus-g mus-maj">G</span>'
                '<span class="mus-g mus-alt">{0}</span> '
                '<span class="mus-a mus-maj">A</span>'
                '<span class="mus-a mus-alt">{0}</span> '
                '<span class="mus-b mus-maj">B</span>'
                '<span class="mus-b mus-alt">{0}</span>'
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
                '<div class="highlight">'
                '<pre>'
                '<span></span>'
                '<span class="kn">;;</span> '
                '<span class="mus-c mus-min">Cm</span>'
                '<span class="mus-c mus-alt">{0}</span> '
                '<span class="mus-d mus-min">Dm</span>'
                '<span class="mus-d mus-alt">{0}</span> '
                '<span class="mus-e mus-min">Em</span>'
                '<span class="mus-e mus-alt">{0}</span> '
                '<span class="mus-f mus-min">Fm</span>'
                '<span class="mus-f mus-alt">{0}</span> '
                '<span class="mus-g mus-min">Gm</span>'
                '<span class="mus-g mus-alt">{0}</span> '
                '<span class="mus-a mus-min">Am</span>'
                '<span class="mus-a mus-alt">{0}</span> '
                '<span class="mus-b mus-min">Bm</span>'
                '<span class="mus-b mus-alt">{0}</span>'
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
                '<div class="highlight">'
                '<pre>'
                '<span></span>'
                '<span class="kn">;;</span> '
                '<span class="mus-cb mus-maj">Cb</span>'
                '<span class="mus-cb mus-alt">{0}</span> '
                '<span class="mus-db mus-maj">Db</span>'
                '<span class="mus-db mus-alt">{0}</span> '
                '<span class="mus-eb mus-maj">Eb</span>'
                '<span class="mus-eb mus-alt">{0}</span> '
                '<span class="mus-fb mus-maj">Fb</span>'
                '<span class="mus-fb mus-alt">{0}</span> '
                '<span class="mus-gb mus-maj">Gb</span>'
                '<span class="mus-gb mus-alt">{0}</span> '
                '<span class="mus-ab mus-maj">Ab</span>'
                '<span class="mus-ab mus-alt">{0}</span> '
                '<span class="mus-bb mus-maj">Bb</span>'
                '<span class="mus-bb mus-alt">{0}</span>'
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
                '<div class="highlight">'
                '<pre>'
                '<span></span>'
                '<span class="kn">;;</span> '
                '<span class="mus-cb mus-min">Cbm</span>'
                '<span class="mus-cb mus-alt">{0}</span> '
                '<span class="mus-db mus-min">Dbm</span>'
                '<span class="mus-db mus-alt">{0}</span> '
                '<span class="mus-eb mus-min">Ebm</span>'
                '<span class="mus-eb mus-alt">{0}</span> '
                '<span class="mus-fb mus-min">Fbm</span>'
                '<span class="mus-fb mus-alt">{0}</span> '
                '<span class="mus-gb mus-min">Gbm</span>'
                '<span class="mus-gb mus-alt">{0}</span> '
                '<span class="mus-ab mus-min">Abm</span>'
                '<span class="mus-ab mus-alt">{0}</span> '
                '<span class="mus-bb mus-min">Bbm</span>'
                '<span class="mus-bb mus-alt">{0}</span>'
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
                '<div class="highlight">'
                '<pre>'
                '<span></span>'
                '<span class="kn">;;</span> '
                '<span class="mus-cs mus-maj">C#</span>'
                '<span class="mus-cs mus-alt">{0}</span> '
                '<span class="mus-ds mus-maj">D#</span>'
                '<span class="mus-ds mus-alt">{0}</span> '
                '<span class="mus-es mus-maj">E#</span>'
                '<span class="mus-es mus-alt">{0}</span> '
                '<span class="mus-fs mus-maj">F#</span>'
                '<span class="mus-fs mus-alt">{0}</span> '
                '<span class="mus-gs mus-maj">G#</span>'
                '<span class="mus-gs mus-alt">{0}</span> '
                '<span class="mus-as mus-maj">A#</span>'
                '<span class="mus-as mus-alt">{0}</span> '
                '<span class="mus-bs mus-maj">B#</span>'
                '<span class="mus-bs mus-alt">{0}</span>'
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
                '<div class="highlight">'
                '<pre>'
                '<span></span>'
                '<span class="kn">;;</span> '
                '<span class="mus-cs mus-min">C#m</span>'
                '<span class="mus-cs mus-alt">{0}</span> '
                '<span class="mus-ds mus-min">D#m</span>'
                '<span class="mus-ds mus-alt">{0}</span> '
                '<span class="mus-es mus-min">E#m</span>'
                '<span class="mus-es mus-alt">{0}</span> '
                '<span class="mus-fs mus-min">F#m</span>'
                '<span class="mus-fs mus-alt">{0}</span> '
                '<span class="mus-gs mus-min">G#m</span>'
                '<span class="mus-gs mus-alt">{0}</span> '
                '<span class="mus-as mus-min">A#m</span>'
                '<span class="mus-as mus-alt">{0}</span> '
                '<span class="mus-bs mus-min">B#m</span>'
                '<span class="mus-bs mus-alt">{0}</span>'
                '</pre>'
                '</div>'.format(alt),
                result
            )


if __name__ == '__main__':
    unittest.main()
