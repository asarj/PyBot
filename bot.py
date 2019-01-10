import wikipedia
import wolframalpha
import wx

app_id = "JEREAK-7XJ4VHGV5Q"
query = ""
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,
                 None,
                 pos = wx.DefaultPosition,
                 size = wx.Size(450, 100),
                 style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
                 title = "PyBot")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel, label="Welcome to the PyBot, how can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        input = input.lower()
        analyze_input(input)

def analyze_input(input):
    if(query == "shut down"):
        print("App has terminated")
    else:
        try:
            #wolframalpha
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            answer = next(res.results).text
        except:
            #wikipedia
            wikipedia.set_lang("en")
            answer = wikipedia.summary(input, sentences = 2)
        print(answer)

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()