#usr/bin/python2
#-*- coding: utf-8 -*-
# Module Kontol
import os,sys,re,random,time
# author : Xenz
# github : https://github.com/Xenz-11
# facebook : Xenz Why
# whatsapp : 083138613993
## [ recode aja gapapa buat belajar lumayan nambah ilmu ^_^ ] ##
## [ maap kalo codinganya berantakan authornya agak tolol😂 ] ##
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
\t{}┌─────────────┐\n\t{}│ {}PENJUMLAHAN {}│\n\t{}└─────────────┘\n
'''.format(k,k,p,k,k)
pengurangan='''
\t{}┌─────────────┐\n\t{}│ {}PENGURANGAN {}│\n\t{}└─────────────┘\n
'''.format(h,h,p,h,h)
perkalian='''
\t{}┌───────────┐\n\t{}│ {}PERKALIAN {}│\n\t{}└───────────┘\n
'''.format(bm,bm,p,bm,bm)
pembagian='''
\t{}┌───────────┐\n\t{}│ {}PEMBAGIAN {}│\n\t{}└───────────┘\n
'''.format(b,b,p,b,b)
list='''
{}┌────────────────────┐\n{}│ {}[{}1{}] {}Penjumlahan    {}│\n{}│ {}[{}2{}] {}Pengurangan    {}│\n{}│ {}[{}3{}] {}Perkalian      {}│\n{}│ {}[{}4{}] {}Pembagian      {}│\n{}└────────────────────┘
'''.format(m,m,k,p,k,bm,m,m,k,p,k,bm,m,m,k,p,k,bm,m,m,k,p,k,bm,m,m)
def cl():
    os.system('clear')
def menu():
    cl()
    print(mtk)
    print(list)
    xenzganz=int(input('\x1b[1;96m┌─[ \x1b[1;92mXENZ \x1b[1;96m]\n└─▸ \x1b[1;93m'))
    if xenzganz == 1:
       cl()
       print(mtk)
       print(penjumlahan)
       xenz1=int(input('\x1b[1;92m Masukan Nilai ▸ \t\x1b[1;93m'))
       xenz2=int(input('\x1b[1;92m Di Tambah Berapa ▸ \t\x1b[1;93m'))
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
         xenz3=int(input('\x1b[1;92m Masukan Nilai ▸ \t\x1b[1;93m'))
         xenz4=int(input('\x1b[1;92m Di Kurangi Berapa ▸ \t\x1b[1;93m'))
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
         xenz5=int(input('\x1b[1;92m Masukan Nilai ▸ \t\x1b[1;93m'))
         xenz6=int(input('\x1b[1;92m Di Kali Berapa ▸ \t\x1b[1;93m'))
         hasil3=xenz5*xenz6
         print '\n''\t\x1b[1;93m' ,xenz5, '\x1b[1;97m×\x1b[1;93m' ,xenz6, '\x1b[1;97m=\x1b[1;93m' ,hasil3, '\n'
         bek=raw_input('\t\x1b[1;96m[ ENTER TO BACK ]')
         if bek =="" "":
          menu()
         else:                                                                
                 menu()
    elif xenzganz == 4:
         cl()
         print(mtk)
         print(pembagian)
         xenz7=int(input('\x1b[1;92m Masukan Nilai ▸ \t\x1b[1;93m'))
         xenz8=int(input('\x1b[1;92m Di Bagi Berapa ▸ \t\x1b[1;93m'))
         hasil4=xenz7/xenz8
         print '\n''\x1b[1;93m\t' ,xenz7, '\x1b[1;97m÷\x1b[1;93m' ,xenz8, '\x1b[1;97m=\x1b[1;93m' ,hasil4, '\n'
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