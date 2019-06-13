# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pygments.lexer import RegexLexer, bygroups, default
from pygments.token import *

from pybemolle.tokens import *


__all__ = ['BemolleLexer']


class BemolleLexer(RegexLexer):
    name = 'Bemolle'
    aliases = ['bemolle', 'bmolle']
    filenames = ['*.bemolle', '*.bmolle']
    mimetypes = ['text/be-molle', 'text/b-molle',
                 'text/bemolle', 'text/bmolle']

    def include_chords(*tokens, alt=r'[#\*\w\\\/]*'):
        """Makes a list of tokens ready to include.
        Adds all possible tokens: major, minor, a symbols, etc.

        :param tuple tokens: tuple of (regex, pygments.token.Token)
        :param str alt: alteration symbols regexp
        :return list: list of tokens ready to include
        """
        result = [(r'(?:[ \t]|\\\n)+', Text)]
        for r, ch in tokens:
            result.append((r'\b({0}m)({1})'.format(r, alt),
                           bygroups(ch.Minor, ch.Alt)))
            result.append((r'\b({0})({1})'.format(r, alt),
                           bygroups(ch.Major, ch.Alt)))
        result.append(default('#pop'))
        return result

    tokens = {
        'root': [
            (r'(::|:lat)((?:\s|\\\s)+)', bygroups(Keyword.Namespace, Text),
             'chords_lat'),
            (r'(;;|;eng)((?:\s|\\\s)+)', bygroups(Keyword.Namespace, Text),
             'chords_eng'),
            (r'.', Text),
        ],
        'chords_lat': include_chords(
            (r'C#', DoDiesis),
            (r'D#', ReDiesis),
            (r'E#', MiDiesis),
            (r'F#', FaDiesis),
            (r'G#', SolDiesis),
            (r'A#', LaDiesis),
            (r'H#', SiDiesis),
            (r'Cb', DoBemolle),
            (r'Db', ReBemolle),
            (r'Eb', MiBemolle),
            (r'Fb', FaBemolle),
            (r'Gb', SolBemolle),
            (r'Ab', LaBemolle),
            (r'B', SiBemolle),
            (r'C', Do),
            (r'D', Re),
            (r'E', Mi),
            (r'F', Fa),
            (r'G', Sol),
            (r'A', La),
            (r'H', Si),
        ),
        'chords_eng': include_chords(
            (r'C#', CSharp),
            (r'D#', DSharp),
            (r'E#', ESharp),
            (r'F#', FSharp),
            (r'G#', GSharp),
            (r'A#', ASharp),
            (r'B#', BSharp),
            (r'Cb', CFlat),
            (r'Db', DFlat),
            (r'Eb', EFlat),
            (r'Fb', FFlat),
            (r'Gb', GFlat),
            (r'Ab', AFlat),
            (r'Bb', BFlat),
            (r'C', C),
            (r'D', D),
            (r'E', E),
            (r'F', F),
            (r'G', G),
            (r'A', A),
            (r'B', B),
        ),
    }
