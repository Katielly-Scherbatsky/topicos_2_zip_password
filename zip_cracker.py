import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import time

def tentar_senhas(zip_path, wordlist_path, status_label):
    try:
        zip_file = zipfile.ZipFile(zip_path)

        encodings = ['utf-8', 'latin-1']
        for enc in encodings:
            try:
                with open(wordlist_path, 'r', encoding=enc) as wordlist:
                    for linha in wordlist:
                        senha = linha.strip()
                        try:
                            zip_file.extractall(pwd=bytes(senha, 'utf-8'))
                            status_label.config(text=f"✅ Senha encontrada: {senha}", fg="lightgreen")
                            return
                        except:
                            status_label.config(text=f"Senha: {senha} ❌ (errada)", fg="white")
                            status_label.update()
                            time.sleep(0.05)
                break
            except UnicodeDecodeError:
                continue

        status_label.config(text="❌ Nenhuma senha funcionou.", fg="red")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def iniciar_brute_force(zip_entry, wordlist_entry, status_label):
    zip_path = zip_entry.get()
    wordlist_path = wordlist_entry.get()

    if not zip_path or not wordlist_path:
        messagebox.showwarning("Atenção", "Por favor, selecione o ZIP e a Wordlist.")
        return

    threading.Thread(target=tentar_senhas, args=(zip_path, wordlist_path, status_label), daemon=True).start()

def escolher_arquivo(entry):
    path = filedialog.askopenfilename()
    if path:
        entry.delete(0, tk.END)
        entry.insert(0, path)

# GUI
root = tk.Tk()
root.title("ZIP Password Cracker")
root.geometry("500x280")
root.configure(bg="#0d1117")  # fundo escuro

def estilo_widget(widget):
    widget.configure(bg="#161b22", fg="white", insertbackground="white", relief="flat", highlightbackground="#30363d")

tk.Label(root, text="Arquivo ZIP:", bg="#0d1117", fg="white").pack()
zip_entry = tk.Entry(root, width=60)
estilo_widget(zip_entry)
zip_entry.pack()
tk.Button(root, text="Selecionar ZIP", command=lambda: escolher_arquivo(zip_entry), bg="#161b22", fg="white").pack(pady=2)

tk.Label(root, text="Wordlist:", bg="#0d1117", fg="white").pack()
wordlist_entry = tk.Entry(root, width=60)
estilo_widget(wordlist_entry)
wordlist_entry.pack()
tk.Button(root, text="Selecionar Wordlist", command=lambda: escolher_arquivo(wordlist_entry), bg="#161b22", fg="white").pack(pady=2)

status_label = tk.Label(root, text="Aguardando...", fg="white", bg="#0d1117", wraplength=480)
status_label.pack(pady=10)

tk.Button(root, text="Iniciar Ataque", command=lambda: iniciar_brute_force(zip_entry, wordlist_entry, status_label),
          bg="#238636", fg="white", activebackground="#2ea043", relief="flat", padx=10, pady=5).pack(pady=10)

root.mainloop()
