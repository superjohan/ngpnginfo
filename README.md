# ngpnginfo

## Extract Neo Geo color palette from a PNG

Usage: `pipenv run python3 ngpnginfo.py [filename]`

This program outputs a C array meant to be used with [ngdevkit](https://github.com/dciabrin/ngdevkit).

The program is pretty dumb currently: it assumes the palette is the same for every tile, and completely ignores the dark bit. But it's enough for my needs.

The tool expects indexed colors and only uses the first 16 colors of the palette.
