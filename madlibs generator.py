# Open the file "story.txt" in read mode and read its content into the variable 'story'
with open("story.txt", "r") as f:
    story = f.read()

# Initialize an empty set to store unique placeholder words
words = set()
# Variable to keep track of the start position of a placeholder word
start_of_word = -1

# Define the start and end characters of the placeholder words
target_start = "<"
target_end = ">"

# Iterate through each character in the story along with its index
for i, char in enumerate(story):
    # If the current character is the start of a placeholder word
    if (char == target_start):
        # Record the start index of the placeholder word
        start_of_word = i

    # If the current character is the end of a placeholder word and a start has been recorded
    if (char == target_end and start_of_word != -1):
        # Extract the placeholder word from the story
        word = story[start_of_word: i + 1]
        # Add the extracted placeholder word to the set of words
        words.add(word)
        # Reset the start_of_word to indicate that the placeholder word has been processed
        start_of_word = -1

# Initialize an empty dictionary to store the user's answers for each placeholder word
answers = {}

# Prompt the user to enter a word for each unique placeholder word
for word in words:
    answer = input("Enter a word for " + word + ": ")
    # Store the user's answer in the dictionary, with the placeholder word as the key
    answers[word] = answer

# Replace each placeholder word in the story with the user's corresponding answer
for word in words:
    story = story.replace(word, answers[word])

# Print the modified story
print(story)
