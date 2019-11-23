# ngpnginfo

## Extract Neo Geo color palette from a PNG

This program outputs a C array meant to be used with [ngdevkit](https://github.com/dciabrin/ngdevkit).

The program is pretty dumb currently: it assumes the palette is the same for every tile, and completely ignores the dark bit. But it's enough for my needs.
