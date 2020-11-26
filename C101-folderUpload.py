# Uploads a folder to Dropbox
import dropbox
import os


class TransferData():
    def __init__(self, access_token):
        self.access_token = access_token

    def uploadFile(self, folderpath):
        dbx = dropbox.Dropbox(self.access_token)
        direc = os.walk(folderpath)
        (a, b, files) = direc.__next__()
        for file in files:
            source_path = folderpath + '/' + file
            dest_path = "/folderuploads/" + \
                folderpath.split("/")[-1] + '/' + file
            binaryfile = open(source_path, "rb").read()
            dbx.files_upload(binaryfile, dest_path)


def main():
    access_token = "ACCESS_TOKEN_HERE"
    td = TransferData(access_token)
    source_path = input("enter folder path")
    td.uploadFile(source_path)


main()
