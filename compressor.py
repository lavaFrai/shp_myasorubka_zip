from zipfile import ZipFile


def zip(path_file, archive):
    zipObj = ZipFile(archive, 'w')
    zipObj.write(path_file)
    zipObj.close()
