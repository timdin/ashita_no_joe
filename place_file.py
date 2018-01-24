import ftplib

class ftp():
    def ftp_login(user_name, password):
        # login
        host = '10.145.177.28'
        print "Logging in..."
        try:
            session = ftplib.FTP(host, user_name, password)
            print "Successfully logged in with: " + user_name
            print session.getwelcome()
        except:
            raise Exception("Failed to Login with user: " + user_name)
        return session

    def ftp_upload(session, cid, local_path = "C:\Automation\Upload File"):
        # go to the correct path to upload EDI files
        qfarok_path = '/prod/edicomm/v4/'+cid+'/in'
        if session.pwd() != qfarok_path:
            session.cwd(qfarok_path)
        print "PATH: "+session.pwd()
        """
        # file to send
        file = open('kitten.jpg','rb')
        # send the file
        session.storbinary('STOR kitten.jpg', file)
        
        # close file and FTP
        file.close()     
        """
        session.quit()

if __name__ == '__main__':
    # values to input
    # user_name = 'yrchen'
    user_name = 'clee'
    # password = 'Innova_0821'
    password = 'AsdAsd4589===='
    cid = 'VAH60142'

    print "START placing file..."
    ftp().ftp_upload(ftp().ftp_login(user_name, password), cid)
    print "FINISH placing file..."