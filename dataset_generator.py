import random
import datetime

# Define group members
members = ["Rahul", "Priya", "Aman", "Neha", "Vikram", "Sonia", "Arjun", "Divya", "Rohit", "Meera", "Alice", "Bob", "Charlie", "Dave", "Eve", "Frank", "Grace", "Harry"]

# Sample messages (including emojis)
messages = [
    "Hey, what’s up?"
    "How’s everyone doing?"
    "Long time no see!"
    "Anyone free to hang out this weekend?"
    "What are you all up to?"
    "I’m so bored right now."
    "Did you see the latest episode of that show?"
    "I can’t believe it’s already Friday!"
    "What’s for dinner tonight?"
    "I’m so tired today."
    "Let’s plan a trip next month!"
    "Who’s coming to the party tonight?"
    "What time should we meet?"
    "I’ll book the tickets, don’t worry."
    "Don’t forget to bring your ID."
    "I’ll pick you up at 7."
    "Let’s do a potluck—everyone bring something."
    "I’m running late, sorry!"
    "Can someone send me the address?"
    "I’ll handle the decorations."
    "OMG, that’s amazing!"
    "No way!"
    "I’m so happy for you!"
    "This is hilarious!"
    "I can’t stop laughing!"
    "That’s so sad."
    "I’m so angry right now."
    "Wow, that’s impressive!"
    "I’m speechless."
    "This made my day!"
    "What do you think about this idea?"
    "Can someone help me with this?"
    "Does anyone know a good restaurant nearby?"
    "Should we order food?"
    "What’s the plan for tomorrow?"
    "Who’s in charge of the music?"
    "Can we reschedule?"
    "What's the budget for this?"
    "Do you think it’s a good idea?"
    "Any suggestions for a movie to watch?"
    "Why did the chicken cross the road? "
    "Knock knock! Who’s there?"
    "I’m not lazy, I’m in energy-saving mode."
    "I’m not arguing, I’m just explaining why I’m right."
    "I’m not short, I’m concentrated awesome."
    "I’m not procrastinating, I’m just prioritizing fun."
    "I’m not weird, I’m limited edition."
    "I’m not late, everyone else is just early."
    "I’m not ignoring you, I’m just prioritizing my peace."
    "I’m not lost, I’m exploring alternative routes."
    "Did you finish the assignment?"
    "I have a deadline tomorrow, ugh."
    "Can someone explain this to me?"
    "I’m so stressed right now."
    "Let’s study together this weekend."
    "I need coffee to survive this day. ☕"
    "Who’s presenting first?"
    "I’m so done with this project."
    "Let’s take a break and grab some food."
    "I’m pulling an all-nighter tonight."
    "Hey everyone! What's the plan for today? 🤔",
    "Don't forget about the assignment deadline! ⏳",
    "Let's meet at 10:00 for a group discussion. 📚",
    "Good morning! Hope you all have a great day! ☀️",
    "Who’s up for a late-night coding session? 💻🔥",
    "Anyone available to discuss data structures? 🧩",
    "Congratulations on completing the project! 🎉",
    "Midterms are coming! Let’s plan a study session. 📖",
    "Who needs help with the DBMS topic? 🏗️",
    "What’s the update on our final year project? 🤖",
    "Weekend trip plan? Let's decide the place. 🏕️",
    "How was today's lecture? Did you all understand recursion? 🔄",
    "Let's have a mock interview session this weekend. 🎤",
    "Happy New Year, everyone! Hope this year is amazing for all of us. 🎊🎆",
    "Just solved a tough coding problem. Feeling great! 🚀",
    "Who’s up for a brainstorming session on AI models? 🤯",
    "I found a great tutorial on machine learning. Sharing the link. 🔗",
    "What time are we meeting tomorrow? ⏰",
    "Today's quiz was tough! How did you all do? 😵",
    "Need help with debugging my Python code. 🐍",
    "The OS lecture was really boring today. 😴",
    "Can someone share the notes from today’s class? 📄",
    "Let’s celebrate after exams! 🎊🍕",
    "I got selected for an internship! 🎉🔥",
    "Exams are over! Time to relax. 😌",
    "Interview tomorrow! Feeling nervous. 🤞",
    "Anyone free for a quick doubt-solving session? 🤓",
    "Assignment submitted! That was tough. 😓",
    "Who’s bringing snacks for the next study session? 🍕🍫",
    "AI is mind-blowing! Just read an article on neural networks. 🧠💡",
    "Today’s coding session was fun! Learned so much. 🎯",
    "Final semester vibes! Almost done with college. 🎓",
    "<Media omitted>",  # Represents an image/video sent in WhatsApp
    "<Media omitted>",
    "<Media omitted>"
]


# Function to generate random timestamps over a year
def generate_random_timestamp(start_date, end_date):
    delta = end_date - start_date
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start_date + datetime.timedelta(seconds=random_seconds)


# Set start and end dates for a full year
start_date = datetime.datetime(2024, 1, 1, 0, 0)
end_date = datetime.datetime(2024, 12, 31, 23, 59)

# Generate chat messages for a year
num_messages = 20000  # Adjust this to control the dataset size
chat_log = []

for _ in range(num_messages):
    timestamp = generate_random_timestamp(start_date, end_date)
    member = random.choice(members)
    message = random.choice(messages)

    formatted_timestamp = timestamp.strftime("%d/%m/%Y, %H:%M")
    chat_log.append(f"{formatted_timestamp} - {member}: {message}")

# Sort messages chronologically
chat_log.sort()

# Save chat to a file
with open("whatsapp_group_chat.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(chat_log))

print("WhatsApp group chat dataset generated successfully!")
