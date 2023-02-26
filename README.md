# embroiderySplit

Small python script to split embroidery files by color, while keeping the
pattern bounds constant.
This script was written to deal with the error message:

> *This design is too large for the embroidery unit.*

which is thrown by the embroidery machine PFAFF creative 1.5 for file
sizes above 100 KB.

By splitting the embroidery file into smaller units it is possible to
embroider each color separately, which leads to smaller file sizes.

## Requirements

- pyembroidery

    ```bash
    python3 -m pip install pyembroidery
    ```

## Usage

To split your embroidery file into one file per color block use:

```bash
python3 embroidery_split.py filename
```

where `filename` is the path to the embroidery file to split.

For a list of all supported file extensions look at the [pyembroidery
GitHub page](https://github.com/EmbroidePy/pyembroidery).

## Known issues

Currently, there is a color change appended to all color blocks. 
There are no stitches in the new color, so you
can stop the embroidery at this point.
