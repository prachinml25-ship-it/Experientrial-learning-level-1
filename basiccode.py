story = "One day, a {adj} {noun} went to {place}. " \
        "It decided to {verb} {adv}!"

noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adj = input("Enter an adjective: ")
adv = input("Enter an adverb: ")
place = input("Enter a place: ")

result = story.format(
    noun=noun,
    verb=verb,
    adj=adj,
    adv=adv,
    place=place
)

print("\n--- GENERATED STORY ---")
print(result)
