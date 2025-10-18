import tkinter as tk
from tkinter import messagebox
import math

# Window Setup
wn = tk.Tk()
wn.title("Calculator")
wn.geometry('450x800')

# Global Variables
out = tk.StringVar(value="0") 
history = tk.StringVar(value="") 
operator = tk.StringVar(value="") 

# Values
inp0_str = tk.StringVar(value="0") 
inp1_str = tk.StringVar(value="") 
result_float = tk.DoubleVar(value=0.0) 

# Process state
global proc
proc = tk.StringVar(value="") 
dot_active = tk.BooleanVar(value=False)

# Output
cnr = tk.Frame(wn, height=150, bg='lightgray')
cnr.pack(fill=tk.X, side=tk.TOP)
cnr.pack_propagate(False)

# History
lbl_history = tk.Label(cnr, bg='lightgray', fg='darkgray', font=('Arial', 20), textvariable=history, anchor='se', padx=10)
lbl_history.pack(fill=tk.X, side=tk.TOP)

# Result display
res = tk.Label(cnr, bg='lightgray', font=('Arial', 60, 'bold'), textvariable=out, anchor='se', padx=10)
res.pack(fill=tk.X, side=tk.BOTTOM)

# Initialize display
out.set("0")
inp0_str.set("0")

#Frame for Buttons
cfm = tk.Frame(wn, bg='#000000')
cfm.pack(fill=tk.BOTH, expand=True)

#Grid Positioning
for i in range(4):
    cfm.columnconfigure(i, weight=1)
for i in range(6): # 6 rows for buttons
    cfm.rowconfigure(i, weight=1)

#Commands

def update_display(value_str):
    if value_str.endswith(".0"):
        value_str = value_str[:-2]
    
    if len(value_str) > 12: 
        out.set(f"{float(value_str):.5e}") 
    else:
        out.set(value_str if value_str != "" else "0")

def number_click(number):
    current_proc = proc.get()
    
    if not current_proc:
        target_str_var = inp0_str
    else:
        target_str_var = inp1_str

    current_val = target_str_var.get()

    if current_val == "0":
        new_val = str(number)
    else:
        if len(current_val) < 15:
             new_val = current_val + str(number)
        else:
             new_val = current_val
             
    target_str_var.set(new_val)
    update_display(new_val)

def decimal_click():
    current_proc = proc.get()
    
    if not current_proc:
        target_str_var = inp0_str
    else:
        target_str_var = inp1_str
    
    current_val = target_str_var.get()
    
    if "." not in current_val:
        new_val = current_val + "."
        target_str_var.set(new_val)
        out.set(new_val)

def operator_click(op_symbol):

    if inp0_str.get() == "":
        return 

    if proc.get() and inp1_str.get():
        equal_click()
    
    proc.set(op_symbol)
    operator.set(op_symbol) 
    inp1_str.set("") 
    history.set(inp0_str.get() + " " + op_symbol)
    out.set(inp0_str.get()) 


def equal_click():

    op = proc.get()
    num1_str = inp0_str.get()
    num2_str = inp1_str.get()

    if not op or not num2_str:
        return 
    
    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
        result = 0.0

        if op == '÷':
            if num2 == 0:
                out.set("Error: Div by 0")
                return 
            result = num1 / num2
        elif op == '×':
            result = num1 * num2
        elif op == '–':
            result = num1 - num2
        elif op == '+':
            result = num1 + num2
            
        #Final Result
        final_result = round(result, 8) 
        final_result_str = str(final_result)
        
        history.set(f"{num1_str} {op} {num2_str} =")
        inp0_str.set(final_result_str) 
        inp1_str.set("") 
        proc.set("")
        
        update_display(final_result_str)
        
    except ValueError:
        out.set("Error: Invalid Input")
        inp0_str.set("0")
        inp1_str.set("")
        proc.set("")
        history.set("")


def clear_entry():

    if proc.get():
        inp1_str.set("")
        out.set("0")
    else:
        inp0_str.set("0")
        out.set("0")


def clear_all():

    inp0_str.set("0")
    inp1_str.set("")
    proc.set("")
    out.set("0")
    history.set("")


def backspace():
    current_proc = proc.get()
    target_str_var = inp1_str if current_proc else inp0_str
    
    current_val = target_str_var.get()
    if current_val:
        new_val = current_val[:-1]
        if not new_val or new_val == '-':
            new_val = "0"
            if not current_proc:
                history.set("") 
        
        target_str_var.set(new_val)
        update_display(new_val)


def unary_operation(op_type):
    
    target_str_var = inp1_str if proc.get() and inp1_str.get() else inp0_str
    current_val_str = target_str_var.get()
    
    if not current_val_str: return
    
    try:
        val = float(current_val_str)
        result = 0.0

        if op_type == 'percent':
            result = val / 100
        elif op_type == 'sqrt':
            if val < 0:
                out.set("Error: Imaginary")
                return
            result = math.sqrt(val)
        elif op_type == 'square':
            result = val ** 2
        elif op_type == 'reciprocal':
            if val == 0:
                out.set("Error: Div by 0")
                return
            result = 1 / val
        elif op_type == 'negate':
            result = -val
            

        final_result = round(result, 8) 
        final_result_str = str(final_result)

        target_str_var.set(final_result_str)
        update_display(final_result_str)
        
    except ValueError:
        out.set("Error")
        


#Button Placement

def create_button(text, command, row, col, font_size=40, style='standard'):
    bg_color = {
        'clear': '#FFB03A', 
        'operator': '#A4A4A4', 
        'number': '#EAEAEA', 
        'equal': '#3CB371' 
    }.get(style, '#EAEAEA')
    
    fg_color = 'black' if style in ['number', 'clear'] else 'white'
    
    if text in ['CE', 'C', '⌫']:
        style = 'clear'
        bg_color = '#FFB03A'
        fg_color = 'black'
    elif text in ['÷', '×', '–', '+']:
        style = 'operator'
        bg_color = '#A4A4A4'
        fg_color = 'white'
    elif text == '=':
        style = 'equal'
        bg_color = '#3CB371'
        fg_color = 'white'
    
    btn = tk.Button(cfm, text=text, font=('Arial', font_size, 'bold' if text in ['÷', '×', '–', '+', '='] else ''), 
                    command=command, bg=bg_color, fg=fg_color, bd=0)
    btn.grid(row=row, column=col, sticky=tk.NSEW, padx=2, pady=2)
    return btn


create_button('CE', clear_entry, 0, 0, font_size=30, style='clear')
create_button('C', clear_all, 0, 1, font_size=30, style='clear')
create_button('%', lambda: unary_operation('percent'), 0, 2, font_size=30, style='operator')
create_button('⌫', backspace, 0, 3, font_size=40, style='clear')

create_button('√', lambda: unary_operation('sqrt'), 1, 0, font_size=30, style='operator')
create_button('x²', lambda: unary_operation('square'), 1, 1, font_size=30, style='operator')
create_button('¹/ₓ', lambda: unary_operation('reciprocal'), 1, 2, font_size=30, style='operator')
create_button('÷', lambda: operator_click('÷'), 1, 3, font_size=40, style='operator')

create_button('7', lambda: number_click(7), 2, 0)
create_button('8', lambda: number_click(8), 2, 1)
create_button('9', lambda: number_click(9), 2, 2)
create_button('×', lambda: operator_click('×'), 2, 3, font_size=40, style='operator')

create_button('4', lambda: number_click(4), 3, 0)
create_button('5', lambda: number_click(5), 3, 1)
create_button('6', lambda: number_click(6), 3, 2)
create_button('–', lambda: operator_click('–'), 3, 3, font_size=40, style='operator')

create_button('1', lambda: number_click(1), 4, 0)
create_button('2', lambda: number_click(2), 4, 1)
create_button('3', lambda: number_click(3), 4, 2)
create_button('+', lambda: operator_click('+'), 4, 3, font_size=40, style='operator')

create_button('±', lambda: unary_operation('negate'), 5, 0, font_size=30)
create_button('0', lambda: number_click(0), 5, 1)
create_button('.', decimal_click, 5, 2, font_size=40)
create_button('=', equal_click, 5, 3, font_size=40, style='equal')


wn.mainloop()