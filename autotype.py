import tkinter as tk
from tkinter import messagebox
import threading
import pyautogui
import keyboard
import time
import re
import ctypes

class AutotypeUI:
    def __init__(self, master):
        # High DPI Awareness for clearer text on modern laptops
        try:
            ctypes.windll.shcore.SetProcessDpiAwareness(1)
        except Exception:
            try:
                ctypes.windll.user32.SetProcessDPIAware()
            except Exception:
                pass

        master.title("Auto Typer by Adhavan ")
        master.geometry("520x390")
        master.resizable(False, False)

        # Shortcut Key
        tk.Label(master, text="Shortcut Key:").place(x=10, y=10)
        self.hotkey_entry = tk.Entry(master, width=15)
        self.hotkey_entry.insert(0, "F6")
        self.hotkey_entry.place(x=100, y=10)

        tk.Label(master, text="[Use one key at time]").place(x=230, y=10)

        # Comments
        comment = "Welcome to autotyper by Adhavan"
        tk.Label(master, text="Comments:").place(x=10, y=40)
        self.comment_box = tk.Label(master, text=comment, wraplength=480, justify="left")
        self.comment_box.place(x=10, y=60)

        # Text Box
        tk.Label(master, text="Text:").place(x=10, y=100)
        self.text_input = tk.Text(master, width=62, height=6)
        self.text_input.place(x=10, y=120)

        # Checkbox
        self.special_key_var = tk.BooleanVar()
        tk.Checkbutton(master, text="Simulate Paste Command & No Special Key Processing",
                       variable=self.special_key_var).place(x=10, y=230)

        # Buttons
        self.ok_button = tk.Button(master, text="OK", width=10, command=self.prepare_typing)
        self.ok_button.place(x=150, y=270)

        self.cancel_button = tk.Button(master, text="Cancel", width=10, command=master.quit)
        self.cancel_button.place(x=250, y=270)

        self.special_button = tk.Button(master, text="Special Keys", width=12, command=self.show_special_keys)
        self.special_button.place(x=10, y=330)


        self.running = False
        self.bound_hotkey = None

    def prepare_typing(self):
        self.text_to_type = self.text_input.get("1.0", tk.END).strip()
        if not self.text_to_type:
            messagebox.showerror("Error", "Please enter text to type.")
            return

        new_hotkey = self.hotkey_entry.get().strip().lower()
        if not new_hotkey:
            messagebox.showerror("Error", "Please enter a valid Autotype key (e.g., F1-F12,0-9")
            return

        try:
            if self.bound_hotkey:
                keyboard.remove_hotkey(self.bound_hotkey)

            self.bound_hotkey = keyboard.add_hotkey(new_hotkey, self.toggle_typing, suppress=True)
            messagebox.showinfo("Hotkey Set", f"Hotkey '{new_hotkey.upper()}' registered.\nSwitch to any window and press it to start.")
        except Exception as e:
            messagebox.showerror("Hotkey Error", f"Could not bind hotkey: {e}\n\nTry running this program as Administrator.")

    def toggle_typing(self):
        if self.running:
            self.running = False
        else:
            if not hasattr(self, 'text_to_type') or not self.text_to_type:
                return
            self.running = True
            threading.Thread(target=self.start_typing, daemon=True).start()

    def parse_and_type(self, text):
        tokens = re.split(r"(\{[A-Z]+\})", text)
        for token in tokens:
            if not self.running:
                break
            if re.fullmatch(r"\{[A-Z]+\}", token):
                key = token.strip("{}").lower()
                pyautogui.press(key)
            else:
                pyautogui.typewrite(token, interval=0.05)

    def start_typing(self):
        if self.special_key_var.get():
            pyautogui.write(self.text_to_type)
            pyautogui.press("enter")
        else:
            self.parse_and_type(self.text_to_type)
        self.running = False

    def show_special_keys(self):
        guide = """Use special key tags like:
{ENTER}, {TAB}, {BACKSPACE}, {ESC}, {SPACE}
They will be interpreted as keystrokes."""
        messagebox.showinfo("Special Keys Guide", guide)

    def download_stub(self):
        messagebox.showinfo("Info", "This is a placeholder for .NET download.")


if __name__ == "__main__":
    root = tk.Tk()
    app = AutotypeUI(root)
    root.mainloop()
