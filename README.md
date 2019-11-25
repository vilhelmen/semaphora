# SEMAPHORA

![SEMAPHORA](semaphora.png "SEMAPHORA")

Generates [semaphore](https://en.wikipedia.org/wiki/Flag_semaphore) lettering SVGs in the style of the [peace symbol](https://en.wikipedia.org/wiki/Peace_symbols).

Writes output to directly to disk. Output will most likely look best in two character chunks. Supports `[A-Z0-9# ]+`.

Create a single symbol:

`./semaphora.py ND`

Create multiple symbols and concat:

`./semaphora.py SE MA PH OR A`


Template is easy-ish to edit, just pop the xml into draw.io and tweak. For best results, export all components as one SVG and separate components manually. Raises if ring and line svgs don't have the same size.
