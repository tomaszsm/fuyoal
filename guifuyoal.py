#!/usr/bin/python3

import wx
from core import *

class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Fuyoal 1.0", size=wx.Size(650,370))
        self.edc = edcr()

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.WaitCursor= wx.Cursor(wx.CURSOR_WAIT)
        self.RegCursor= wx.Cursor(wx.CURSOR_ARROW)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.bSizer1 = wx.BoxSizer(wx.VERTICAL)

        self.sbSizer1 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel2, wx.ID_ANY, u"First input file (for encryption or decrypion)"), wx.HORIZONTAL)

        self.m_button3 = wx.Button(self.sbSizer1.GetStaticBox(), wx.ID_ANY, u"Find file", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button3.Bind(wx.EVT_BUTTON, self.onOpenFile1)
        self.sbSizer1.Add(self.m_button3, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(self.sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200,-1), 0)
        self.m_textCtrl1.Bind(wx.EVT_KILL_FOCUS, self.update_output_file)
        self.sbSizer1.Add(self.m_textCtrl1, 0, wx.ALL, 5)

        self.m_staticText1 = wx.StaticText(self.sbSizer1.GetStaticBox(), wx.ID_ANY, u"Key 1:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.sbSizer1.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_textCtrl2 = wx.TextCtrl(self.sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150,-1), wx.TE_PASSWORD)
        self.sbSizer1.Add(self.m_textCtrl2, 0, wx.ALL, 5)

        self.m_staticText1a = wx.StaticText(self.sbSizer1.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1a.Wrap(-1)
        self.sbSizer1.Add(self.m_staticText1a, 0, wx.ALL, 5)

        self.bSizer1.Add(self.sbSizer1, 1, wx.ALL | wx.EXPAND, 5)

        self.bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText3 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"Size of phony ciphertext:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)
        self.bSizer6.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self.m_panel2, wx.ID_ANY, u"default", wx.DefaultPosition, wx.DefaultSize, 0)
        self.bSizer6.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self.m_panel2, wx.ID_ANY, u"KB", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText4.Wrap(-1)
        self.bSizer6.Add(self.m_staticText4, 0, wx.ALL, 5)

        self.bSizer1.Add(self.bSizer6, 1, wx.EXPAND, 5)

        self.m_checkBox2 = wx.CheckBox(self.m_panel2, wx.ID_ANY, u"Include second file", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Bind(wx.EVT_CHECKBOX, self.onCheck) 
        self.bSizer1.Add(self.m_checkBox2, 0, wx.ALL, 5)

        self.sbSizer3 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel2, wx.ID_ANY, u"Second input file (for encryption)"), wx.HORIZONTAL)

        self.m_button4 = wx.Button(self.sbSizer3.GetStaticBox(), wx.ID_ANY, u"Find file", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button4.Bind(wx.EVT_BUTTON, self.onOpenFile2)
        self.m_button4.Enable(False)

        self.sbSizer3.Add(self.m_button4, 0, wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self.sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200,-1), 0)
        self.m_textCtrl3.Enable(False)

        self.sbSizer3.Add(self.m_textCtrl3, 0, wx.ALL, 5)

        self.m_staticText2 = wx.StaticText(self.sbSizer3.GetStaticBox(), wx.ID_ANY, u"Key 2:", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.sbSizer3.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self.sbSizer3.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150,-1), wx.TE_PASSWORD)
        self.m_textCtrl4.Enable(False)

        self.sbSizer3.Add(self.m_textCtrl4, 0, wx.ALL, 5)

        self.m_staticText2a = wx.StaticText(self.sbSizer3.GetStaticBox(), wx.ID_ANY, u"", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2a.Wrap(-1)
        self.sbSizer3.Add(self.m_staticText2a, 0, wx.ALL, 5)

        self.bSizer1.Add(self.sbSizer3, 1, wx.ALL | wx.EXPAND, 5)

        self.sbSizer4 = wx.StaticBoxSizer(wx.StaticBox(self.m_panel2, wx.ID_ANY, u"Output file"), wx.HORIZONTAL)

        self.m_button7 = wx.Button(self.sbSizer4.GetStaticBox(), wx.ID_ANY, u"Find file", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button7.Bind(wx.EVT_BUTTON, self.onOpenFile3)

        self.sbSizer4.Add(self.m_button7, 0, wx.ALL, 5)

        self.m_textCtrl6 = wx.TextCtrl(self.sbSizer4.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(400,-1), 0)

        self.sbSizer4.Add(self.m_textCtrl6, 0, wx.ALL, 5)

        self.bSizer1.Add(self.sbSizer4, 1, wx.ALL | wx.EXPAND, 5)
        
        self.bSizer14 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button5 = wx.Button(self.m_panel2, wx.ID_ANY, u"Encrypt", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button5.Bind(wx.EVT_BUTTON, self.onEncrypt)
        self.bSizer14.Add( self.m_button5, 0, wx.ALL, 5 )

        self.m_button6 = wx.Button(self.m_panel2, wx.ID_ANY, u"Decrypt", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_button6.Bind(wx.EVT_BUTTON, self.onDecrypt)
        self.bSizer14.Add(self.m_button6, 0, wx.ALL, 5)

        self.bSizer1.Add( self.bSizer14, 1, wx.EXPAND, 5 )

        self.m_panel2.SetSizer(self.bSizer1)
        self.m_panel2.Layout()
        self.bSizer1.Fit(self.m_panel2)

        self.Layout()
        self.Centre(wx.BOTH)

    def onOpenFile1(self, event):
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",
            wildcard="All files (*.*)|*.*|Encrypted files (*.fya)|*.fya",
            style=wx.FD_OPEN | wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.m_textCtrl1.SetValue(path)
            try:
                self.m_staticText1a.SetLabel(self.nicesize(os.path.getsize(path)))
            except WindowsError:
                self.Warn("File " + self.m_textCtrl1.GetValue() + " does not exist!")
            self.update_output_file(None)
        dlg.Destroy()

    def onOpenFile2(self, event):
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",
            wildcard="All files (*.*)|*.*",
            style=wx.FD_OPEN | wx.FD_CHANGE_DIR | wx.FD_FILE_MUST_EXIST
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.m_textCtrl3.SetValue(path)
            try:
                self.m_staticText2a.SetLabel(self.nicesize(os.path.getsize(path)))
            except WindowsError:
                self.Warn("File " + self.m_textCtrl3.GetValue() + " does not exist!")
        dlg.Destroy()

    def onOpenFile3(self, event):
        dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultFile="",
            wildcard="All files (*.*)|*.*|Encrypted files (*.fya)|*.fya",
            style=wx.FD_SAVE
        )
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.m_textCtrl6.SetValue(path)
        dlg.Destroy()

    def update_output_file(self, evt):
        if(self.m_textCtrl1.GetValue()[-4:]==".fya"):
            fileout = self.m_textCtrl1.GetValue()[:-4]
        else:
            fileout = self.m_textCtrl1.GetValue() + ".fya"
        self.m_textCtrl6.SetValue(fileout)
        if(evt):
            evt.Skip()
        
    def onCheck(self, event):
        checked = event.GetEventObject().Get3StateValue()
        if(checked):
            self.m_button4.Enable()
            self.m_textCtrl3.Enable()
            self.m_textCtrl4.Enable()
            self.m_textCtrl5.Enable(False)
            self.m_button6.Enable(False)
        else:
            self.m_button4.Enable(False)
            self.m_textCtrl3.Enable(False)
            self.m_textCtrl4.Enable(False)
            self.m_textCtrl5.Enable()
            self.m_button6.Enable()

    def onEncrypt(self, event):
        if(self.m_textCtrl1.GetValue()==""):
            self.Warn("Please specify file 1!")
            return(-1)
        if(not os.path.isfile(self.m_textCtrl1.GetValue())):
            self.Warn("File " + self.m_textCtrl1.GetValue() + " does not exist!")
            return(-1)
        if(self.m_textCtrl2.GetValue()==""):
            self.Warn("Key 1 is empty - it is extremmely insecure!")
            return(-1)
        outfile = self.m_textCtrl6.GetValue()
        if(os.path.isfile(outfile)):
            if(not self.Ask("File already exists. Overwrite?")):
                return(-1)
        try:
            f = open(outfile,"w")
            f.close()
        except:
            self.Warn("Cannot write to file!")
            return(-1)
        # Encrypt 2 files
        if(self.m_checkBox2.GetValue()):
            if(self.m_textCtrl3.GetValue()==""):
                self.Warn("Please specify file 2!")
                return(-1)
            if(not os.path.isfile(self.m_textCtrl3.GetValue())):
                self.Warn("File " + self.m_textCtrl3.GetValue() + " does not exist!")
                return(-1)
            if(self.m_textCtrl4.GetValue()==""):
                self.Warn("Key 2 is empty - it is extremmely insecure!")
                return(-1)
            if(self.m_textCtrl2.GetValue()==self.m_textCtrl4.GetValue()):
                self.Warn("Key 1 is same as key 2 - this is situation which is unfortunate for many reasons!")
                return(-1)
            self.m_panel2.SetCursor(self.WaitCursor)
            ret = self.edc.encrypt_file2(self.m_textCtrl1.GetValue(),bytes(self.m_textCtrl2.GetValue(),"utf8"), \
                                         self.m_textCtrl3.GetValue(),bytes(self.m_textCtrl4.GetValue(),"utf8"), \
                                         outfile)
            self.m_panel2.SetCursor(self.RegCursor)
            if(ret==0):
                self.Info("Files encrypted.")
            elif(ret==-2):
                self.Warn("Could not write to file!")
            else:
                self.Warn("Something went wrong!")
        # Encrypt 1 file
        else:
            if(self.m_textCtrl5.GetValue()=="default"):
                self.m_panel2.SetCursor(self.WaitCursor)
                ret = self.edc.encrypt_file1(self.m_textCtrl1.GetValue(),bytes(self.m_textCtrl2.GetValue(),"utf8"),False,outfile)
                self.m_panel2.SetCursor(self.RegCursor)
                if(ret==0):
                    self.Info("File encrypted.")
                elif(ret==-2):
                    self.Warn("Could not write to file!")
                else:
                    self.Warn("Something went wrong!")
            else:
                try:
                    ## sizealt = max(round(float(self.m_textCtrl5.GetValue())*1024),1)
                    sizealt = int(round(float(self.m_textCtrl5.GetValue())*1024))
                    if(sizealt < 1):
                        raise
                except:
                    self.Warn("Wrong size parameter!")
                    return(-1)
                self.m_panel2.SetCursor(self.WaitCursor)
                ret = self.edc.encrypt_file1(self.m_textCtrl1.GetValue(),bytes(self.m_textCtrl2.GetValue(),"utf8"),sizealt,False)
                self.m_panel2.SetCursor(self.RegCursor)
                if(ret==0):
                    self.Info("File encrypted.")
                elif(ret==-2):
                    self.Warn("Could not write to file!")
                else:
                    self.Warn("Something went wrong!")

    def onDecrypt(self, event):
        if(self.m_textCtrl1.GetValue()==""):
            self.Warn("Please specify file 1!")
            return(-1)
        if(not os.path.isfile(self.m_textCtrl1.GetValue())):
            self.Warn("File " + self.m_textCtrl1.GetValue() + " does not exist!")
            return(-1)
        outfile = self.m_textCtrl6.GetValue()
        try:
            f = open(outfile,"w")
            f.close()
        except:
            self.Warn("Cannot write to file!")
            return(-1)
        self.m_panel2.SetCursor(self.WaitCursor)
        ret = self.edc.decrypt_file(self.m_textCtrl1.GetValue(),bytes(self.m_textCtrl2.GetValue(),"utf8"),outfile)
        self.m_panel2.SetCursor(self.RegCursor)
        if(ret==0):
            self.Info("File decrypted.")
        elif(ret==-2):
            self.Warn("Wrong key!")
        elif(ret==-3):
            self.Warn("Wrong input file!")
        else:
            self.Warn("Something went wrong!")

    def Info(parent, message, caption = 'Fuyoal'):
        dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_INFORMATION)
        dlg.ShowModal()
        dlg.Destroy()

    def Warn(parent, message, caption = 'Error'):
        dlg = wx.MessageDialog(parent, message, caption, wx.OK | wx.ICON_WARNING)
        dlg.ShowModal()
        dlg.Destroy()

    def Ask(parent, message, caption = 'Warning'):
        dlg = wx.MessageDialog(parent, message, caption, wx.YES_NO | wx.ICON_WARNING)
        result = dlg.ShowModal() == wx.ID_YES
        dlg.Destroy()
        return(result)


    def nicesize(self,size):
        if(size < 1024):
            ret = str(size)+" B"
        elif(size < 1048576):
            ksize = round(size/1024.0,2)
            ret = str(ksize)+" KB"
        else:
            msize = round(size/1048576.0,2)
            ret = str(msize)+" MB"
        return(ret)


app = wx.App()
top = Frame()
top.Show()
app.MainLoop()
