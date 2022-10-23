import argparse as ap
import re
from rembg import remove
from PIL import Image
parser=ap.ArgumentParser(description='Remove image background')
parser.add_argument('-i','--input',help='input image path')
args=vars(parser.parse_args())
if args['input']==None:
    print('bagi la input wei')
else:
    input=args['input']
    input=input.replace('\\','/')
    last_slash:int=0
    last_dot:int=0
    for slash in re.finditer('\/',input):
        last_slash=slash.start()
    filename=input[last_slash+1:]
    for dot in re.finditer('\.',filename):
        last_dot=dot.start()
    filename=filename[0:last_dot]+'-rembg.png'
    filepath=input[0:last_slash+1]+filename
    img=Image.open(input)
    output=remove(img)
    output.save(filepath)
    print('Image has been saved at '+filepath)
