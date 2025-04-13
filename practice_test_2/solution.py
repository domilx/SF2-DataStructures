import json

class Quest:
    def __init__(self, name, difficulty, participants):
        self.name = name
        self.difficulty = difficulty
        self.participants = participants

    def __lt__(self, other):
        return self.difficulty < other.difficulty

    def __repr__(self):
        return f"Quest({self.name}, {self.difficulty}, {self.participants})"

try:
    f = open("quests.json", "r")
    data = json.load(f)
    f.close()
except Exception:
    exit("Error reading file")

# Prompt for difficulty threshold.
threshold_input = input("Enter difficulty threshold: ")
try:
    threshold = int(threshold_input)
except Exception:
    exit("Invalid threshold.")

# Create list for filtered quests.
filtered_quests = []
i = 0
while i < len(data):
    quest_dict = data[i]
    # Create Quest object from dictionary.
    quest = Quest(quest_dict["name"], quest_dict["difficulty"], quest_dict["participants"])
    # Use relational operator to check difficulty.
    if quest.difficulty >= threshold:
        filtered_quests.append(quest)
    i += 1

# Sort filtered quests by difficulty (ascending).
filtered_quests.sort()

# Build list of quest names and set of unique participants.
quest_names = []
unique_participants = set()
j = 0
while j < len(filtered_quests):
    quest_names.append(filtered_quests[j].name)
    k = 0
    while k < len(filtered_quests[j].participants):
        unique_participants.add(filtered_quests[j].participants[k])
        k += 1
    j += 1

print("Filtered quests:", quest_names)
print("Unique participants:", unique_participants)
