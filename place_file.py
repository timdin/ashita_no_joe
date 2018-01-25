import ftplib, os, shutil, sys


class Ftp():

    def __init__(self, user_name="", password=""):
        if user_name and password:
            self.ftp_login(user_name, password)
        else:
            raise Exception("User name and password should not be empty!")

    def ftp_login(self, user_name, password):
        # login
        host = '10.145.177.28'
        print "Logging in..."
        try:
            self.session = ftplib.FTP(host, user_name, password)
            print "Successfully logged in with: " + user_name
            print self.session.getwelcome()
        except:
            raise Exception("Failed to Login with user: " + user_name)

    def ftp_upload(self, cid, local_path = "C:\Automation\Upload File"):
        # go to the correct path to upload EDI files
        #TODO: if there are more then 1 cids in string "cid", then separate with ","
        qfarok_path = '/prod/edicomm/v4/' + cid + '/in'
        if self.session.pwd() != qfarok_path:
            self.session.cwd(qfarok_path)
        print "PATH: "+self.session.pwd()

        # send file
        local_file_list = os.listdir(local_path)
        print "Local Files: " + str(local_file_list)
        for local_file in local_file_list:
            ftp_file = qfarok_path + '/' + local_file
            f = open(local_path + '/' + local_file, "rb")
            a = "STOR " + ftp_file
            self.session.storbinary(a, f)
            print "Transfer completed for " + local_file
            f.close()

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
    uploader.ftp_upload(cid)
    uploader.disconnect()