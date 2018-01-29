# Written by Chanel Chen on 2018/01/26.
# Script Description:
# 1) Find out if the CID is Institutional or Professional
# 2) Run script in SSH
# ---------------------------------------------------------------------------#
import paramiko
import place_file


class SSH():

    def __init__(self, user_name, password):
        hostname = '10.145.177.28'
        self.ssh = paramiko.SSHClient()
        self.robot_print = "*WARN* "
        self.robot_info = "*INFO* "
        print "Logging in SSH..."
        try:
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname, port=22, username=user_name, password=password, timeout=30)
            print self.robot_print + "Successfully logged in SSH with: " + user_name
        except:
            raise Exception("Failed to Login SSH with user: " + user_name)

    def check_claim_type(self, check_cid):
        if check_cid[2] == "H":
            return "UB92"
        elif check_cid[2] == "P":
            return "1500"
        else:
            raise Exception("Can not find out the Claim type from CID: " + check_cid)

    def upload_file(self, cid):
        claim_type = self.check_claim_type(cid)
        go_to_folder = "cd user/local/bin"
        upload_script = "WN_IMPORT.EXEC %s %s"%(str(cid), str(claim_type))
        self.ssh.exec_command(go_to_folder)
        print self.robot_print + "Start Uploading Files..."
        self.ssh.exec_command(upload_script)
        print self.robot_print + ">>>SUCCESSFULLY UPLOAD FILE TO CID %s !<<<" % (str(cid))

if __name__ == '__main__':
    # values to input
    # user_name = 'yrchen'
    user_name = 'clee'
    # password = 'Innova_0821'
    password = 'AsdAsd4589===='
    cid = 'TXH20905'

    #TODO: write a loop there to input more then one cids
    ftp = place_file.FTP(user_name, password)
    ftp.ftp_place(cid)
    ftp.disconnect()
    print "------------------------------------"
    ssh = SSH(user_name, password)
    ssh.upload_file(cid)
    ftp.move_files()
