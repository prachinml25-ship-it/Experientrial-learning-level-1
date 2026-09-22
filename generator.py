stories = [
    "One day, a {adj} {noun} went to {place}. "
    "It decided to {verb} {adv} and made everyone laugh!",

    "At {place}, a {adj} {noun} suddenly started to "
    "{verb} {adv}. Everyone was surprised!"
]

while True:
    print("\n--- MAD LIBS GENERATOR ---")
    print("1. Funny Adventure")
    print("2. Crazy Day")

    choice = int(input("Choose a template (1/2): "))

    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adj = input("Enter an adjective: ")
    adv = input("Enter an adverb: ")
    place = input("Enter a place: ")

    story = stories[choice - 1].format(
        noun=noun,
        verb=verb,
        adj=adj,
        adv=adv,
        place=place
    )

    print("\n--- GENERATED STORY ---")
    print(story)

    save = input("\nSave story? (yes/no): ")

    if save.lower() == "yes":
        with open("madlibs_stories.txt", "a") as file:
            file.write(story + "\n\n")
        print("Story saved successfully!")

    again = input("\nCreate another story? (yes/no): ")

    if again.lower() != "yes":
        break

print("\nThank you for using Mad Libs Generator!")
