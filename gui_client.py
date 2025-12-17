import tkinter as tk
from tkinter import messagebox
from smtp_client import send_email

def send_email_gui():
    to_email = entry_to.get()
    subject = entry_subject.get()
    body = text_body.get("1.0", tk.END)

    if not to_email or not subject or not body.strip():
        messagebox.showerror("Error", "Please fill all fields")
        return

    try:
        send_email(to_email, subject, body)
        messagebox.showinfo("Success", "Email sent successfully")
        entry_to.delete(0, tk.END)
        entry_subject.delete(0, tk.END)
        text_body.delete("1.0", tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Main window
root = tk.Tk()
root.title("Email Client")
root.geometry("400x350")

# To Email
tk.Label(root, text="To Email:").pack(pady=5)
entry_to = tk.Entry(root, width=45)
entry_to.pack()

# Subject
tk.Label(root, text="Subject:").pack(pady=5)
entry_subject = tk.Entry(root, width=45)
entry_subject.pack()

# Body
tk.Label(root, text="Message:").pack(pady=5)
text_body = tk.Text(root, height=8, width=45)
text_body.pack()

# Send Button
tk.Button(root, text="Send Email", command=send_email_gui).pack(pady=15)

root.mainloop()