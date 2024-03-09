# Create the language teaching assistant
from openai import OpenAI
import time

client = OpenAI(api_key="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")

assistant = client.beta.assistants.create(
    name="Lang_bot",
    instructions="You are a helpful assistant who interacts with the user to teach them languages. You have to clear their doubts and answer to the point. Assume the role given by the user and continue to chat with them.",
    #tools=[{"type": "retrieval"}],
    model="gpt-3.5-turbo-0125"  # or any other language-focused model
)

print(assistant)
#Assistant(id='asst_U4KyfS9qOgI6vGKr2PKTAFgp', created_at=1709974491, description=None, file_ids=[], instructions='You are a helpful assistant who interacts with the user to teach them languages. You have to clear their doubts and answer to the point. Assume the role given by the user and continue to chat with them.', metadata={}, model='gpt-3.5-turbo-0125', name='Lang_bot', object='assistant', tools=[])

# Create a new thread
thread = client.beta.threads.create()

# Add a message to the thread
message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Can you generate a conversation between a shopkeeper and a customer."
)

print(thread)
print(message)

# Run the assistant on the thread
run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id=assistant.id,
    #messages=messages_data,
    instructions="Please address the user as User. Consider the user as beginner "
)

print(run)

while run.status != 'completed':
    time.sleep(1);
    run = client.beta.threads.runs.retrieve(thread_id = thread.id, run_id = run.id)
    print(run.status)

messages = client.beta.threads.messages.list(
    thread_id=thread.id,
)

print(messages)
print(messages.data[0].content[0].text.value)


'''
for msg in reversed(messages.data):
    print(msg.content[0].text.value)
'''
