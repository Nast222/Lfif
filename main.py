import tkinter as tk
from tkinter import messagebox
import json
import random
import os

FILENAME = 'quotes.json'

def load_quotes():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def save_quotes(quotes):
    with open(FILENAME, 'w', encoding='utf-8') as f:
        json.dump(quotes, f, ensure_ascii=False, indent=2)

def generate_quote():
    if not quotes:
        messagebox.showinfo('Цитаты', 'Список цитат пуст!')
        return
    quote = random.choice(quotes)
    quote_text.set(f'"{quote["text"]}"')
    quote_author.set(f'— {quote["author"]}')
    quote_theme.set(f'Тема: {quote["theme"]}')
    history_listbox.insert(0, f'"{quote["text"]}" — {quote["author"]}')

def filter_quotes():
    author = entry_author_filter.get().strip().lower()
    theme = entry_theme_filter.get().strip().lower()
    filtered = [
        q for q in quotes
        if (not author or author in q["author"].lower()) and
           (not theme or theme in q["theme"].lower())
    ]
    update_listbox(filtered)

def update_listbox(data=None):
    listbox.delete(0, tk.END)
    for q in (data or quotes):
        listbox.insert(tk.END, f'"{q["text"]}" — {q["author"]} | Тема: {q["theme"]}')

# Загрузка цитат
quotes = load_quotes()

# Создание окна
root = tk.Tk()
root.title('Генератор случайных цитат')
root.geometry('600x500')

# Переменные для отображения
quote_text = tk.StringVar()
quote_author = tk.StringVar()
quote_theme = tk.StringVar()

# Вывод текущей цитаты
tk.Label(root, textvariable=quote_text, wraplength=500, font=('Arial', 12)).pack(pady=10)
tk.Label(root, textvariable=quote_author, font=('Arial', 10)).pack()
tk.Label(root, textvariable=quote_theme, font=('Arial', 10)).pack()

# Кнопка генерации
tk.Button(root, text='Сгенерировать цитату', command=generate_quote).pack(pady=10)

# Фильтрация
tk.Label(root, text='Фильтр по автору:').pack()
entry_author_filter = tk.Entry(root)
entry_author_filter.pack()
tk.Label(root, text='Фильтр по теме:').pack()
entry_theme_filter = tk.Entry(root)
entry_theme_filter.pack()
tk.Button(root, text='Применить фильтр', command=filter_quotes).pack(pady=5)

# Список всех цитат
listbox = tk.Listbox(root, width=70, height=10)
listbox.pack(pady=10)
update_listbox()

# История сгенерированных цитат
tk.Label(root, text='История:').pack()
history_listbox = tk.Listbox(root, width=70, height=5)
history_listbox.pack(pady=10)

root.mainloop()
