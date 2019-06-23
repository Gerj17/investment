import tkinter as tk
from pathlib import Path


#  this gui is separated into two sections(blocks) they are written in chronological order
#  the first block is the welcome and leave page it
#  the second page is where the relevant data is entered to be calculated


class Block1(tk.Frame):
    """

    """
    def __init__(self, window):
        tk.Frame.__init__(self, )
        self.pack()
        self.window = window
        # -----Create widgets-----
        self.btn_new = tk.Button(self, text="New Report ", command=self.bt_new, padx=2, pady=2)
        self.btn_done = tk.Button(self, text="Done", command=self.quit, padx=2, pady=2)

        # -----Place widget in frame-----

        self.btn_new.grid(row=2, column=1, padx=200, pady=13)
        self.btn_done.grid(row=4, column=1, padx=200, pady=13)

    def bt_new(self):
        self.pack_forget()
        return Block2(self.window)

    def pack_it(self):
        return self.pack()


class Block2(tk.Frame):
    reports = []

    def __init__(self, window):
        tk.Frame.__init__(self, )
        self.pack()
        self.window = window

        #  -------Create Widgets---------
        self.company = tk.Label(self, text="Name of Company")
        self.shares = tk.Label(self, text="Number of Shares")
        self.price = tk.Label(self, text="Bid Price")
        self.dividends = tk.Label(self, text="Average dividends * ensure a common base year is set")
        self.location = tk.Label(self, text="Location of file")
        self.space = tk.Label(self, text="")

        self.a = tk.Entry(self, width=40)
        self.b = tk.Entry(self, width=40)
        self.c = tk.Entry(self, width=40)
        self.d = tk.Entry(self, width=40)
        self.e = tk.Entry(self, width=40, text="'C:/Users/Gerard/Documents")

        self.document = tk.Button(self, text="Document", command=self.document)
        self.desktop = tk.Button(self, text="Desktop", command=self.desktop)
        self.done = tk.Button(self, text="Done", bg="#7FC9D8", command=self.done)

        #  -----Set Widgets--------
        #  Labels
        self.company.grid(row=0, column=0, sticky="W", pady=10)
        self.shares.grid(row=1, column=0, sticky="W", pady=10)
        self.price.grid(row=2, column=0, sticky="W", pady=10)
        self.dividends.grid(row=3, column=0, sticky="W", pady=10)
        self.location.grid(row=4, column=0, sticky="W", pady=10)
        self.space.grid(row=6, column=0, sticky="W", pady=10)

        #  Entry
        self.a.grid(row=0, column=1, columnspan=2, sticky="E", padx=20, pady=10)
        self.b.grid(row=1, column=1, columnspan=2, sticky="E", padx=20, pady=10)
        self.c.grid(row=2, column=1, columnspan=2, sticky="E", padx=20, pady=10)
        self.d.grid(row=3, column=1, columnspan=2, sticky="E", padx=20, pady=10)
        self.e.grid(row=4, column=1, columnspan=2, sticky="E", padx=20, pady=10)

        #  Buttons
        self.document.grid(row=5, column=1)
        self.desktop.grid(row=5, column=2)
        self.done.grid(row=7, column=0, columnspan=3, ipadx=200, pady=7, )

        #  ------Other------

    def document(self):
        self.e.delete(0, 'end')
        doc_path = Path.home().joinpath("Documents")
        self.e.insert(0, doc_path)

    def desktop(self):
        self.e.delete(0, 'end')
        doc_path = Path.home().joinpath("Desktop")
        self.e.insert(0, doc_path)

    def done(self):
        self.get_data()
        self.pack_forget()
        return Block1(self.window),

    def get_data(self, ):
        report = ({
            "name": self.a.get(),
            "shares": self.b.get(),
            "price": self.c.get(),
            "avg_div": self.d.get(),
            "location": self.e.get(),
        })

        self.reports.append(report)

        print(self.reports)
        print("hello")

    def repo(self):
        return self.reports

class BlockPar(tk.Frame):
    def __init__(self, window):
        tk.Frame.__init__(self, )
        self.pack()
        self.window = window
        # -----Create widgets-----
        self.b_name = tk.Label(self, text="Business Name")
        self.m_price = tk.Label(self, text="Market Price")
        self.avg_return = tk.Label(self, text="Average Dividend// Expected Dividend")
        self.answer = tk.Label(self, text="Years till par return")

        self.btn_calculate = tk.Button(self, text="calculate", command=self.calculate, padx=2, pady=2)
        self.btn_done = tk.Button(self, text="Done", command=self.quit, padx=2, pady=2)

        # -----Place widget in frame-----

        self.btn_calculate.grid(row=2, column=1, padx=200, pady=13)
        self.btn_done.grid(row=4, column=1, padx=200, pady=13)

    def calculate(self):
        return None
#root = tk.Tk()
# root.geometry("400x160")
#a = BlockPar(root)
#root.mainloop()