cat ~/mari_app/main.py
import json, os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView

FILE = "mari.json"
data = {"balance":100,"income":100,"expense":30,"debtors":{"Tafadzwa":145},"history":[]}
if os.path.exists(FILE):
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except:
        pass

class MariApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.bal_label = Label(text=f"Balance: ${data['balance']:.2f}", font_size=28, size_hint_y=None, height=60)
        self.debt_label = Label(text=f"Zvikwereti ${sum(data['debtors'].values()):.2f}", size_hint_y=None, height=30)
        root.add_widget(self.bal_label)
        root.add_widget(self.debt_label)
        btn_in = Button(text='Mari Yapinda', background_color=(0.9,1,0.35,1), color=(0,0,0,1), size_hint_y=None, height=55)
        btn_out = Button(text='Mari Yabuda', background_color=(0.18,0.8,0.44,1), size_hint_y=None, height=55)
        btn_debt_add = Button(text='Chikwereti +', size_hint_y=None, height=55)
        btn_debt_pay = Button(text='Debtor Paid -', background_color=(0.2,0.6,1,1), size_hint_y=None, height=55)
        btn_debtors = Button(text='Debtors List', size_hint_y=None, height=55)
        btn_report = Button(text='Reports', size_hint_y=None, height=55)
        btn_zimra = Button(text='ZIMRA Income Statement', background_color=(1,0.3,0.3,1), size_hint_y=None, height=55)
        btn_in.bind(on_press=lambda x: self.ask("Mari Yapinda", self.add_income))
        btn_out.bind(on_press=lambda x: self.ask("Mari Yabuda", self.add_expense))
        btn_debt_add.bind(on_press=lambda x: self.ask("Chikwereti - Name + Amount", self.add_debt))
        btn_debt_pay.bind(on_press=lambda x: self.ask_pay())
        btn_debtors.bind(on_press=lambda x: self.show_debtors())
        btn_report.bind(on_press=lambda x: self.show_report())
        btn_zimra.bind(on_press=lambda x: self.show_zimra())
        for b in [btn_in, btn_out, btn_debt_add, btn_debt_pay, btn_debtors, btn_report, btn_zimra]:
            root.add_widget(b)
        return root
    def save(self):
        with open(FILE,"w") as f:
            json.dump(data, f)
        self.bal_label.text = f"Balance: ${data['balance']:.2f}"
        self.debt_label.text = f"Zvikwereti ${sum(data['debtors'].values()):.2f}"
    def ask(self, title, cb):
        box = BoxLayout(orientation='vertical', spacing=10, padding=10)
        t1 = TextInput(hint_text="Amount", input_filter='float', multiline=False)
        t2 = TextInput(hint_text="Name / Reason", multiline=False)
        b = Button(text="SAVE", size_hint_y=None, height=50, background_color=(0.9,1,0.35,1), color=(0,0,0,1))
        box.add_widget(t1); box.add_widget(t2); box.add_widget(b)
        pop = Popup(title=title, content=box, size_hint=(0.85,0.5))
        b.bind(on_press=lambda x: [cb(t1.text, t2.text), pop.dismiss(), self.save()])
        pop.open()
    def ask_pay(self):
        box = BoxLayout(orientation='vertical', spacing=10, padding=10)
        t1 = TextInput(hint_text="Amount Paid", input_filter='float', multiline=False)
        t2 = TextInput(hint_text="Debtor Name (exact)", multiline=False)
        b = Button(text="PAY", size_hint_y=None, height=50, background_color=(0.2,0.6,1,1))
        box.add_widget(t1); box.add_widget(t2); box.add_widget(b)
        pop = Popup(title="Debtor Paid", content=box, size_hint=(0.85,0.5))
        b.bind(on_press=lambda x: [self.pay_debt(t1.text, t2.text), pop.dismiss(), self.save()])
        pop.open()
    def add_income(self, amt, who):
        if not amt: return
        data["balance"] += float(amt)
        data["income"] += float(amt)
        data["history"].append(f"{who} +${amt}")
    def add_expense(self, amt, why):
        if not amt: return
        data["balance"] -= float(amt)
        data["expense"] += float(amt)
        data["history"].append(f"{why} -${amt}")
    def add_debt(self, amt, name):
        if not amt or not name: return
        data["debtors"][name] = data["debtors"].get(name, 0) + float(amt)
    def pay_debt(self, amt, name):
        if not amt or not name: return
        if name.strip() not in data["debtors"]:
            self.popup_msg(f"{name} not found in debtors")
            return
        name = name.strip()
        pay = float(amt)
        data["debtors"][name] -= pay
        if data["debtors"][name] <= 0:
            del data["debtors"][name]
        data["balance"] += pay
        data["income"] += pay
        data["history"].append(f"{name} PAID ${pay}")
    def popup_msg(self, msg):
        box = BoxLayout(orientation='vertical', padding=10)
        box.add_widget(Label(text=msg))
        b = Button(text="OK", size_hint_y=None, height=50)
        box.add_widget(b)
        pop = Popup(title="Info", content=box, size_hint=(0.7,0.4))
        b.bind(on_press=lambda x: pop.dismiss())
        pop.open()
    def show_debtors(self):
        from kivy.uix.scrollview import ScrollView
        scroll = ScrollView()
        box = BoxLayout(orientation='vertical', padding=10, spacing=5, size_hint_y=None)
        box.bind(minimum_height=box.setter('height'))
        if not data['debtors']:
            box.add_widget(Label(text="No debtors yet", size_hint_y=None, height=30))
        else:
            for name, amt in data['debtors'].items():
                box.add_widget(Label(text=f"{name}: ${amt:.2f}", size_hint_y=None, height=30))
        scroll.add_widget(box)
        main = BoxLayout(orientation='vertical')
        main.add_widget(scroll)
        b = Button(text="Close", size_hint_y=None, height=50)
        main.add_widget(b)
        pop = Popup(title=f"Debtors Total ${sum(data['debtors'].values()):.2f}", content=main, size_hint=(0.9,0.8))
        b.bind(on_press=lambda x: pop.dismiss())
        pop.open()
    def show_report(self):
        txt = f"Income: ${data['income']:.2f}\nExpense: ${data['expense']:.2f}\nBalance: ${data['balance']:.2f}\n\nHistory:\n" + "\n".join(data['history'][-15:])
        box = BoxLayout(orientation='vertical', padding=10)
        box.add_widget(Label(text=txt))
        b = Button(text="Close", size_hint_y=None, height=50)
        box.add_widget(b)
        pop = Popup(title="Report", content=box, size_hint=(0.9,0.8))
        b.bind(on_press=lambda x: pop.dismiss())
        pop.open()
    def show_zimra(self):
        income = data['income']
        expense = data['expense']
        gross = income - expense
        debt_total = sum(data['debtors'].values())
        txt = f"MINI INCOME STATEMENT\nFor ZIMRA Submission\n\nTotal Income: ${income:.2f}\nLess: Expenses: ${expense:.2f}\n--------------------------\nGROSS PROFIT: ${gross:.2f}\n\nCash on Hand: ${data['balance']:.2f}\nDebtors Owed: ${debt_total:.2f}\n\nNote: Give this to ZIMRA"
        box = BoxLayout(orientation='vertical', padding=10)
        box.add_widget(Label(text=txt))
        b = Button(text="Close", size_hint_y=None, height=50)
        box.add_widget(b)
        pop = Popup(title="ZIMRA Report", content=box, size_hint=(0.9,0.8))
        b.bind(on_press=lambda x: pop.dismiss())
        pop.open()

MariApp().run()
