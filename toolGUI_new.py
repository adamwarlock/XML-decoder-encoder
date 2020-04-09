#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Apr 05, 2020 01:44:20 PM EDT  platform: Windows NT

import sys
import os
from xml.dom import minidom
import base64
from xml.etree import ElementTree as et

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
    from tkinter.messagebox import showinfo
    from tkinter import filedialog

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import toolGUI_new_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    toolGUI_new_support.set_Tk_var()
    top = Toplevel1 (root)
    toolGUI_new_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    toolGUI_new_support.set_Tk_var()
    top = Toplevel1 (w)
    toolGUI_new_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def selectfile(self):
        self.Text1.delete('1.0','end')
        self.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("XML files","*.xml"),("all files","*.*")))
        self.Text1.insert('1.0',self.filename)
    def load(self):
        self.fname = self.Text1.get('1.0','end')[:-1]
        print(self.fname)
        self.xmltag = 'content'
        if '.xml' not in self.fname:
            self.fname = self.fname + '.xml'
            
        if len(self.fname) == 1:
            showinfo('Error','Enter a File Name!')
        elif len(self.xmltag) == 1:
            showinfo('Error','Enter a XML tag!')
        elif self.fname not in os.listdir() and not os.path.isfile(self.fname):
                        showinfo('Error','File not found!')
        else:
            self.fullXML = open(self.fname,'r')
            self.xmldoc = minidom.parse(self.fname)
            taglist = self.xmldoc.getElementsByTagName(self.xmltag)
            self.Scrolledtext1.delete('1.0','end')
            for line in self.fullXML.readlines():
                self.Scrolledtext1.insert('end',line)
            self.fullXML.close()
            if len(taglist) == 0:
                showinfo('Error','Nothing to Decode in this xml')
                self.Scrolledtext2.delete('1.0','end')
            else:
                b64txt = taglist[0].childNodes[0].data + "================================"
                normalTxt = base64.b64decode(b64txt)
                
                
                if self.flag.get() == 1:
                    normalxlm = minidom.parseString(normalTxt)
                    prettyxml = normalxlm.toprettyxml()
                    self.Scrolledtext2.delete('1.0','end')
                    self.Scrolledtext2.insert('1.0',prettyxml)
                    #print(prettyxml)
                else:
                    self.Scrolledtext2.delete('1.0','end')
                    self.Scrolledtext2.insert('1.0',normalTxt)
                    #print(normalTxt)
                
                gridDoc = et.fromstring(normalTxt)
                labelText=[]
                editText = []
                for element in gridDoc.iter():
                    labelText.append( element.tag.split('}')[-1] )
                    editText.append( element.text)
                print(len(labelText))
                print(len(editText))                  
                self.labels=[]
                self.entry=[]
                self.check=['applicationDate','applicationId','estimatedClosingDate','submitRequestTime','dealId']
                j=0
                for i in range(len(labelText)):
                    if labelText[i] in self.check:
                        self.labels.append(tk.Text(self.Scrolledwindow1))
                        self.labels[j].place(x=20, y=20+(j*20), height=18, width=246)
                        #self.labels[i].configure(height=18,width=250)
                        #self.labels[i].grid(row =i, column=0)
                        self.labels[j].insert('1.0',labelText[i])
                        self.labels[j].configure(state='disabled')
                        #self.labels[i].pack()
                        
                        self.entry.append(tk.Text(self.Scrolledwindow1))
                        self.entry[j].place(x=330, y=20+(j*20), height=18, width=250)
                       #self.entry[i].grid(row=i,column=1)
                       #self.entry[i].configure(height=18,width=250)
                        self.entry[j].configure(takefocus="")
                        self.entry[j].configure(cursor="xterm")
                        if editText[i] == None or editText[i] == '':
                            self.entry[j].configure(state='disabled')
                        else:
                            self.entry[j].insert('1.0',editText[i])
                        j+=1
                    #self.entry[i].pack()
                
    def enc_save(self):
        newxmlTxt = self.Scrolledtext1.get('1.0','end')[:-1]
        newcontentTxt = self.Scrolledtext2.get('1.0','end')[:-1]
        print(newcontentTxt)
#        print('\n\n\n')
        #print(newxmlTxt.split('\n'))
        try:
            nfName = minidom.parseString(newxmlTxt).getElementsByTagName('messageId')[0].childNodes[0].data
            nfName +='.xml'
        except Exception:
            nfName = self.fname.replace('.xml','_new.xml')
            showinfo('Error','File Name not Found in XML!\nNew File saved as '+nfName)
            
        #print(base64.b64encode(newxmltxt.encode('ascii')).decode('ascii')[:-1])
        #print(newxmltxt.split())
        #xml_string = os.linesep.join([s for s in newxmltxt.splitlines() if s.strip()]) # remove the weird newline issue
        #print(xml_string)
        
        for i in range(len(self.labels)):
            if self.labels[i].get('1.0','end')[:-1] in newcontentTxt:
                start = newcontentTxt.find('<'+self.labels[i].get('1.0','end')[:-1]+'>')+len('<'+self.labels[i].get('1.0','end')[:-1]+'>')
                end = newcontentTxt.find('</'+self.labels[i].get('1.0','end')[:-1]+'>')
                newcontentTxt = newcontentTxt.replace(newcontentTxt[start:end],self.entry[i].get('1.0','end')[:-1])
                
        encodednewTxt = base64.b64encode(newcontentTxt.encode('ascii')).decode('ascii').rstrip('=')
#        print(encodednewTxt)
#        nfName = self.fname.replace('.xml','_new.xml')
#        f = open(self.fname)
        nf = open(nfName,'w')
        for line in newxmlTxt.split('\n'):
            if '<content>' in line:
                start = line.find('<content>')+len('<content>')
                end=line.find('</content>')
                line=line.replace(line[start:end],encodednewTxt)
                #print(line)
            nf.write(line+"\n")
        showinfo('Saved','File saved as: '+os.getcwd()+'\\' +nfName)

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("875x796+470+124")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        self.flag= tk.IntVar()
        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.034, rely=0.05, height=21, width=214)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''File Name :''')
        

        self.TButton2 = ttk.Button(top,command = self.load)
        self.TButton2.place(relx=0.414, rely=0.110, height=25, width=76)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Decode''')
       
        self.TButton3 = ttk.Button(top,command = self.selectfile)
        self.TButton3.place(relx=0.514, rely=0.05, height=25, width=76)
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Browse...''')
       
        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.331, rely=0.05, relheight=0.03, relwidth=0.142)
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="none")



        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.TCheckbutton1 = ttk.Checkbutton(top)
        self.TCheckbutton1.place(relx=0.651, rely=0.126, relwidth=0.149
                , relheight=0.0, height=21)
        self.TCheckbutton1.configure(variable=self.flag, onvalue=1,offvalue=0)
        self.TCheckbutton1.configure(takefocus="")
        self.TCheckbutton1.configure(text='''Prettify XML''')

        global _images
        _images = (

         tk.PhotoImage("img_close", data='''R0lGODlhDAAMAIQUADIyMjc3Nzk5OT09PT
                 8/P0JCQkVFRU1NTU5OTlFRUVZWVmBgYGF hYWlpaXt7e6CgoLm5ucLCwszMzNbW
                 1v//////////////////////////////////// ///////////yH5BAEKAB8ALA
                 AAAAAMAAwAAAUt4CeOZGmaA5mSyQCIwhCUSwEIxHHW+ fkxBgPiBDwshCWHQfc5
                 KkoNUtRHpYYAADs= '''),

         tk.PhotoImage("img_closeactive", data='''R0lGODlhDAAMAIQcALwuEtIzFL46
                 INY0Fdk2FsQ8IdhAI9pAIttCJNlKLtpLL9pMMMNTP cVTPdpZQOBbQd60rN+1rf
                 Czp+zLxPbMxPLX0vHY0/fY0/rm4vvx8Pvy8fzy8P//////// ///////yH5BAEK
                 AB8ALAAAAAAMAAwAAAVHYLQQZEkukWKuxEgg1EPCcilx24NcHGYWFhx P0zANBE
                 GOhhFYGSocTsax2imDOdNtiez9JszjpEg4EAaA5jlNUEASLFICEgIAOw== '''),

         tk.PhotoImage("img_closepressed", data='''R0lGODlhDAAMAIQeAJ8nD64qELE
                 rELMsEqIyG6cyG7U1HLY2HrY3HrhBKrlCK6pGM7lD LKtHM7pKNL5MNtiViNaon
                 +GqoNSyq9WzrNyyqtuzq+O0que/t+bIwubJw+vJw+vTz+zT z////////yH5BAE
                 KAB8ALAAAAAAMAAwAAAVJIMUMZEkylGKuwzgc0kPCcgl123NcHWYW Fs6Gp2mYB
                 IRgR7MIrAwVDifjWO2WwZzpxkxyfKVCpImMGAeIgQDgVLMHikmCRUpMQgA7 ''')
        )

        self.style.element_create("close", "image", "img_close",
               ("active", "pressed", "!disabled", "img_closepressed"),
               ("active", "alternate", "!disabled",
               "img_closeactive"), border=8, sticky='')

        self.style.layout("ClosetabNotebook", [("ClosetabNotebook.client",
                                     {"sticky": "nswe"})])
        self.style.layout("ClosetabNotebook.Tab", [
            ("ClosetabNotebook.tab",
              { "sticky": "nswe",
                "children": [
                    ("ClosetabNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("ClosetabNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("ClosetabNotebook.label", {"side":
                                      "left", "sticky": ''}),
                                    ("ClosetabNotebook.close", {"side":
                                        "left", "sticky": ''}),]})]})]})])

        PNOTEBOOK = "ClosetabNotebook" 
 
        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
             [('selected', _compcolor), ('active',_ana2color)])
        self.PNotebook1 = ttk.Notebook(top)
        self.PNotebook1.place(relx=0.023, rely=0.189, relheight=0.737
                 , relwidth=0.953)
        self.PNotebook1.configure(style=PNOTEBOOK)
        self.PNotebook1_t1 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t1, padding=3)
        self.PNotebook1.tab(0, text="Full XML",compound="none",underline="-1",)
        self.PNotebook1_t1.configure(background="#d9d9d9")
        self.PNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.PNotebook1_t1.configure(highlightcolor="black")
        self.PNotebook1_t2 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t2, padding=3)
        self.PNotebook1.tab(1, text="Content Decode XML",compound="none",underline="-1",)
        self.PNotebook1_t2.configure(background="#d9d9d9")
        self.PNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.PNotebook1_t2.configure(highlightcolor="black")
        self.PNotebook1_t3 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t3, padding=3)
        self.PNotebook1.tab(2, text="Grid View",compound="none",underline="-1",)
        self.PNotebook1_t3.configure(background="#d9d9d9")
        self.PNotebook1_t3.configure(highlightbackground="#d9d9d9")
        self.PNotebook1_t3.configure(highlightcolor="black")
 
        self.Scrolledtext1 = ScrolledText(self.PNotebook1_t1)
        self.Scrolledtext1.place(relx=0.012, rely=0.036, relheight=0.884
                 , relwidth=0.958)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(font="TkTextFont")
        self.Scrolledtext1.configure(foreground="black")
        self.Scrolledtext1.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext1.configure(highlightcolor="black")
        self.Scrolledtext1.configure(insertbackground="black")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#c4c4c4")
        self.Scrolledtext1.configure(selectforeground="black")
        self.Scrolledtext1.configure(wrap="none")
 
        self.Scrolledtext2 = ScrolledText(self.PNotebook1_t2)
        self.Scrolledtext2.place(relx=0.012, rely=0.02, relheight=0.954
                 , relwidth=0.982)
        self.Scrolledtext2.configure(background="white")
        self.Scrolledtext2.configure(font="TkTextFont")
        self.Scrolledtext2.configure(foreground="black")
        self.Scrolledtext2.configure(highlightbackground="#d9d9d9")
        self.Scrolledtext2.configure(highlightcolor="black")
        self.Scrolledtext2.configure(insertbackground="black")
        self.Scrolledtext2.configure(insertborderwidth="3")
        self.Scrolledtext2.configure(selectbackground="#c4c4c4")
        self.Scrolledtext2.configure(selectforeground="black")
        self.Scrolledtext2.configure(wrap="none")
        # self.PNotebook1.bind('<Button-1>',_button_press)
        # self.PNotebook1.bind('<ButtonRelease-1>',_button_release)
        # self.PNotebook1.bind('<Motion>',_mouse_over)
        
                              
        self.Scrolledwindow1 = ScrolledWindow(self.PNotebook1_t3)
        self.Scrolledwindow1.place(relx=0.012, rely=0.018, relheight=0.95
                 , relwidth=0.982)
        self.Scrolledwindow1.configure(background="white")
        self.Scrolledwindow1.configure(borderwidth="2")
        self.Scrolledwindow1.configure(relief="groove")
        self.Scrolledwindow1.configure(selectbackground="#c4c4c4")
        self.color = self.Scrolledwindow1.cget("background")
        self.Scrolledwindow1_f = tk.Frame(self.Scrolledwindow1,
                               background=self.color)
        self.Scrolledwindow1.create_window(0, 0, anchor='nw',
                                       window=self.Scrolledwindow1_f)

                              
#        self.Scrolledwindow1 = ScrollableFrame(self.Frame1)
#        self.Scrolledwindow1.pack(fill='both',expand=True)
        self.Label3 = tk.Label(self.Scrolledwindow1)
        self.Label3.place(x=20, y=2, height=18, width=250)
        self.Label3.configure(text='''XML TAG''')
        
        self.Label4 = tk.Label(self.Scrolledwindow1)
        self.Label4.place(x=330, y=2, height=18, width=250)
        self.Label4.configure(text='''Value''')
        # self.TEntry1 = ttk.Entry(self.Scrolledwindow1)
        # self.TEntry1.place(relx=0.1, rely=0.094, relheight=0.034, relwidth=0.18)
        # self.TEntry1.configure(takefocus="")
        # self.TEntry1.configure(cursor="xterm")
        self.PNotebook1.bind('<Button-1>',_button_press)
        self.PNotebook1.bind('<ButtonRelease-1>',_button_release)
        self.PNotebook1.bind('<Motion>',_mouse_over)
        

        self.TButton1 = ttk.Button(top,command = self.enc_save)
        self.TButton1.place(relx=0.423, rely=0.93, height=25, width=100)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''Encode and Save''')

# The following code is add to handle mouse events with the close icons
# in PNotebooks widgets.
def _button_press(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        index = widget.index("@%d,%d" % (event.x, event.y))
        widget.state(['pressed'])
        widget._active = index

def _button_release(event):
    widget = event.widget
    if not widget.instate(['pressed']):
            return
    element = widget.identify(event.x, event.y)
    try:
        index = widget.index("@%d,%d" % (event.x, event.y))
    except TclError:
        pass
    if "close" in element and widget._active == index:
        widget.forget(index)
        widget.event_generate("<<NotebookTabClosed>>")

    widget.state(['!pressed'])
    widget._active = None

def _mouse_over(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        widget.state(['alternate'])
    else:
        widget.state(['!alternate'])

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

class ScrolledWindow(AutoScroll, tk.Canvas):
      '''A standard Tkinter Canvas widget with scrollbars that will
      automatically show/hide as needed.'''
      @_create_container
      def __init__(self, master, **kw):
           tk.Canvas.__init__(self, master, **kw)
           AutoScroll.__init__(self, master)

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





