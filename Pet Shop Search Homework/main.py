PETS = ["hamster", "rabbit", "parrot", "goldfish", "turtle", "puppy", "kitten", "guinea pig"]
MAX_FIXES = 2
TEST_SEARCHES = [
    ("hamstr", "hamster"),
    ("rabit", "rabbit"),
    ("parott", "parrot"),
    ("gold fish", "goldfish"),
    ("puppee", "puppy"),
    ("pig", "guinea pig"),
]
def edit_distance(a, b):
    table = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        table[i][0] = i
    for j in range(len(b) + 1):
        table[0][j] = j
    return 0
print("PART 1: Edit distance")
print(edit_distance("cat", "cut"), edit_distance("rabit", "rabbit"))
def closest(search):
    return (0, "")
print("\nPART 2: Closest pet")
print(closest("parott"))
def did_you_mean(search):
    return "no match"
print("\nPART 3: Did you mean?")
print(did_you_mean("hamstr"), "|", did_you_mean("elephant"))
print("\nPART 4: Test all searches")
mistakes = 0