import  zipfile
def unzip(way_from, way_to):
    zip = zipfile.ZipFile(way_from)
    zip.extractall(way_to)
    zip.close()


# by. Novikov