import tkinter as tk
from tkinter import scrolledtext
import subprocess

def test_endpoint():
    url = entry_url.get()
    method = method_var.get()
    headers = entry_headers.get("1.0", tk.END).strip()
    data = entry_data.get("1.0", tk.END).strip()

    curl_command = ["curl", "-X", method, url]

    if headers:
        for header in headers.split("\n"):
            curl_command.extend(["-H", header])

    if data:
        curl_command.extend(["-d", data])

    try:
        result = subprocess.run(curl_command, capture_output=True, text=True)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, result.stdout)
    except Exception as e:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, str(e))

root = tk.Tk()
root.title("endPointer 1.0")

tk.Label(root, text="URL:").grid(row=0, column=0, sticky=tk.W)
entry_url = tk.Entry(root, width=50)
entry_url.grid(row=0, column=1)

tk.Label(root, text="Método:").grid(row=1, column=0, sticky=tk.W)
method_var = tk.StringVar(value="GET")
tk.OptionMenu(root, method_var, "GET", "POST", "PUT", "DELETE").grid(row=1, column=1, sticky=tk.W)

tk.Label(root, text="Headers (uno por línea):").grid(row=2, column=0, sticky=tk.NW)
entry_headers = scrolledtext.ScrolledText(root, width=50, height=5)
entry_headers.grid(row=2, column=1, padx=5, pady=5)
tk.Label(root, text="Datos (JSON):").grid(row=3, column=0, sticky=tk.NW)
entry_data = scrolledtext.ScrolledText(root, width=50, height=5)
entry_data.grid(row=3, column=1, padx=5, pady=5)

tk.Button(root, text="Probar Endpoint", command=test_endpoint).grid(row=4, column=0, columnspan=2, pady=10)

tk.Label(root, text="Salida:").grid(row=5, column=0, sticky=tk.NW)
output_text = scrolledtext.ScrolledText(root, width=80, height=10)
output_text.grid(row=5, column=1, padx=5, pady=5)

root.mainloop()
