#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
'''
Author : Vivek Chopra

'''

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

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
    py3 = True

import toolGUI_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    toolGUI_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    toolGUI_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    
    def load(self):
        self.fname = self.Text1.get('1.0','end')[:-1]
        self.xmltag = self.Text2.get('1.0','end')[:-1]
        if '.xml' not in self.fname:
            self.fname = self.fname + '.xml'
            
        if len(self.fname) == 1:
            showinfo('Error','Enter a File Name!')
        elif len(self.xmltag) == 1:
            showinfo('Error','Enter a XML tag!')
        elif self.fname not in os.listdir():
            showinfo('Error','File not found!')
        else:

            xmldoc = minidom.parse(self.fname)
            taglist = xmldoc.getElementsByTagName(self.xmltag)

            if len(taglist) == 0:
                showinfo('Error','XML tag not found!')
                self.Scrolledtext1.delete('1.0','end')
            else:
                b64txt = taglist[0].childNodes[0].data + "================================"
                normalTxt = base64.b64decode(b64txt)
                normalxlm = minidom.parseString(normalTxt)
                prettyxml = normalxlm.toprettyxml()
                
                if self.flag.get() == 1:
                    self.Scrolledtext1.delete('1.0','end')
                    self.Scrolledtext1.insert('1.0',prettyxml)
                    print(prettyxml)
                else:
                    self.Scrolledtext1.delete('1.0','end')
                    self.Scrolledtext1.insert('1.0',normalTxt)
                    print(normalTxt)
    def enc_save(self):
        newxmltxt = self.Scrolledtext1.get('1.0','end')[:-1]
        print(newxmltxt)
        #print(minidom.parseString(newxmltxt).normalize())
        #print(base64.b64encode(newxmltxt.encode('ascii')).decode('ascii')[:-1])
        #print(newxmltxt.split())
        #xml_string = os.linesep.join([s for s in newxmltxt.splitlines() if s.strip()]) # remove the weird newline issue
        #print(xml_string)
        encodednewTxt = base64.b64encode(newxmltxt.encode('ascii')).decode('ascii').rstrip('=')
        print(encodednewTxt)
        f = open(self.fname)
        nf = open('new_'+self.fname,'w')
        for line in f.readlines():
            if '<content>' in line:
                start = line.find('<content>')+len('<content>')
                end=line.find('</content>')
                line=line.replace(line[start:end],encodednewTxt)
                #print(line)
            nf.write(line)
        showinfo('Saved','File saved as: '+'new_'+self.fname)
        

    
            
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

        top.geometry("875x732+470+124")
        top.minsize(120, 1)
        top.maxsize(1924, 1061)
        top.resizable(1, 1)
        top.title("Main Window")
        top.configure(background="#d9d9d9")
        self.flag= tk.IntVar()
        self.Text1 = tk.Text(top)
        self.Text1.place(relx=0.331, rely=0.055, relheight=0.033, relwidth=0.142)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="none")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.034, rely=0.055, height=21, width=214)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''File Name :''')
        
        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.034, rely=0.109, height=21, width=214)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''Enter XML tag to decode :''')

        self.Text2 = tk.Text(top)
        self.Text2.place(relx=0.331, rely=0.109, relheight=0.033, relwidth=0.142)

        self.Text2.configure(background="white")
        self.Text2.configure(cursor="fleur")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="#c4c4c4")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(wrap="none")

        self.TButton2 = ttk.Button(top, command = self.load)
        self.TButton2.place(relx=0.514, rely=0.109, height=25, width=76)
        self.TButton2.configure(takefocus="")
        self.TButton2.configure(text='''Decode''')

        self.TLabelframe1 = ttk.Labelframe(top)
        self.TLabelframe1.place(relx=0.011, rely=0.178, relheight=0.813
                , relwidth=0.971)
        self.TLabelframe1.configure(relief='')
        self.TLabelframe1.configure(text='''Editor''')

        self.Scrolledtext1 = ScrolledText(self.TLabelframe1)
        self.Scrolledtext1.place(relx=0.012, rely=0.034, relheight=0.849
                , relwidth=0.982, bordermode='ignore')
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
        
        self.style.map('TCheckbutton',background=
            [('selected', _bgcolor), ('active', _ana2color)])
        self.TCheckbutton1 = ttk.Checkbutton(top)
        self.TCheckbutton1.place(relx=0.777, rely=0.137, relwidth=0.16
        , relheight=0.0, height=21)
        self.TCheckbutton1.configure(variable=self.flag, onvalue=1,offvalue=0)
        self.TCheckbutton1.configure(takefocus="")
        self.TCheckbutton1.configure(text='''Prettify XML''')
        
        self.TButton3 = ttk.Button(self.TLabelframe1, command = self.enc_save)
        self.TButton3.place(relx=0.450, rely=0.908, height=25, width=100
                , bordermode='ignore')
        self.TButton3.configure(takefocus="")
        self.TButton3.configure(text='''Encode and Save''')
        


        

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





