# Create the language teaching assistant
import openai
from openai import OpenAI
import time

client = OpenAI()

#create an assistant
assistant = client.beta.assistants.create(
    name="Eval_Bot",
    instructions="You are an language evaluator who interacts with the user to teach them languages. You have to ask questions to understand and check user's level of understanding of English by asking simple one word answer questions. you should chcek the user's answer to the question and reply whether its correct or not. after that ask the user if they want more questions. ",
    #tools=[{"type": "retrieval"}],
    model="gpt-3.5-turbo-0125"  # or any other language-focused model
)

# Create a new thread
thread = client.beta.threads.create()

# Add a message to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Can you generate a question to test user's basic proficiency in English."
)

# Run the assistant on the thread
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    #messages=messages_data,
    instructions="Please address the user as User. Consider the user as beginner "
)

while run.status != 'completed':
    time.sleep(1)
    run = client.beta.threads.runs.retrieve(thread_id = thread.id, run_id = run.id)
    print(run.status)

messages = client.beta.threads.messages.list(
    thread_id=thread.id,
)

#print(messages)
print(messages.data[0].content[0].text.value)

answer = input()   #take user input for q answering

# Add answer reply message to the thread
message2 = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=answer
)

# Run the assistant on the thread
run2 = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    #messages=messages_data,
    instructions="Please address the user as User. Consider the user as beginner "
)

#print(run)

while run2.status != 'completed':
    time.sleep(1)
    run = client.beta.threads.runs.retrieve(thread_id = thread.id, run_id = run.id)
    print(run2.status)

messages2 = client.beta.threads.messages.list(
    thread_id=thread.id,
)

#print(messages)
print(messages2.data[0].content[0].text.value)


'''
for msg in reversed(messages.data):
    print(msg.content[0].text.value)
'''
