import dropbox as da
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=da.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):

        relative_path = os.path.realpath(local_path, file_from)
        dropbox_path = os.path.join(file_to,relative_path)

        with open (local_path,'rb') as f:
            dbx.upload_files(f.read(), dropbox_path, mode=WriteMode('overwrite'))


def main():
    access_token = 'sl.BJVLBfcLu2u4l0EegvDK4xII0TpI-YqSpm1_lroKxytNznW7I3TLMfJ6-8jok748XjBA6hCpcaxILRDtPvt50O3CFwgD3_AoX1cGFfsBXi55ObKjYapv-0LyMLC75bPjPODC_mA4EqY6'
    transferData= TransferData(access_token)
    file_from=input("add your file")
    file_to='/jabinHw101.txt'
    print(transferData.upload_file(file_from,file_to))

if __name__=='__main__':
     main()


