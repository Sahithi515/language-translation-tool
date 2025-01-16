import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def translate_text():
    try:
        src_text = source_text.get("1.0", tk.END).strip()
        src_lang = src_lang_combo.get()
        dest_lang = dest_lang_combo.get()
        
        if not src_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        translator = Translator()
        src_lang_code = next(key for key, value in LANGUAGES.items() if value == src_lang)
        dest_lang_code = next(key for key, value in LANGUAGES.items() if value == dest_lang)

        translation = translator.translate(src_text, src=src_lang_code, dest=dest_lang_code)
        translated_text.delete("1.0", tk.END)
        translated_text.insert(tk.END, translation.text)
    except Exception as e:
        messagebox.showerror("Translation Error", str(e))


app = tk.Tk()
app.title("Language Translator")
app.geometry("600x400")
app.resizable(False, False)

# Source Text Label and Textbox
tk.Label(app, text="Enter Text:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
source_text = tk.Text(app, height=8, width=60)
source_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Source Language Selection
tk.Label(app, text="Source Language:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="w")
src_lang_combo = ttk.Combobox(app, values=list(LANGUAGES.values()), state="readonly", width=30)
src_lang_combo.grid(row=2, column=1, padx=10, pady=5)
src_lang_combo.set("english")  # Default value

# Destination Language Selection
tk.Label(app, text="Destination Language:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="w")
dest_lang_combo = ttk.Combobox(app, values=list(LANGUAGES.values()), state="readonly", width=30)
dest_lang_combo.grid(row=3, column=1, padx=10, pady=5)
dest_lang_combo.set("spanish")  # Default value

# Translate Button
translate_button = tk.Button(app, text="Translate", command=translate_text, font=("Arial", 12))
translate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Translated Text Label and Textbox
tk.Label(app, text="Translated Text:", font=("Arial", 12)).grid(row=5, column=0, padx=10, pady=10, sticky="w")
translated_text = tk.Text(app, height=8, width=60)
translated_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Run the GUI application
app.mainloop()
