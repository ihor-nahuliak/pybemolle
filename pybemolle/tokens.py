# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from pygments.token import *


Chord = Name.Chord

Do = C = Chord.C
Re = D = Chord.D
Mi = E = Chord.E
Fa = F = Chord.F
Sol = G = Chord.G
La = A = Chord.A
Si = B = Chord.B

DoBemolle = CFlat = Chord.C.Flat
ReBemolle = DFlat = Chord.D.Flat
MiBemolle = EFlat = Chord.E.Flat
FaBemolle = FFlat = Chord.F.Flat
SolBemolle = GFlat = Chord.G.Flat
LaBemolle = AFlat = Chord.A.Flat
SiBemolle = BFlat = Chord.B.Flat

DoDiesis = CSharp = Chord.C.Sharp
ReDiesis = DSharp = Chord.D.Sharp
MiDiesis = ESharp = Chord.E.Sharp
FaDiesis = FSharp = Chord.F.Sharp
SolDiesis = GSharp = Chord.G.Sharp
LaDiesis = ASharp = Chord.A.Sharp
SiDiesis = BSharp = Chord.B.Sharp

# put our own tokens into style sheet
STANDARD_TYPES.update({
    C: 'c',
    D: 'd',
    E: 'e',
    F: 'f',
    G: 'f',
    A: 'a',
    B: 'b',
    C.Flat: 'cb',
    D.Flat: 'db',
    E.Flat: 'eb',
    F.Flat: 'fb',
    G.Flat: 'fb',
    A.Flat: 'ab',
    B.Flat: 'bb',
    C.Sharp: 'cs',
    D.Sharp: 'ds',
    E.Sharp: 'es',
    F.Sharp: 'fs',
    G.Sharp: 'fs',
    A.Sharp: 'as',
    B.Sharp: 'bs',
})
