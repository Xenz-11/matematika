#usr/bin/python2
#-*- coding: utf-8 -*-
# Module Kontol
import os,sys,re,random,time
# author : Xenz
# github : https://github.com/Xenz-11
# facebook : Xenz Why
# whatsapp : 083138613993
## [ recode aja gapapa buat belajar lumayan nambah ilmu ^_^ ] ##
## [ maap kalo codinganya berantakan authornya agak tololπ ] ##
m='\x1b[1;91m'
h='\x1b[1;92m'
k='\x1b[1;93m'
b='\x1b[1;94m'
u='\x1b[1;95m'
bm='\x1b[1;96m'
p='\x1b[1;97m'
t='\x1b[8m'
mtk='''
\t{}_  _ {}___ {}_  _\n\t{}|\/| {} |  {}|_/\n\t{}|  | {} |  {}| \_
'''.format(m,k,h,m,k,h,m,k,h)
penjumlahan= '''
\t{}βββββββββββββββ\n\t{}β {}PENJUMLAHAN {}β\n\t{}βββββββββββββββ\n
'''.format(k,k,p,k,k)
pengurangan='''
\t{}βββββββββββββββ\n\t{}β {}PENGURANGAN {}β\n\t{}βββββββββββββββ\n
'''.format(h,h,p,h,h)
perkalian='''
\t{}βββββββββββββ\n\t{}β {}PERKALIAN {}β\n\t{}βββββββββββββ\n
'''.format(bm,bm,p,bm,bm)
pembagian='''
\t{}βββββββββββββ\n\t{}β {}PEMBAGIAN {}β\n\t{}βββββββββββββ\n
'''.format(b,b,p,b,b)
list='''
{}ββββββββββββββββββββββ\n{}β {}[{}1{}] {}Penjumlahan    {}β\n{}β {}[{}2{}] {}Pengurangan    {}β\n{}β {}[{}3{}] {}Perkalian      {}β\n{}β {}[{}4{}] {}Pembagian      {}β\n{}ββββββββββββββββββββββ
'''.format(m,m,k,p,k,bm,m,m,k,p,k,bm,m,m,k,p,k,bm,m,m,k,p,k,bm,m,m)
def cl():
    os.system('clear')
def menu():
    cl()
    print(mtk)
    print(list)
    xenzganz=int(input('\x1b[1;96mββ[ \x1b[1;92mXENZ \x1b[1;96m]\nβββΈ \x1b[1;93m'))
    if xenzganz == 1:
       cl()
       print(mtk)
       print(penjumlahan)
       xenz1=int(input('\x1b[1;92m Masukan Nilai βΈ \t\x1b[1;93m'))
       xenz2=int(input('\x1b[1;92m Di Tambah Berapa βΈ \t\x1b[1;93m'))
       hasil1=xenz1+xenz2
       print '\n''\t\x1b[1;93m' ,xenz1, '\x1b[1;97m+\x1b[1;93m' ,xenz2, '\x1b[1;97m=\x1b[1;93m' ,hasil1, '\n'
       bek=raw_input('\t\x1b[1;96m[ ENTER TO BACK ]')
       if bek =="" "":
          menu()
       else:                                                                
               menu()
    elif xenzganz == 2:
         cl()
         print(mtk)
         print(pengurangan)
         xenz3=int(input('\x1b[1;92m Masukan Nilai βΈ \t\x1b[1;93m'))
         xenz4=int(input('\x1b[1;92m Di Kurangi Berapa βΈ \t\x1b[1;93m'))
         hasil2=xenz3-xenz4
         print '\n''\t\x1b[1;93m' ,xenz3, '\x1b[1;97m-\x1b[1;93m' ,xenz4, '\x1b[1;97m=\x1b[1;93m' ,hasil2, '\n'
         bek=raw_input('\t\x1b[1;96m[ ENTER TO BACK ]')
         if bek =="" "":
          menu()
         else:                                                                
                 menu()
    elif xenzganz == 3:
         cl()
         print(mtk)
         print(perkalian)
         xenz5=int(input('\x1b[1;92m Masukan Nilai βΈ \t\x1b[1;93m'))
         xenz6=int(input('\x1b[1;92m Di Kali Berapa βΈ \t\x1b[1;93m'))
         hasil3=xenz5*xenz6
         print '\n''\t\x1b[1;93m' ,xenz5, '\x1b[1;97mΓ\x1b[1;93m' ,xenz6, '\x1b[1;97m=\x1b[1;93m' ,hasil3, '\n'
         bek=raw_input('\t\x1b[1;96m[ ENTER TO BACK ]')
         if bek =="" "":
          menu()
         else:                                                                
                 menu()
    elif xenzganz == 4:
         cl()
         print(mtk)
         print(pembagian)
         xenz7=int(input('\x1b[1;92m Masukan Nilai βΈ \t\x1b[1;93m'))
         xenz8=int(input('\x1b[1;92m Di Bagi Berapa βΈ \t\x1b[1;93m'))
         hasil4=xenz7/xenz8
         print '\n''\x1b[1;93m\t' ,xenz7, '\x1b[1;97mΓ·\x1b[1;93m' ,xenz8, '\x1b[1;97m=\x1b[1;93m' ,hasil4, '\n'
         bek=raw_input('\t\x1b[1;96m[ ENTER TO BACK ]')
         if bek =="" "":
          menu()
         else:                                                                
                 menu()
    else:
    	   print('\n\t\x1b[1;93m[ \x1b[1;96mPilih Yang Ada Di Menu Anj:( \x1b[1;93m]')
           time.sleep(2)
           menu()
menu()