#coding:utf-8
import wx

app = wx.App()
win = wx.Frame(
	None,
	title="simple editor",
	size=(410, 335))
bkg = wx.Panel(win)
def openFile(evt):
	dlg = wx.FileDialog(
		win,
		"Open",
		"",
		"",
		"All files (*.*)|*.*",
		wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
	filepath = ''
	if dlg.ShowModal() == wx.ID_OK:
		filepath = dlg.GetPath()
	else:
		return
	filename.SetValue(filepath)
	fopen = open(filepath)
	fcontent = fopen.read()
	contents.SetValue(fcontent)
	fopen.close()
def saveFile(evt):
	fcontent = contents.GetValue()
	fopen = open(filename.GetValue(), 'w')
	fopen.write(fcontent)
	fopen.close()
openBtn = wx.Button(bkg, label='open')
openBtn.Bind(wx.EVT_BUTTON, openFile)
saveBtn = wx.Button(bkg, label='save')
saveBtn.Bind(wx.EVT_BUTTON, saveFile)
filename = wx.TextCtrl(bkg, style=wx.TE_READONLY)
contents = wx.TextCtrl(bkg, style=wx.TE_MULTILINE)
hbox = wx.BoxSizer()
hbox.Add(openBtn, proportion=0, flag=wx.LEFT | wx.ALL, border=5)
hbox.Add(filename, proportion=1, flag=wx.EXPAND | wx.TOP | wx.BOTTOM, border=5)
hbox.Add(saveBtn, proportion=0, flag=wx.LEFT | wx.ALL, border=5)
bbox = wx.BoxSizer(wx.VERTICAL)
bbox.Add(hbox, proportion=0, flag=wx.EXPAND | wx.ALL)
bbox.Add(
	contents,
	proportion=1,
	flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,
	border=5)
bkg.SetSizer(bbox)
win.Show()
app.MainLoop()
