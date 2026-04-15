
import tkinter as tk

blocked_keywords = ["dark", "hack", "illegal","x hamster","hentai","xxx.com","incognito tab"]
history = []
danger_count = 0

def check_website():
   global danger_count
   
   website = entry.get().lower()
   history.append(website)
   reasons = []

   if any(word in website for word in blocked_keywords):
       reasons.append("Contains risky keywords")

   if "http" in website and not website.startswith("https"):
        reasons.append("No https (not secure)") 

   if len(website) > 25: 
       reasons.append("Very long URL (suspicious)")     

   if reasons:
      danger_count += 1
      result_label.config(text="⚠ Unsafe!\n" + "\n".join(reasons), fg="red") 
        
   else:
       result_label.config(text="Safe Website", fg="green")
       
       history_label.config(text="History: " + ", ".join(history))
       danger_label.config(text="Danger Count: " + str(danger_count)) 
        
# GUI
root = tk.Tk()
root.title("SafeNet")
root.geometry("300x250")
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=10)

button = tk.Button(root, text="Check Website", command=check_website)
button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

history_label = tk.Label(root, text="History: ")
history_label.pack()
danger_label = tk.Label(root, text="Danger Count: 0")
danger_label.pack()

root.mainloop()
