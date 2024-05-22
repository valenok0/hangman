import tkinter as tk
from tkinter import messagebox

word_to_guess = "python"

root = tk.Tk()
root.title("Виселица")
root.geometry("300x250+400+330")

max_attempts = 6
current_attempt = 1

hangman_images = [f"hangman_images/{i}.png" for i in range(max_attempts + 1)]

guessed_letters = ["_" for _ in word_to_guess]

def show_next_image():
    global current_attempt
    current_attempt += 1
    if current_attempt <= max_attempts:
        image_path = hangman_images[current_attempt]
        photo = tk.PhotoImage(file=image_path)
        image_label.config(image=photo)
        image_label.image = photo
    else:
        messagebox.showinfo("Игра окончена", "Вы проиграли!")
        root.destroy()

def check_letter():
    global current_attempt
    guessed_letter = entry.get()
    if guessed_letter in word_to_guess:
        messagebox.showinfo("Поздравляем!", f"Буква '{guessed_letter}' есть в слове.")
        for i, letter in enumerate(word_to_guess):
            if letter == guessed_letter:
                guessed_letters[i] = guessed_letter
        update_display()
        if "_" not in guessed_letters:
            messagebox.showinfo("Победа!", "Вы угадали слово!")
            root.destroy()
    else:
        messagebox.showerror("Ошибка!", f"Буквы '{guessed_letter}' нет в слове.")
        show_next_image()

def update_display():
    word_label.config(text=" ".join(guessed_letters))

word_label = tk.Label(root, text=" ".join(["_" for _ in word_to_guess]), font=("Arial", 20))
word_label.pack()

entry_label = tk.Label(root, text="Введите букву:")
entry_label.pack()

entry = tk.Entry(root)
entry.pack()

check_button = tk.Button(root, text="Проверить", command=check_letter)
check_button.pack()

image_path = hangman_images[current_attempt]
photo = tk.PhotoImage(file=image_path)
image_label = tk.Label(root, image=photo)
image_label.pack()

root.mainloop()