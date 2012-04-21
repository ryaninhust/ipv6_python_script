import socket
import fcntl
import struct
import os

def   get_ip_address(ifname):
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack('256s', ifname[:15]))[20:24])
   
interface = 'eth0'
ip = get_ip_address('eth0')
print 'DBG >>> current inet ip on %s : %s'%(interface,ip)

interface = 'sit1'

cmd = 'modprobe ipv6'
print 'RUN >>>',cmd
os.system(cmd)

cmd = 'ip tunnel add %s mode sit remote 59.66.4.50 local %s'%(interface,ip)
print 'RUN >>>',cmd
os.system(cmd)

cmd = 'ifconfig %s up'%(interface)
print 'RUN >>>',cmd
os.system(cmd)

cmd = 'ifconfig %s add 2001:da8:200:900e:0:5efe:%s/64'%(interface,ip)
print 'RUN >>>',cmd
os.system(cmd)

cmd = 'ip route add ::/0 via 2001:da8:200:900e::1 metric 1'
print 'RUN >>>',cmd
os.system(cmd)