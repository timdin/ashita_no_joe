# Written by Chanel Chen on 2017/01/25.
# Script Description:
# 1) FTP login
# 2) Place the file(s) from local to qfarok via ftp
# 3) Move the file(s) to another directory
# ---------------------------------------------------------------------------#
import ftplib
import os
import shutil


class Ftp():

    def __init__(self, user_name="", password=""):
        if user_name and password:
            self.ftp_login(user_name, password)
        else:
            raise Exception("User name and password should not be empty!")

    def ftp_login(self, user_name, password):
        # login #
        host = '10.145.177.28'
        print "Logging in..."
        try:
            self.session = ftplib.FTP(host, user_name, password)
            print "Successfully logged in with: " + user_name
            print self.session.getwelcome()
        except:
            raise Exception("Failed to Login with user: " + user_name)

    def ftp_place(self, cid, local_path = "C:\Automation\Upload File"):

        # go to the correct path in qfarok to copy EDI files #
        #TODO: if there are more then 1 cids in string "cid", then separate with ","
        qfarok_path = '/prod/edicomm/v4/' + cid + '/in'
        if self.session.pwd() != qfarok_path:
            self.session.cwd(qfarok_path)

        # copy file from local to qfarok via ftp #
        local_file_list = os.listdir(local_path)
        # will raise exception if the local folder is empty
        if (not local_file_list) or ["uploaded"]:
            self.disconnect()
            raise Exception("Please put your file in '" + local_path + "' before upload")
        print "Local Files: " + str(local_file_list)
        for local_file in local_file_list:
            ftp_file = qfarok_path + '/' + local_file
            if "." in local_file:
                lf = open(local_path + '/' + local_file, "rb")
                ff = "STOR " + ftp_file
                self.session.storbinary(ff, lf)
                print "Transfer completed for '" + local_file + "' in folder " + qfarok_path
                lf.close()

        # move files to another directory #
        uploaded_folder = local_path + '\uploaded'
        for local_file_move in local_file_list:
            if not os.path.exists(uploaded_folder):
                os.makedirs(uploaded_folder)
                print "Folder " + uploaded_folder + " created"
            if "." in local_file_move:
                shutil.copy2(local_path + "/" + local_file_move, uploaded_folder + '/' + local_file_move)
                os.remove(local_path + "/" + local_file_move)
                print("File moved: " + local_file_move)

    def disconnect(self):
        self.session.quit()
        print "Disconnected"


if __name__ == '__main__':
    # values to input
    # user_name = 'yrchen'
    user_name = 'clee'
    # password = 'Innova_0821'
    password = 'AsdAsd4589===='
    cid = 'VAH60142'

    uploader = Ftp(user_name, password)
    uploader.ftp_place(cid)
    uploader.disconnect()