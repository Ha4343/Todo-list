import tkinter as tk
from tkinter import messagebox
import random

# Motivational messages
messages = [
    "Great job! Keep going! 🚀",
    "One step closer to success! 🎯",
    "You're unstoppable! 🔥",
    "Task smashed! Keep it up! 💪",
    "Small steps make big changes! 🌟"
]

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List with a Twist")
        self.root.geometry("400x500")
        
        self.tasks = []
        
        # Entry field
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        
        # Buttons
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.pack(pady=5)
        
        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(pady=5)
        
        # Listbox
        self.task_listbox = tk.Listbox(root, width=50, height=15)
        self.task_listbox.pack(pady=10)
        
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    
    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            self.tasks.pop(selected_index)
            messagebox.showinfo("Completed!", random.choice(messages))
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to complete!")
    
    def remove_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            self.tasks.pop(selected_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove!")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
