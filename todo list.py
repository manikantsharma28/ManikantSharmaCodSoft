import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.tasks = []
        
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()
        
        self.listbox = tk.Listbox(root, width=40)
        self.listbox.pack(pady=10)
        
        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack()
        
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")
    
    def complete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.listbox.delete(task_index)
            self.tasks.pop(task_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to complete.")
    
    def delete_task(self):
        selected_task_index = self.listbox.curselection()
        if selected_task_index:
            task_index = selected_task_index[0]
            self.listbox.delete(task_index)
            self.tasks.pop(task_index)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
