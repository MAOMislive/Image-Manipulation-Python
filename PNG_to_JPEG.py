from pathlib import Path
from PIL import Image

inputPath = Path(r"C:\Users\User\Desktop\Images\PNG")
inputFiles = inputPath.glob("**/*.png")
outputPath = Path(r"C:\Users\User\Desktop\Images\JPEG")

for f in inputFiles:
    outputFile = outputPath / Path(f.stem + ".jpg")
    im = Image.open(f)
    if im.mode == 'RGBA':
        im = im.convert('RGB')
    im.save(outputFile)


print('Done Converting!')
