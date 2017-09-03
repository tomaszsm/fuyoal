import wx

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Fuyoal", size=wx.Size(550,300))

    #     self.panel = wx.Panel(self, wx.ID_ANY)

    #     openFileDlgBtn = wx.Button(self.panel, label="Show OPEN FileDialog")
    #     openFileDlgBtn.Bind(wx.EVT_BUTTON, self.onOpenFile)
    
    
        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
		
        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)

        sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel2, wx.ID_ANY, u"First input file"), wx.HORIZONTAL)

        self.m_button3 = wx.Button(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Find file", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button3.Bind(wx.EVT_BUTTON, self.onOpenFile1)
        sbSizer1.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200,-1), 0)
        sbSizer1.Add(self.m_textCtrl1, 0, wx.ALL, 5)

        self.m_staticText1 = wx.StaticText(sbSizer1.GetStaticBox(), wx.ID_ANY, u"Key 1:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        sbSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150,-1), wx.TE_PASSWORD)
        sbSizer1.Add(self.m_textCtrl2, 0, wx.ALL, 5)


        bSizer1.Add(sbSizer1, 1, wx.ALL | wx.EXPAND, 5)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText3 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Size of phony ciphertext:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        bSizer6.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, u"default", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer6.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"kB", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        bSizer6.Add(self.m_staticText4, 0, wx.ALL, 5)


        bSizer1.Add(bSizer6, 1, wx.EXPAND, 5)

        self.m_checkBox2 = wx.CheckBox(self.m_panel2, wx.ID_ANY, u"Include second file", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Bind(wx.EVT_CHECKBOX, self.onCheck) 
        bSizer1.Add(self.m_checkBox2, 0, wx.ALL, 5)

        sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel2, wx.ID_ANY, u"Second input file"), wx.HORIZONTAL)

        self.m_button4 = wx.Button(sbSizer3.GetStaticBox(), wx.ID_ANY, u"Find file", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button4.Bind(wx.EVT_BUTTON, self.onOpenFile2)
        self.m_button4.Enable(False)

        sbSizer3.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200,-1), 0)
        self.m_textCtrl3.Enable(False)

        sbSizer3.Add(self.m_textCtrl3, 0, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(sbSizer3.GetStaticBox(), wx.ID_ANY, u"Key 2:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        sbSizer3.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150,-1), wx.TE_PASSWORD)
        self.m_textCtrl4.Enable(False)

        sbSizer3.Add(self.m_textCtrl4, 0, wx.ALL, 5)


        bSizer1.Add(sbSizer3, 1, wx.ALL | wx.EXPAND, 5)

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )
	
	self.m_button5 = wx.Button( self.m_panel2, wx.ID_ANY, u"Encrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
	bSizer14.Add( self.m_button5, 0, wx.ALL, 5 )
	
	self.m_button6 = wx.Button( self.m_panel2, wx.ID_ANY, u"Decrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
	bSizer14.Add( self.m_button6, 0, wx.ALL, 5 )
		
		
	bSizer1.Add( bSizer14, 1, wx.EXPAND, 5 )


        self.m_panel2.SetSizer(bSizer1)
        self.m_panel2.Layout()
        bSizer1.Fit(self.m_panel2)

        self.Layout()
        self.Centre(wx.BOTH)

    def onOpenFile1(self, event):
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",
            wildcard="All files (*.*)|*.*",
            style=wx.FD_OPEN | wx.FD_CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.m_textCtrl1.SetLabel(path)
            print("Warning")
        dlg.Destroy()

    def onOpenFile2(self, event):
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",
            wildcard="All files (*.*)|*.*",
            style=wx.FD_OPEN | wx.FD_CHANGE_DIR
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.m_textCtrl3.SetLabel(path)
            print("Warning")
        dlg.Destroy()

    def onCheck(self, event):
        checked = event.GetEventObject().Get3StateValue()
        if(checked):
            self.m_button4.Enable()
            self.m_textCtrl3.Enable()
            self.m_textCtrl4.Enable()
            self.m_textCtrl5.Enable(False)
        else:
            self.m_button4.Enable(False)
            self.m_textCtrl3.Enable(False)
            self.m_textCtrl4.Enable(False)
            self.m_textCtrl5.Enable()

    
app = wx.App(redirect=True)
top = Frame()
top.Show()
app.MainLoop()
