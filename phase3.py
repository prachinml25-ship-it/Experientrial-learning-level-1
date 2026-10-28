import tkinter as tk
from tkinter import messagebox
import random

stories = [
    "One day, a {adj} {noun} went to {place}. "
    "It decided to {verb} {adv} and made everyone laugh!",

    "At {place}, a {adj} {noun} suddenly started to "
    "{verb} {adv}. Everyone was surprised!",

    "A {adj} {noun} visited {place} and began to "
    "{verb} {adv}. It became famous!"
]


def generate_story():
    noun = noun_entry.get().strip()
    verb = verb_entry.get().strip()
    adj = adj_entry.get().strip()
    adv = adv_entry.get().strip()
    place = place_entry.get().strip()

    if not all([noun, verb, adj, adv, place]):
        messagebox.showerror(
            "Input Error", "Please fill in all fields!"
        )
        return

    story_template = random.choice(stories)

    story = story_template.format(
        noun=noun,
        verb=verb,
        adj=adj,
        adv=adv,
        place=place
    )

    output.delete("1.0", tk.END)
    output.insert(tk.END, story)


def save_story():
    story = output.get("1.0", tk.END).strip()

    if not story:
        messagebox.showwarning(
            "Warning", "Generate a story first!"
        )
        return

    try:
        with open("madlibs_stories.txt", "a") as file:
            file.write(story + "\n\n")

        messagebox.showinfo(
            "Success", "Story saved successfully!"
        )

    except OSError:
        messagebox.showerror(
            "Error", "Unable to save the story!"
        )


root = tk.Tk()
root.title("Mad Libs Generator")
root.geometry("450x550")

tk.Label(
    root, text="MAD LIBS GENERATOR",
    font=("Arial", 18, "bold")
).pack(pady=15)


def create_input(label):
    tk.Label(root, text=label).pack()
    entry = tk.Entry(root, width=35)
    entry.pack(pady=4)
    return entry


noun_entry = create_input("Enter a noun:")
verb_entry = create_input("Enter a verb:")
adj_entry = create_input("Enter an adjective:")
adv_entry = create_input("Enter an adverb:")
place_entry = create_input("Enter a place:")

tk.Button(
    root, text="Generate Story",
    command=generate_story
).pack(pady=10)

output = tk.Text(root, height=6, width=45, wrap=tk.WORD)
output.pack(pady=5)

tk.Button(
    root, text="Save Story",
    command=save_story
).pack(pady=10)

root.mainloop()
