#!/usr/bin/env python3


import click
import png


@click.command()
@click.argument('filename')
def ngpnginfo(filename):
    reader = png.Reader(filename)
    reader.preamble()

    palette = reader.palette()[0:16]

    c_palette = 'const u16 palette[] = { '

    # 15 14 13 12 11 10 09 08 07 06 05 04 03 02 01 00
    # db r0 g0 b0 r4 r3 r2 r1 g4 g3 g2 g1 b4 b3 b2 b1

    for color in palette:
        # convert 8-bit to 5-bit
        r = color[0] >> 3
        g = color[1] >> 3
        b = color[2] >> 3

        # place color bits in their expected places
        r0 = (r & 0x1) << 14
        g0 = (g & 0x1) << 13
        b0 = (b & 0x1) << 12
        r4 = ((r & 0x10) >> 4) << 11
        r3 = ((r & 0x8) >> 3) << 10
        r2 = ((r & 0x4) >> 2) << 9
        r1 = ((r & 0x2) >> 1) << 8
        g4 = ((g & 0x10) >> 4) << 7
        g3 = ((g & 0x8) >> 3) << 6
        g2 = ((g & 0x4) >> 2) << 5
        g1 = ((g & 0x2) >> 1) << 4
        b4 = ((b & 0x10) >> 4) << 3
        b3 = ((b & 0x8) >> 3) << 2
        b2 = ((b & 0x4) >> 2) << 1
        b1 = (b & 0x2) >> 1

        ng_color = r0 | g0 | b0 | r4 | r3 | r2 | r1 | g4 | g3 | g2 | g1 | b4 | b3 | b2 | b1

        c_palette += hex(ng_color)
        c_palette += ', '

    c_palette = c_palette[0:(len(c_palette) - 2)]
    c_palette += ' };'

    print(c_palette)


if __name__ == '__main__':
    ngpnginfo()
