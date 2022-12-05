import pyembroidery as pe
import os
import sys

def split_pattern_by_color(filename: str) -> None:
    """Split embroidery file in one file per color block. 
    Appends underscore and number of color block to filename for each 
    color block.

    Args:
        filename (str): path to embroidery file. 
            Supports most common file extensions.

    Raises:
        ValueError: File does not exist.
    """
    if not os.path.exists(filename) or not os.path.isfile(filename):
        raise ValueError(
            f"File {filename} does not exist. "
            + "Please provide existing embroidery file as argument.")

    name, ext = os.path.splitext(filename)

    # load model
    f = pe.read(filename)
    # save model bounds
    x1,y1,x2,y2 = f.bounds()
    print("Bounds:", f.bounds())
    i = 0
    # iterate over colors
    for cb in f.get_as_colorblocks():
        # create pattern
        p = pe.EmbPattern()
        # add color block
        p.add_stitchblock(cb)
        # add jumps that any file has same borders
        p.add_stitch_absolute(pe.JUMP, x1, y1)
        p.add_stitch_absolute(pe.JUMP, x1, y2)
        p.add_stitch_absolute(pe.JUMP, x2, y1)
        p.add_stitch_absolute(pe.JUMP, x2, y2)
        # write file
        if f.count_color_changes() > 9: # two digits in filename
            pe.write(p,f"{name}_{i:02d}{ext}")
        else: # one digit in filename
            pe.write(p,f"{name}_{i}{ext}") 
        i+=1
    print("All done")


if __name__ == "__main__":
    # parse arguments
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
        if filename in {"-h", "--help"}:
            print(
    """
    Usage: python3 split_embroidery_file.py [options] FILENAME

    Script splits embroidery files in unique color blocks. 

    Arguments:
        FILENAME        /path/to/embroidery_file

    Options:
        -h, --help      show this help message and exit.
    """)
            exit()
    else:
        raise ValueError("Please provide embroidery file as argument.")

    # split embroidery file
    split_pattern_by_color(filename)