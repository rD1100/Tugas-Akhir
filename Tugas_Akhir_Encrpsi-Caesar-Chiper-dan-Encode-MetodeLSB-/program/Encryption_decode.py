from tkinter import *
from tkinter import ttk
import tkinter.filedialog
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox
from io import BytesIO
from numpy import array
import  os
import time
import cv2
import numpy as np

class Cc:
    output_image_size = 0
    def main(self,root):
        root.title("CAESAR CIPHER LSB")
        root.geometry("1600x700+0+0")
        f=Frame(root)
       # Tops = Frame(root,bg="black",width = 1600,height=50,relief=SUNKEN)
       # Tops.pack(side=TOP)
        title = Label(f,text='Implementasi Algoritma Caesar Cipher')
        title.config(font=('ariel',32,'bold'))
        title.pack(padx=200)
        
        titlee=Label( f,text='Dengan Menyembunyikan Pesan')
        titlee.config(font=('ariel',32,'bold'))
        titlee.pack()
        
        titleee=Label( f,text='Menggunakan Metode LSB  Pada Formulir')
        titleee.config(font=('ariel',32,'bold'))
      #  titleee.grid(row=1,column=3)
        titleee.pack()
        btnenenc=Button(f,relief=SOLID,cursor='hand2',text="Enkripsi & Encode",command= lambda :self.signup(f),padx=30)
        btnenenc.config(font=('ariel',24,'bold'))
        btnenenc.pack(pady=20)
        btndecen=Button(f,relief=SOLID,cursor='hand2',text="Dekripsi & Decode",command=lambda : self.frame2_decode(f),padx=30)
        btndecen.config(font=('ariel',24,'bold'))
        btndecen.pack(pady=5)
        f.grid()
        root.mainloop()

    def home(self,frame):
        frame.destroy()
        self.main(root)
        


    def frame2_decode(self,f):
        root.geometry("1600x700+0+0")
        root.title("HASIL DECODE")
        d_f3 = Frame(root)
        f.destroy()
       # knc=int(txdk.get())
       # rslt=""
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        if not myfile:
            messagebox.showerror("Error","Maaf anda belum pilih sama sekali !")
        else:
            myimg = Image.open(myfile, 'r')
            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            l4= Label(d_f3,text='Gambar Decode :')
            l4.config(font=('courier',18,'bold'))
            l4.grid(row=0, column=0)
            panel = Label(d_f3, image=img,cursor= 'hand2')
            panel.bind("<Button-1>",lambda e: [self.gmbrDec(d_f3,myimg)])
            panel.image = img
            panel.grid(row=1,column=0)
            hidden_data = self.decode(myimg)
           # data_smbny=open(hidden_data,'r')
            #r_data=data_smbny.read()
            l2 = Label(d_f3, text='Pesan tersembunyi :')
            l2.config(font=('courier',18,'bold'))
            l2.grid(row =2,column=0)
            text_psn = Text(d_f3, width=40, height=9)
            text_psn.insert(INSERT, hidden_data)
            text_psn.configure(state='disabled')
            text_psn.config(font=('ariel',16))
            text_psn.grid(row=3,column=0,padx=20)  
            l3=Label(d_f3,text='Kunci Dekripsi:')
            l3.config(font=('courier',18,'bold'))
            l3.grid(row=4,column=0)
            txt_dkrp=Entry(d_f3,width=40,show='*')
            txt_dkrp.config(font=('ariel',16,))
            txt_dkrp.grid(row=5,column=0,padx=20)

            ar= array(myimg)
    
            lbx=Label(d_f3,text='Nilai Matriks Gambar :')
            lbx.config(font=('courier',18,'bold'))
            lbx.grid(row= 0,column= 1)
            txx=Text(d_f3,width= 45,height= 10)
            txx.insert(INSERT,ar)
            txx.configure(state= 'disabled')
            txx.config(font=('ariel',16))
            txx.grid(row= 1,column= 1)
            fle_tx= open('E:/my own/Semester 9/TA/sample/decpros.txt','r')
            r_fle=fle_tx.read()
            fle_tx.close()
            l5= Label(d_f3,text='Proses Ekstrasi :')
            l5.config(font=('courier',18,'bold'))
            l5.grid(row=2, column=1)
            text_psnn = Text(d_f3, width=45, height=10)
            text_psnn.insert(INSERT, r_fle)
            text_psnn.configure(state='disabled')
            text_psnn.config(font=('ariel',16))
            text_psnn.grid(row=3, column=1,padx=20,pady=2)

           # txt_dkrp.configure(state='disabled')
            back_button = Button(d_f3,relief=SOLID,cursor='hand2', text='Dekripsi', command= lambda :self.kydekrp(d_f3,txt_dkrp,text_psn))
            back_button.config(font=('ariel',16,'bold'))
            back_button.grid(row=7,column=1)
            btnky=Button(d_f3,relief=SOLID,cursor='hand2',text='Kembali',command=lambda :Cc.home(self,d_f3))
            btnky.config(font=('ariel',16,'bold'))
            btnky.grid(row=7,column=0)
            #back_button.grid()
            d_f3.grid()
            #root.mainloop()
    
    def gmbrDec(self,d_f3,myimg):
        dc=Tk()
        dc.geometry("700x500+0+0")
        dc.title('NILAI MATRIX GAMBAR DECODE')
        #ep.destroy()
        abc=[]
        gmbr=myimg. copy()
        ar= array(gmbr)
       
       # b=len(abc)
        #for i in ar :
           #  abc.append(format((ar,'08b'))

           # print("append:",abc)
        #print("len :",b)
        #for a in b :
           ## ab= ar % 2
            #print("biner ab :",ab)
      #  argmbr.append(ar)
        lbx=Label(dc,text='Nilai Matriks Gambar :')
        lbx.config(font=('courier',18,'bold'))
        lbx.grid(row= 0,column= 0)
        txx=Text(dc,width= 40,height= 10)
        txx.insert(INSERT,ar)
        txx.configure(state= 'disabled')
        txx.config(font=('ariel',16))
        txx.grid(row= 1,column= 0)
       # back= Button(mx,text='Kembali',command=lambda :Cc.home_enc(self,mx))
      #  back.config(font=('ariel',14,'bold'))
       # back.grid(row= 4,column= 0)
        dc.mainloop()

    def kydekrp(self,d_f3,txt_dkrp,text_psn):
        #root.title("Hasil Dekripsi")
        root.geometry("1600x700+0+0")
        #abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        root.title(" DEKRIPSI  ")
        dk=Frame(root)
        
        dkrp=int(txt_dkrp.get())
        psn_dkrp=text_psn.get("1.0", "end-1c")
       
        tmbh="-"
        mod="mod"
        kr1="("                                                                 
        kr2=")"
        sps=" "
        equal="="
        t2=":"
        nl="26"
        tn="10"
        decW=open("E:/my own/Semester 9/TA/sample/dec.txt","w")
        decrypted=""
        for c in psn_dkrp:

                        if c.isupper(): #check if it's an uppercase character

                            c_index = ord(c) - ord('A')
                            # shift the current character by kcc positions
                            c_shifted = (c_index - dkrp) % 26 + ord('A')
                            c_new = chr(c_shifted)
                            decrypted += c_new
                            a=ord('A')
                            eq=str(c)+sps+t2+sps+kr1+str(c_index)+sps+tmbh+sps +str(dkrp)+sps+kr2+sps+mod+sps+nl+sps+tmbh+str(a)+equal+sps+str(c_shifted)+equal+sps+str(decrypted)
                            decW.write(eq)
                            
                            decW.write("\n")
                        elif c.islower(): #check if its a lowecase character
                            
                            # subtract the unicode of 'a' to get index in [0-25) range
                            c_index = ord(c) - ord('a') 
                            c_shifted = (c_index - dkrp) % 26 + ord('a')
                            c_new = chr(c_shifted)
                            decrypted += c_new
                            b=ord('a')
                            ee=str(c)+sps+t2+sps+kr1+str(c_index)+sps+tmbh+sps +str(dkrp)+sps+kr2+sps+mod+sps+nl+sps+tmbh+str(b)+equal+sps+str(c_shifted)+equal+sps+str(decrypted)
                            decW.write(ee)
                            decW.write("\n")
                        elif c.isdigit():

                            # if it's a number,shift its actual value 
                            c_new = (int(c) - dkrp) % 10
                            decrypted += str(c_new)
                            d=int(c)
                            er=str(c)+sps+t2+sps+kr1+str(d)+sps+tmbh+sps +str(dkrp)+sps+kr2+sps+mod+sps+tn+sps+equal+sps+str(c_new)+equal+sps+str(decrypted)
                            decW.write(er)
                            #encWrite.close()
                            decW.write("\n")
                        else:

                            # if its neither alphabetical nor a number, just leave it like that
                            decrypted += c        
        lblky=Label(dk,text='Hasil Dekripsi :',cursor= 'hand2')
        lblky.bind("<Button-1>",lambda e: [self.cgm1(dk)])
        lblky.config(font=('courier',18,'bold'))
        lblky.grid(row=1,column=0)
        txdk=Text(dk,width=40,height=20)
        txdk.insert(INSERT,decrypted)
        txdk.configure(state='disabled')
        txdk.config(font=('ariel',16))
        txdk.grid(row=2,column=0,padx=20,pady=20)
        btnkyy=Button(dk,relief=SOLID,cursor='hand2',text='Kembali',command=lambda :Cc.home(self,dk))
        btnkyy.config(font=('ariel',16,'bold'))
        btnkyy.grid(row=4,column=0)
        tnky=Button(dk,relief=SOLID,cursor='hand2',text='Simpan',command=lambda :self.smpanDk(txdk))
        tnky.config(font=('ariel',16,'bold'))
        tnky.grid(row=4,column=1)
        d_f3.destroy()
        dk.grid()
        
    def smpanDk(self,txdk):
        w_dk=open('E:/my own/Semester 9/TA/sample/Hasil_Dekripsi.txt','w')
        w_dk.write(txdk.get(1.0,END))
        messagebox.showinfo("Berhasil","Selamat, file text hasil dekripsi berhasil di simpan")
    def cgm1(self,dk):
        
        w = open("E:/my own/Semester 9/TA/sample/dec.txt",'r')
        rW=w.read()
        w.close()
        
        lblkyy=Label(dk,text='Proses Dekripsi :')
        lblkyy.config(font=('courier',18,'bold'))
        lblkyy.grid(row=1,column=1)
        mtx= Text(dk,width= 45,height=20)
        mtx.insert(INSERT,rW)
        mtx.configure(state='disabled')
        mtx.config(font=('ariel',16))
        mtx.grid(row=2,column=1,padx=20,pady=20)
  
    def decode(self, image):
        data = ''
        imgdata = iter(image.getdata())
        encWrite= open('E:/my own/Semester 9/TA/sample/decpros.txt','w')
        
        while (True):
            pixels = [value for value in imgdata.__next__()[:3] +
                      imgdata.__next__()[:3] +
                      imgdata.__next__()[:3]]
            
            binstr = ''
            for i in pixels[:8]:
                if i % 2 == 0:
                    binstr += '0'
                else:
                    binstr += '1'
               # print('i :',i)
                encWrite.write("Nilai Piksel :")
                encWrite.write(str(i))
                encWrite.write("\n")
                encWrite.write("Biner :")
                encWrite.write(binstr)
                encWrite.write("\n")
               # print("binstr",binstr)
           
            data += chr(int(binstr, 2))
            encWrite.write("Hasil :")
            encWrite.write(data)
            encWrite.write("\n")
     
           
            if pixels[-1] % 2 != 0:
                
                return data
            #print("pixels",pixels)

    def signup(self,f):
        f.destroy()
        
        root.title('REGISTRASI ')
        f = ('ariel',20)
        s=Frame(
            root, 
            bd=2, 
            bg='#CCCCCC',
            relief=SOLID, 
            padx=10, 
            pady=10
            )
        check_counter=0
        warn = ""
   
        title=Label(s,
        text='Formulir Pendaftaran : ',bg='#CCCCCC',
        
        )

        title.bind("<Button-1>",lambda e: [self.wrt(txt_q,tW,txt_qq,txt_qqQ)])
        title.config(font=('ariel',20,'bold'))
        title.grid(row=0,column=1, sticky=W, pady=10)
        Label(s,
        text='Nama :',
        bg='#CCCCCC',
        font=f
        ).grid(row=1, column=0, sticky=W, pady=10)
        txt_q=Entry(s, font=f)
        txt_q.grid(row=1, column=1, pady=10, padx=20) 
        #txx.append(txt_q)
        if  txt_q.get() == "":
            warn = "Maaf nama anda masih kosong"
        else:
            check_counter += 1
        check_counter=0
        Label(s,text='Email :',
         bg='#CCCCCC',
         font=f
         ).grid(row=2, column=0, sticky=W, pady=10)
        tW=Entry(s, font=f)
        tW.grid(row=2, column=1, pady=10, padx=20)
        Label(s,
        text='Password:', 
        bg='#CCCCCC',
        font=f
        ).grid(row=3, column=0, sticky=W, pady=10)
        txt_qq=Entry(s,show='*', font=f)
        txt_qq.grid(row=3,column=1, pady=10, padx=20)
        Label(s,
        text='Nomor Handphone :',
        font=f,
        bg='#CCCCCC'
        ).grid(row=4, column=0, sticky=W, pady=10)
        txt_qqQ=Entry(s, font=f)
        txt_qqQ.grid(row=4,column=1, pady=10, padx=20)
       
        if  tW.get() == "":
            warn = "Maaf email anda masih kosong"
        else:
            check_counter += 1

        if  txt_qqQ.get() == "":
            warn = "Maaf nomor handphone anda masih kosong"
        else:
            check_counter += 1

        if txt_qq.get() == "":
            warn = "Maaf password anda masih kosong"
        else:
            check_counter += 1
        
        pross=Button(s,relief=SOLID,cursor='hand2',text='Proses',command=lambda : [self.enenc(s)])
        pross.config(font=('ariel',16,))
        pross.grid(row=12, column=2, pady=10, padx=20)
        cncl=Button(s,relief=SOLID,cursor='hand2',text='Kembali',command=lambda :[Cc.home(self,s)])
        cncl.config(font=('ariel',16))
        cncl.grid(row=12,column=0, pady=10, padx=20)
        s.pack()

    def wrt(self,txt_q,tW,txt_qq,txt_qqQ):
        
        encWrite= open('E:/my own/Semester 9/TA/sample/registrasi.txt','w')
       # encWrite.close()
        ''''
        a=txt_q.get('1.0', 'end-1c')
        aa=tW.get('1.0', 'end-1c')
        aaa=txt_qq.get('1.0', 'end-1c')
        a1=txt_qqQ.get('1.0', 'end-1c')
        '''
        encWrite.write("Nama :")
        encWrite.write(txt_q.get())
        encWrite.write("\n")
        
        encWrite.write("Email :")
        encWrite.write(tW.get())
        encWrite.write("\n")
        
        encWrite.write("Password :")
        encWrite.write(txt_qq.get())
        encWrite.write("\n")
        
        encWrite.write("Nomor Handphone :")
        encWrite.write( txt_qqQ.get())
        encWrite.write("\n")
  
    def enenc(self,s):
        s.destroy()
        f3 = Frame(root)
        root.geometry("1600x700+0+0")
        root.title('FORM ENKRIPSI  :')
        with open('E:/my own/Semester 9/TA/sample/registrasi.txt','r') as fle_tx:
            r_fle=fle_tx.read()
            fle_tx.close()
            tx = Label(f3,text='Pesan:')
            tx.config(font=('courier',18,'bold'))
            tx.pack()
            txbox = Text(f3,width=55,height=15)
            txbox.insert(INSERT,r_fle)
            txbox.configure(state='disabled')
            txbox.config(font=('ariel',16))
            txbox.pack(fill=BOTH,expand=True,padx=200)
            ky = Label(f3,text='Kunci :')
            ky.config(font=('courier',18,'bold'))
            ky.pack()
            kybox = Entry(f3,show='*',width=50)
            kybox.config(font=('ariel',16))
            kybox.pack(pady=20)
            pross=Button(f3,relief=SOLID,cursor='hand2',text='Kembali',command=lambda :[Cc.home(self,f3)])
            pross.config(font=('ariel',16,'bold'))
            pross.pack(side=LEFT,padx=250,ipadx=30)
            cncl=Button(f3,relief=SOLID,cursor='hand2',text='Proses',command=lambda :self.frame2_encode(f3,txbox,kybox))#
            cncl.config(font=('ariel',16,'bold'))
            cncl.pack(side=LEFT,padx=300)
        f3.grid()
    def frame2_encode(self,f3,txbox,kybox):
        root.geometry("1600x700+0+0")
        root.title('HASIL ENKRIPSI DAN GAMBAR ENCODE ')
        ep= Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        psn=txbox.get("1.0", "end-1c")
        kcc=int(kybox.get())
        if not myfile:
            messagebox.showerror("Error","Maaf anda belum pilih sama sekali!")
        else:
            myimg = Image.open(myfile)
            myimage = myimg.resize((300,200))
            img = ImageTk.PhotoImage(myimage)
            l3= Label(ep,text='Gambar Encode')
            l3.bind("<Button-1>",lambda e: [self.matrx(ep,encrypted)])
            l3.config(font=('courier',18,'bold'))
            l3.grid(row=0,column=0)
            panel = Label(ep, image=img,cursor= 'hand2')
            panel.image = img
            self.output_image_size = os.stat(myfile)
            self.o_image_w, self.o_image_h = myimg.size
            panel.grid(row=1,column=0)
            encWrite= open('E:/my own/Semester 9/TA/sample/enc.txt','w')
            tmbh="+"
            mod="mod"
            kr1="("
            kr2=")"
            sps=" "
            equal="="
            t2=":"
            nl="26"
            tn="10"
            encrypted = ""
            for c in psn:
                if c.isupper(): #check if it's an uppercase character
                    c_index = ord(c) - ord('A')
                    c_shifted = (c_index + kcc) % 26 + ord('A')
                    c_new = chr(c_shifted)
                    encrypted += c_new
                    a=ord('A')
                    eq=str(c)+sps+t2+sps+kr1+str(c_index)+sps+tmbh+sps +str(kcc)+sps+kr2+sps+mod+sps+nl+sps+tmbh+str(a)+equal+sps+str(c_shifted)+equal+sps+str(encrypted)
                    encWrite.write(eq)
                    
                    encWrite.write("\n")
                elif c.islower(): #check if its a lowecase character
                    c_index = ord(c) - ord('a') 
                    c_shifted = (c_index + kcc) % 26 + ord('a')
                    c_new = chr(c_shifted)
                    encrypted += c_new
                    b=ord('a')
                    ee=str(c)+sps+t2+sps+kr1+str(c_index)+sps+tmbh+sps +str(kcc)+sps+kr2+sps+mod+sps+nl+sps+tmbh+str(b)+equal+sps+str(c_shifted)+equal+sps+str(encrypted)
                    encWrite.write(ee)
                    encWrite.write("\n")
                elif c.isdigit():
                    c_new = (int(c) + kcc) % 10
                    encrypted += str(c_new)
                    d=int(c)
                    er=str(c)+sps+t2+sps+kr1+str(d)+sps+tmbh+sps +str(kcc)+sps+kr2+sps+mod+sps+equal+sps+str(c_new)+equal+sps+str(encrypted)
                    encWrite.write(er)
                    encWrite.write("\n")
                else:
                    encrypted += c
            l2 = Label(ep, text='Pesan Enkripsi',cursor= 'hand2')
            l2.bind("<Button-1>",lambda e: [self.cgm(ep)])
            l2.config(font=('courier',18,'bold'))
            l2.grid(row=2,column=0)
            text_area = Text(ep, width=40, height=10)
            text_area.insert(INSERT,encrypted)
            text_area.configure(state='disabled')
            text_area.config(font=('ariel',16))
            text_area.grid(row=3,column=0,padx=10,pady=20)
            data = text_area.get("1.0", "end-1c")
            wAr= open('E:/my own/Semester 9/TA/sample/arrAymg.txt','w')
            ar= array(myimg)
            '''
            z=ar.reshape(tuple(d for d in ar.shape if d > 1))
          #  arr=str(z)
            for x in z:
                for y in x:
                   # print(y, end=' ')
                    wAr.write(y)
                #print()
            
           # arr=np.hstack((ar))
           '''
            lbx=Label(ep,text='Nilai Matriks Gambar :')
            lbx.config(font=('courier',18,'bold'))
            lbx.grid(row= 0,column= 1)
            txx=Text(ep,width= 45,height= 10)
            txx.insert(INSERT,ar  )
            txx.configure(state= 'disabled')
            txx.config(font=('ariel',16))
            txx.grid(row= 1,column= 1)       
            sav_button=Button(ep,relief=SOLID,cursor='hand2',text='Simpan ',command=lambda : [self.sav_flenc(ep,text_area)])
            sav_button.config(font=('ariel',14,'bold'))
            sav_button.grid(row=5,column=1,padx=20)
            back_button = Button(ep,relief=SOLID,cursor='hand2', text='Encode', command=lambda : [self.enc_fun(myimg),self.pict_enc(ep)])
            back_button.config(font=('ariel',14,'bold'))
            back_button.grid(row=5,column=2,padx=20)
            encode_button = Button(ep,relief=SOLID,cursor='hand2', text='Kembali', command=lambda : Cc.home(self,ep))
            encode_button.config(font=('ariel',14,'bold'))
            encode_button.grid(row=5,column=0,padx=20)
            ep.grid()
            f3.destroy()
   # argmbr= []

    def enco(self):
        w = open("E:/my own/Semester 9/TA/sample/enc.txt",'r')
        rW=w.read()
        w.close()
        return rW

    def sav_flenc(self,ep,text_area):
        #tx_en=text_area.get("1.0", "end-1c")
        w_fle=open('E:/my own/Semester 9/TA/sample/hiddenMessage.txt','w')
        w_fle.write(text_area.get(1.0,END))
        #encWrite= open('E:/my own/Semester 9/TA/sample/encR.txt','w+')
       # encWrite.write(eq)
       #encWrite.write("\n")
        messagebox.showinfo("Berhasil","Selamat, file text enkripsi berhasil di simpan")
        #w_fle.save(tkinter.filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('txt','*txt')]),defaultextension=".txt"))

    def manualTung(self,pc):
        mn=Tk()
        mn.geometry("700x700+0+0")
        mn.title('HITUNGAN MANUAL PENYISIPAN KARAKTER KE GAMBAR')
       # dataEnc=tkinter.filedialog.askopenfilename(filetypes = ([('txt', '*.txt'),('All Files', '*.*')]))    
        daEnc=open('E:/my own/Semester 9/TA/sample/carakterBiner.txt','r')
        dat=daEnc.read()
        daEnc.close()
       
       # bn=[]

        lb=Label(mn,text=('karakter ke biner :'))
        lb.config(font=('courier',20,'bold'))
        lb.grid(row=1,column= 0)
        '''
        for i in dat :
            #bn='',join(format(ord(i), '08b')
            bn.append(format(ord(i),'08b' ))
            a=ord(i)
            #print(i)  
            sps=" "
            equal="="
            aS="ASCI"
            biN="BINER"
            ch="CHIPER"
            ci=ch+sps+equal+sps+str(i)
            rm=aS+sps+equal+sps+str(a)
            bner=biN+sps+equal+sps+str(bn)
          #  lb_mn3=Label(mn,text=ci)   
            #lb_mn3.config(font=('courier',15,'bold'))  
          #  lb_mn3.grid() 
           # lb_mn2=Label(mn,text=rm)
           # lb_mn2.config(font=('courier',15,'bold'))  
           # lb_mn2.grid() 
           # lb_mn=Label(mn,text=bner)
           # lb_mn.config(font=('courier',15,'bold'))  
            self.cgm(mn,ci,rm,bner)
            '''
        #ocgm=open('E:/my own/Semester 9/TA/sample/carakterBiner.txt','r')
       # rcbn=ocgm.read()
        #ocgm.close()
        tCbm = Text(mn, width=50, height=20)
        tCbm.insert(INSERT,dat)
        tCbm.configure(state='disabled')
        tCbm.config(font=('ariel',16))
        tCbm.grid(row=2,column=0)
           # lb_mn.grid() 
           #lb_mn1=Label(mn,text=bn)
           # lb_mn1.config(font=('courier',15,'bold'))     
            #lb_mn1.grid()                                                                            
          #  print("ASCI :",a)
        mn.mainloop()
           
           # 
           # ("newd:",bn)
    
    def cgm(self,ep):
        '''
        wCgm= open('E:/my own/Semester 9/TA/sample/carakterBiner.txt','w')
        wCgm.write(ci)
        wCgm.write("\n")
        wCgm.write(rm)
        wCgm.write("\n")
        wCgm.write(bner)
        '''
        w = open("E:/my own/Semester 9/TA/sample/enc.txt",'r')
        rW=w.read()
        lb2=Label(ep,text=('Perhitungan Enkripsi :'))
        lb2.config(font=('courier',20,'bold'))
        lb2.grid(row=2,column= 1)
        mtx= Text(ep,width= 45,height=10)
        mtx.insert(INSERT,rW)
        mtx.configure(state='disabled')
        mtx.config(font=('ariel',16))
        mtx.grid(row=3,column=1,padx=30,pady=20)

    def pict_enc(self,ep):
        root.geometry("1600x700+0+0")
        root.title("GAMBAR DAN PESAN SETELAH ENCODING")
        pc=Frame(root)
        myfile = tkinter.filedialog.askopenfilename(filetypes = ([('png', '*.png'),('jpeg', '*.jpeg'),('jpg', '*.jpg'),('All Files', '*.*')]))
        
        if not myfile:
            messagebox.showerror("Error","Maaf anda belum pilih sama sekali !")
        else:
            
            #dataItung=self.manualTung(dat)
            myimg = Image.open(myfile, 'r')
            myimage = myimg.resize((300, 200))
            img = ImageTk.PhotoImage(myimage)
            lb_pic= Label(pc,text='Gambar Stego Image :')
            lb_pic.config(font=('courier',18,'bold'))
            lb_pic.grid( row=0,column=0)
            panel = Label(pc, image=img,cursor= 'hand2')
            panel.image = img
            panel.grid(row=1,column=0)
            arr= array(myimg)
            arrr=np.hstack((arr))
            lb_mt = Label(pc, text='Matriks gambar :')
            lb_mt.config(font=('courier',18,'bold'))
            lb_mt.grid(row=2,column=0)
            tx_mt = Text(pc, width=40, height=9)
            tx_mt.insert(INSERT, arr)
            tx_mt.configure(state='disabled')
            tx_mt.config(font=('ariel',16))
            tx_mt.grid(row=3,column=0,padx=20)  
            daEnc=open('E:/my own/Semester 9/TA/sample/carakterBiner.txt','r')
            dat=daEnc.read()
            daEnc.close()
        lb=Label(pc,text=('Karakter ke Biner :'))
        lb.config(font=('courier',20,'bold'))
        lb.grid(row=0,column= 1)  
        tCbm = Text(pc, width=45, height=10)
        tCbm.insert(INSERT,dat)
        tCbm.configure(state='disabled')
        tCbm.config(font=('ariel',16))
        tCbm.grid(row=1,column=1)
        
        oRgb=open('E:/my own/Semester 9/TA/sample/binerRgb.txt','r')
        rRgb=oRgb.read()
        lRgb= Label(pc,text='Biner ke Nilai Pixel :')
        lRgb.config(font=('courier',18,'bold'))
        lRgb.grid( row=2,column=1)
        tRgb = Text(pc, width=45, height=10)
        tRgb.insert(INSERT, rRgb)
        tRgb.configure(state='disabled')
        tRgb.config(font=('ariel',16))
        tRgb.grid(row=3,column=1,padx=20)  


        kmbl_button = Button(pc,relief=SOLID,cursor='hand2', text='Kembali', command=lambda : Cc.home(self,pc))
        kmbl_button.config(font=('ariel',14,'bold'))
        kmbl_button.grid()
        pc.grid(pady=15)
        ep.destroy()

    def matrx(self,ep,encrypted):
        mx=Tk()
        mx.geometry("300x200+0+0")
        mx.title('Jumlah Huruf')
      #  arList=[]
        #ep.destroy()
      #  a=len(encrypted)
        #rsl=j
      #  argmbr.append(ar)
        lbx=Label(mx,text='Jumlah Karakter :')
        lbx.config(font=('courier',18,'bold'))
        lbx.grid(row= 0,column= 0)
        #for i in ar :
            #for j in i :
               # txx=Label(mx,text=j)
               # txx.grid()
        txx=Text(mx,width= 10,height= 1)
        txx.insert(INSERT,len(encrypted))
        txx.configure(state= 'disabled')
        txx.config(font=('ariel',16))
        txx.grid(row= 0,column= 1)
       # back= Button(mx,text='Kembali',command=lambda :Cc.home_enc(self,mx))
      #  back.config(font=('ariel',14,'bold'))
       # back.grid(row= 4,column= 0)
        mx.grid()

    def rms_enc(self,ep,kcc): 
        rm=Tk()
        rm.geometry("700x650+0+0")
        rm.title('PERHITUNGAN MANUAL ENKRIPSI')
        #v_rm=str(lb_enc)
      #  q_rm=int(ki.get("1.0", "end-1c"))
        abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
        global psn
        global kc
        psn=txx[0]
        #kc=kyy[0]
       # knc=""
      #  knc=kyy
        w = open("E:/my own/Semester 9/TA/sample/enc.txt",'r')
        rW=w.read()
        w.close()
        knci=kcc
        hasil=""
        #kcy=int(kyy.get())
       # print("pesan :",knci)
        lbed=Label(rm,text=('Alfabet Caesar Chiper :'))
        lbed.config(font=('courier',20,'bold'))
        lbed.grid(row=0,column=0)
        #while i<10:
        #lbabjd=Label(rm,text=bd1)
        #lbabjd.config(font=('courier',18,'bold'))
           # i+=1
        #lbabjd.grid(row=1,column=0)

       # while i<11:
            #lbabjd=Label(rm,text=bd2[i])
            #lbabjd.config(font=('courier',18,'bold'))
            #i+=1
           #lbabjd.grid(row=2,column=i)
        tbl=ttk.Treeview(rm,show='headings',height=8)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=('courier', 200))
        tbl['columns']=('Alfabet','Value')
        #tbl.column('#0',width=0,stretch=NO)
        tbl.column('Alfabet',anchor=CENTER,width=150)
        #tbl.column('Name',anchor=CENTER)
        tbl.column('Value',anchor=CENTER,width=150)
        
        #tbl.heading('#0',text='q',anchor=CENTER)
      #  tbl.heading('Alfabet',text='Id',anchor=CENTER)
        tbl.heading('Alfabet',text='Alfabet',anchor=CENTER)
        tbl.heading('Value',text='Nilai',anchor=CENTER)
        #sb=Scrollbar(rm,oriental=VERTICAL)
      # sb.grid(row=1,column=1)

        for q in range (len(abjad)):
            tbl.insert(parent='',index=q,iid=q,text='',values=(abjad[q],q))
           # tbl.config(font=('courier',18,'bold'))
        #tbl.insert(parent='',index=1,iid=1,text='',values=('','B','1'))
        tbl.grid(row=1,column=0)
        lb2=Label(rm,text=('Perhitungan Enkripsi :'))
        lb2.config(font=('courier',20,'bold'))
        lb2.grid(row=3,column= 0)
        '''
        for karakter in psn:
            nl=len(abjad)
            tmbh="+"
            mod="mod"
            kr1="("
            kr2=")"
            sps=" "
            equal="="
            t2=":"
            if karakter in abjad:
                index_lama = abjad.index(karakter)
                index_baru = (index_lama + knci ) % len(abjad)
                abjad_baru = abjad[index_baru]
                hasil = hasil + abjad_baru 
                eq=str(karakter)+sps+t2+sps+kr1+str(index_lama)+sps+tmbh+sps +str(knci)+sps+kr2+sps+mod+sps+str(nl)+sps+equal+sps+str(index_baru)+equal+sps+str(hasil)
               # print(eq)
                lb_enc=Label(rm,text=eq)
              #  rm.update()
               # time.sleep(2)
                lb_enc.config(font=('courier',15,'bold'))
                    #for i in range (len (tks)):
                #for i in range(len(tks)):
               # lb_enc.grid()
        #Label(rm,text=v_rm).grid()
        '''
        rms=Text(rm,width= 70,height= 15)
        rms.insert(INSERT,rW)
        rms.configure(state='disabled')
        rms.config(font=('ariel',16))
        rms.grid(row=4,column=1)
        rm.mainloop()

    

    def genData(self,data):
        newd = []
        wCgm= open('E:/my own/Semester 9/TA/sample/carakterBiner.txt','w')
        sps=" "
        equal="="
        aS="ASCI"
        biN="BINER"
        ch="CHIPER"
        for i in data:
            newd.append(format(ord(i), '08b'))
            a=ord(i)
           # print("asci :",a)
           # print("biner :",newd)
            ci=ch+sps+equal+sps+str(i)
            rm=aS+sps+equal+sps+str(a)
            bner=biN+sps+equal+sps+str(newd)
            wCgm.write(ci)
            wCgm.write("\n")
            wCgm.write(rm)
            wCgm.write("\n")
            wCgm.write(bner)
            wCgm.write("\n")
        return newd

    def modPix(self,pix, data):
        datalist = self.genData(data)
        lendata = len(datalist)
        imdata = iter(pix)
        encWrite= open('E:/my own/Semester 9/TA/sample/binerRgb.txt','w')
        #encWrite.close()
        for i in range(lendata):
            # Extracting 3 pixels at a time
            pix = [value for value in imdata.__next__()[:3] +
                   imdata.__next__()[:3] +
                   imdata.__next__()[:3]] 
            # Pixel value should be made
            # odd for 1 and even for 0
            for j in range(0, 8):
                if (datalist[i][j] == '0') and (pix[j] % 2 != 0):
                   # print("")
                    
                    if (pix[j] % 2 != 0):
                        pi=pix[j]
                        pix[j] -= 1
                       #print("datalist :",datalist[i][j])
                     #   print("pix[j] :",pix[j],"-","1","","=",pi)

                elif (datalist[i][j] == '1') and (pix[j] % 2 == 0):
                   # print("")
                    pix[j] -= 1
                 #   print("datalist :",datalist[i][j])
                  #  print("pix[j] :",pix[j])
                a= str(datalist[i][j])
                b=str(pix[j])
                encWrite.write("biner :")
                encWrite.write(a)
                encWrite.write("\n")
                encWrite.write("Nilai Pixel :")
                encWrite.write(b)
                encWrite.write("\n")
              #  print("datalist [i][j]:",datalist[i][j])
               # print("pix[j] :",pix[j])
           # print('datalist 2 :',datalist[i][j])
           # print('lendata :',lendata)
            # Eigh^th pixel of every set tells
            # whether to stop or read further.
            # 0 means keep reading; 1 means the
            # message is over.
            if (i == lendata - 1):
                if (pix[-1] % 2 == 0):
                    pix[-1] -= 1
            else:
                if (pix[-1] % 2 != 0):
                    pix[-1] -= 1

            pix = tuple(pix)
            yield pix[0:3]
            yield pix[3:6]
            yield pix[6:9]
           # print ("pix :",pix)

    def encode_enc(self,newimg, data):
        w = newimg.size[0]
        (x, y) = (0, 0)

        for pixel in self.modPix(newimg.getdata(), data):

            # Putting modified pixels in the new image
            newimg.putpixel((x, y), pixel)
            if (x == w - 1):
                x = 0
                y += 1
            else:
                x += 1
         #   print("encode:",pixel)
            #img_b_blue_bin = map(bin, pixel)
           # print("biner :",img_b_blue_bin)

    def enc_fun(self,myimg):
       # data = [line.rstrip('\n') for line in w_fle]
      #  dataa=tkinter.filedialog.askopenfilename(filetypes = ([('txt', '*.txt'),('All Files', '*.*')]))    
        #data=w_fle.copy(),
      #  with open('E:/my own/Semester 9/TA/sample/hiddenMessage.txt','r') as datar : 
      #  if (len(dataa) == 0):
          #  messagebox.showinfo("Alert","Maaf data masih kosong, silahkan masukkan data yang di perlukan")
        with open ('E:/my own/Semester 9/TA/sample/hiddenMessage.txt','r') as datar : 
          #  datar=open(dataa,'r')
            data=datar.read()
            datar.close()
            newimg = myimg.copy()
            self.encode_enc(newimg, data)
            my_file = BytesIO()
            temp=os.path.splitext(os.path.basename(myimg.filename))[0]
            newimg.save(tkinter.filedialog.asksaveasfilename(initialfile=temp,filetypes = ([('png', '*.png')]),defaultextension=".png"))
            self.d_image_size = my_file.tell()
            self.d_image_w,self.d_image_h = newimg.size
            messagebox.showinfo("Berhasil","Selamat encoding berhasil, dan stego image berhasil di simpan")

    def page3(self,frame):
        frame.destroy()
        self.main(root)

root = Tk()

o = Cc()
o.main(root)

root.mainloop()
