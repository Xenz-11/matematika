#usr/bin/python2
#-*- coding: utf-8 -*-
import os,sys,re,time,random
k='\x1b[1;93m'
h='\x1b[1;92m'
p='\x1b[1;97m'
bm='\x1b[1;96m'
b='\x1b[1;95m'
xenz='''
{}Pilih Versi Matematika
{}Gw Saranin Pake python aja soalnya gw ga bisa coding php 😂

{}({}1{}) {}Php
{}({}2{}) {}Python
{}({}0{}) {}Exit
'''.format(h,b,k,p,k,bm,k,p,k,bm,k,p,k,bm)
def cl():
    os.system('clear')
def pilih():
    cl()
    print(xenz)
    p=int(input('\x1b[1;97m┌─[ \x1b[1;96mXENZ \x1b[1;97m]\n\x1b[1;97m└─▸ \x1b[1;93m'))
    if p == 1:
       cl()
       os.system('cd module\nphp mtk.php')
    elif p == 2:
         cl()
         os.system('cd module\npython2 mtk.py')
    elif p == 0:
         cl()
         sys.exit()
    else:
        print('\t\x1b[1;93m[\x1b[1;91m!\x1b[1;93m] \x1b[1;96mPilih Yg Benar Anj 😂')
        time.sleep(2)
        cl()
        pilih()
pilih()
