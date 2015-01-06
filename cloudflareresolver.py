# Follow me on twitter @EBKDev.
# Simple Cloudflare Resolver

import socket
print(' Coded by @EBKDev ')
site = raw_input("URL: ")
mainIP = socket.gethostbyname(site)
subdomains = ['mail.','direct.','cpanel.','ftp.','email.','server.','status.','forum.','portal?.','beta.','admin.','webmail.','imap.','pop.', 'ssl.','blog.','m.']

e,found = 0,0

print('\n'+site.upper()+': '+mainIP+'\n')

try:
    for sub in subdomains:
        e += 1
        try:
            x = socket.gethostbyname(sub+site)
            found += 1
            if len(sub) < 8:
                sub = str(sub) + (' ' * (8 - len(sub)) )
            print(sub.upper()+site+' - '+x)
        except: pass
    print('\nFOUND {0}/{1} IPs'.format(found,e))
except Exception as e: print e
