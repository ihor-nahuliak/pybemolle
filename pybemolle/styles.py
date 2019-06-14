# -*- coding: utf-8 -*-
"""
    pygments.styles.native
    ~~~~~~~~~~~~~~~~~~~~~~

    pygments version of my "native" vim theme.

    :copyright: Copyright 2006-2019 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.style import Style

from pybemolle.tokens import *


__all__ = ['BemolleStyle']


class BemolleStyle(Style):
    """
    Colored chords theme.
    """

    background_color = '#202020'
    highlight_color = '#404040'

    styles = {
        Token: '#d0d0d0',
        Whitespace: '#666666',

        Chord.C: '#00e800',
        Chord.D: '#006bff',
        Chord.E: '#8100ce',
        Chord.F: '#3d015b',
        Chord.G: '#d10400',
        Chord.A: '#ff8800',
        Chord.B: '#9af400',

        Error: 'bg:#e3d2d2 #a61717'
    }
