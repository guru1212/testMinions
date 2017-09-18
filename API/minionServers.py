'''
Created on Sep 17, 2017

@author: gsethura
'''
import paramiko
import socket
class testMinions(object):
    '''
    Minions class to do operations mentioned in the payload
    '''
            
    def __init__(self):
        '''
        connect to VM
        '''
    def sshConnect(self, host, uname, pwd ):
        
        self.sshCl = paramiko.SSHClient()
        self.sshCl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print "Connecting"
        self.sshCl.connect( hostname = host, username = uname, password=pwd )        
        print "Connected"
        
    def sshMinion(self):
        stdin,stdout,stderr = self.sshCl.exec_command('ls')
        out = stdout.readlines()
        self.sshCl.close()
        return '\n'.join (out)
    
    def testsshMinion(self, commands):
        for operation in commands:
            for k,v in operation.items():
                print k, ":", v
                stdin,stdout,stderr = self.sshCl.exec_command(v)
                out = stdout.readlines()
                print out
        self.sshCl.close()
        return out