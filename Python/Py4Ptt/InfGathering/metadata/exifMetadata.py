from PIL.ExifTags import TAGS
from PIL import Image

def testForExif(imgFileName):
    try:
        exifData = {}
        imgFile = Image.open(imgFileName)
        info = imgFile._getexif()   # Extrae metadatos de una imagen
        if info:
            for (tag,value) in info.items():
                decoded = TAGS.get(tag,tag)
                exifData[decoded] = value
            exifGPS = exifData['GPSInfo']
            if exifGPS:
                print '[+] ' + imgFileName + ' GPS Data: ' + exifGPS
    except:
        pass
testForExif('<RUta de la imagen>')
