import os
from termcolor import colored, cprint
import jinja2

codepath = os.getcwd()
jinjadir = codepath+'/j2temps/'
outputdir = codepath+'/outdir/'

templateLoader = jinja2.FileSystemLoader( searchpath=jinjadir )
templateEnv = jinja2.Environment( loader=templateLoader )

CVIPCONFFILE = 'c6-c7-vip-001.conf.j2'
CVIPMASTERFILE = 'c6-c7-vip-common-master.j2'
CVIPSLAVEFILE = 'c6-c7-vip-common-slave.j2'
UMASTERFILE = 'ub-int-master.j2'
USLAVEFILE = 'ub-int-slave.j2'

tempcvipconf = templateEnv.get_template( CVIPCONFFILE )
tempcvipmaster = templateEnv.get_template( CVIPMASTERFILE )
tempcvipslave = templateEnv.get_template( CVIPSLAVEFILE )
tempumaster = templateEnv.get_template( UMASTERFILE )
tempuslave = templateEnv.get_template( USLAVEFILE )

ipadd = colored('IP address', 'green', attrs=['bold', 'underline'])
username = colored('username', 'green', attrs=['bold', 'underline'])
password = colored('password', 'magenta', attrs=['bold', 'underline'])
successfully = colored('successfully', 'green', attrs=['bold', 'underline'])
carp = colored('CARP', 'green', attrs=['bold', 'underline'])
ucarp = colored('UCARP', 'green', attrs=['bold', 'underline'])
centos = colored('CentOS', 'yellow', attrs=['bold', 'underline'])
freebsd = colored('FreeBSD', 'yellow', attrs=['bold', 'underline'])
ubuntu = colored('Ubuntu', 'yellow', attrs=['bold', 'underline'])
enter = colored('Enter', 'cyan', attrs=['bold', 'underline'])
server = colored('server', 'cyan', attrs=['bold', 'underline'])
