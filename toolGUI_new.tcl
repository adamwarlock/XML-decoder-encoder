#############################################################################
# Generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#  Apr 08, 2020 08:01:58 PM EDT  platform: Windows NT
set vTcl(timestamp) ""


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 875x795+470+125
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1061
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "New Toplevel"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    label $top.lab52 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab52" "Label2" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex53 \
        -background white -font TkTextFont -foreground black \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 124 -wrap word 
    $top.tex53 configure -font "TkTextFont"
    $top.tex53 insert end text
    vTcl:DefineAlias "$top.tex53" "Text2" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu56 \
        -takefocus {} -text Tbutton 
    vTcl:DefineAlias "$top.tBu56" "TButton2" vTcl:WidgetProc "Toplevel1" 1
    text $top.tex62 \
        -background white -font TkTextFont -foreground black \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground #c4c4c4 \
        -selectforeground black -width 124 -wrap word 
    $top.tex62 configure -font "TkTextFont"
    $top.tex62 insert end text
    vTcl:DefineAlias "$top.tex62" "Text1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab63 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Label 
    vTcl:DefineAlias "$top.lab63" "Label1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TCheckbutton -background $vTcl(actual_gui_bg)
    ttk::style configure TCheckbutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TCheckbutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::checkbutton $top.tCh68 \
        -variable tch68 -takefocus {} -text Tcheck 
    vTcl:DefineAlias "$top.tCh68" "TCheckbutton1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure PC.TNotebook -background $vTcl(actual_gui_bg)
    ttk::style configure PC.TNotebook.Tab -background $vTcl(actual_gui_bg)
    ttk::style configure PC.TNotebook.Tab -foreground $vTcl(actual_gui_fg)
    ttk::style configure PC.TNotebook.Tab -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::style layout PC.TNotebook.Tab {
                    Notebook.tab -children {
                        Notebook.padding -side top -children {
                            Notebook.focus -side top -children {
                                Notebook.text -side right
                                Notebook.image -side left
                            }
                        }
                    }
               }
    vTcl::widgets::ttk::pnotebook::createCmd $top.pNo46 \
        -width 300 -height 200 -style "PC.TNotebook" 
    vTcl:DefineAlias "$top.pNo46" "PNotebook1" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo46 configure -style "PC.TNotebook"
    bind $top.pNo46 <Button-1> {
        _button_press
    }
    bind $top.pNo46 <ButtonRelease-1> {
        _button_release
    }
    bind $top.pNo46 <Motion> {
        _mouse_over
    }
    frame $top.pNo46.t0 \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.pNo46.t0" "PNotebook1_t1" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo46 add $top.pNo46.t0 \
        -padding 0 -sticky nsew -state normal -text {Page 1} -image image2 \
        -compound none -underline -1 
    set site_4_0  $top.pNo46.t0
    vTcl::widgets::ttk::scrolledtext::CreateCmd $site_4_0.scr48 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$site_4_0.scr48" "Scrolledtext1" vTcl:WidgetProc "Toplevel1" 1

    $site_4_0.scr48.01 configure -background white \
        -font TkTextFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -wrap none
    place $site_4_0.scr48 \
        -in $site_4_0 -x 10 -y 20 -width 795 -relwidth 0 -height 495 \
        -relheight 0 -anchor nw -bordermode ignore 
    frame $top.pNo46.t1 \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.pNo46.t1" "PNotebook1_t2" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo46 add $top.pNo46.t1 \
        -padding 0 -sticky nsew -state normal -text {Page 2} -image image2 \
        -compound none -underline -1 
    set site_4_1  $top.pNo46.t1
    vTcl::widgets::ttk::scrolledtext::CreateCmd $site_4_1.scr44 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$site_4_1.scr44" "Scrolledtext2" vTcl:WidgetProc "Toplevel1" 1

    $site_4_1.scr44.01 configure -background white \
        -font TkTextFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground #c4c4c4 \
        -selectforeground black \
        -width 10 \
        -wrap none
    place $site_4_1.scr44 \
        -in $site_4_1 -x 0 -relx 0.012 -y 0 -rely 0.02 -width 0 \
        -relwidth 0.982 -height 0 -relheight 0.954 -anchor nw \
        -bordermode ignore 
    frame $top.pNo46.t2 \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    vTcl:DefineAlias "$top.pNo46.t2" "PNotebook1_t3" vTcl:WidgetProc "Toplevel1" 1
    $top.pNo46 add $top.pNo46.t2 \
        -padding 0 -sticky nsew -state normal -text {New Page} -image {} \
        -compound none -underline -1 
    set site_4_2  $top.pNo46.t2
    frame $site_4_2.fra44 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 545 -width 815 
    vTcl:DefineAlias "$site_4_2.fra44" "Frame1" vTcl:WidgetProc "Toplevel1" 1
    place $site_4_2.fra44 \
        -in $site_4_2 -x 0 -relx 0.012 -y 0 -rely 0.018 -width 0 \
        -relwidth 0.982 -height 0 -relheight 0.973 -anchor nw \
        -bordermode ignore 
    ttk::style configure TCheckbutton -background $vTcl(actual_gui_bg)
    ttk::style configure TCheckbutton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TCheckbutton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::checkbutton $top.tCh49 \
        -variable tch49 -takefocus {} -text Tcheck 
    vTcl:DefineAlias "$top.tCh49" "TCheckbutton2" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu50 \
        -takefocus {} -text Tbutton 
    vTcl:DefineAlias "$top.tBu50" "TButton1" vTcl:WidgetProc "Toplevel1" 1
    ttk::style configure TButton -background $vTcl(actual_gui_bg)
    ttk::style configure TButton -foreground $vTcl(actual_gui_fg)
    ttk::style configure TButton -font "$vTcl(actual_gui_font_dft_desc)"
    ttk::button $top.tBu44 \
        -takefocus {} -text Tbutton 
    vTcl:DefineAlias "$top.tBu44" "TButton3" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab52 \
        -in $top -x 30 -y 80 -width 214 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tex53 \
        -in $top -x 290 -y 80 -width 124 -relwidth 0 -height 24 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tBu56 \
        -in $top -x 450 -y 80 -anchor nw -bordermode ignore 
    place $top.tex62 \
        -in $top -x 290 -y 40 -width 124 -height 24 -anchor nw \
        -bordermode ignore 
    place $top.lab63 \
        -in $top -x 30 -y 40 -width 214 -relwidth 0 -height 21 -anchor nw \
        -bordermode ignore 
    place $top.tCh68 \
        -in $top -x 570 -y 100 -width 130 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.pNo46 \
        -in $top -x 0 -relx 0.023 -y 0 -rely 0.189 -width 0 -relwidth 0.953 \
        -height 0 -relheight 0.737 -anchor nw -bordermode ignore 
    place $top.tCh49 \
        -in $top -x 720 -y 100 -width 130 -relwidth 0 -height 21 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.tBu50 \
        -in $top -x 370 -y 740 -width 100 -relwidth 0 -anchor nw \
        -bordermode ignore 
    place $top.tBu44 \
        -in $top -x 0 -relx 0.514 -y 0 -rely 0.05 -height 25 -relheight 0 \
        -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

