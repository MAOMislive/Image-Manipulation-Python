from pathlib import Path
from PIL import Image

inputPath = Path(r"C:\Users\PNG") # PNG(Source) Folder Location
inputFiles = inputPath.glob("**/*.png")
outputPath = Path(r"C:\Users\JPEG") # JPEG(Destination) Folder Location

for f in inputFiles:
    outputFile = outputPath / Path(f.stem + ".jpg")
    im = Image.open(f)
    if im.mode == 'RGBA':
        im = im.convert('RGB')
    im.save(outputFile)
