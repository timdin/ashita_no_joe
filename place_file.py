import ftplib

class ftp():

    def __init__(self, user_name, password):
        self.ftp_login(user_name, password)

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
        qfarok_path = '/prod/edicomm/v4/'+cid+'/in'
        if self.session.pwd() != qfarok_path:
            self.session.cwd(qfarok_path)
        print "PATH: "+self.session.pwd()
        """
        # file to send
        file = open('kitten.jpg','rb')
        # send the file
        session.storbinary('STOR kitten.jpg', file)
        
        # close file and FTP
        file.close()     
        """
        self.session.quit()

if __name__ == '__main__':
    # values to input
    # user_name = 'yrchen'
    user_name = 'clee'
    # password = 'Innova_0821'
    password = 'AsdAsd4589===='
    cid = 'VAH60142'

    print "START placing file..."
    uploader = ftp()
    # ftp().ftp_upload(ftp().ftp_login(user_name, password), cid)
    uploader.ftp_login(user_name, password)
    uploader.ftp_upload(cid)
    print "FINISH placing file..."