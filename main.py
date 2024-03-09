from flask import Flask, render_template, url_for, request, jsonify
# import openai
# from openai import OpenAI
import time

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return render_template("index.html",url_for=url_for)  

@app.route("/conversation")
def conversation():
    return render_template("conversation.html") 

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

# @app.route('/oral')
# def oral():
#     return render_template('oral.html')
# def openai_endpoint():
#     user_input = request.json.get('userInput')
#     # Create the language teaching assistant

#     client = OpenAI(api_key="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")

#     assistant = client.beta.assistants.create(
#         name="Lang_bot",
#         instructions="You are a helpful assistant who interacts with the user to teach them languages. You have to clear their doubts and answer to the point. Assume the role given by the user and continue to chat with them.",
#         #tools=[{"type": "retrieval"}],
#         model="gpt-3.5-turbo-0125"  # or any other language-focused model
#     )

#     # Create a new thread
#     thread = client.beta.threads.create()

#     # Add a message to the thread
#     message = client.beta.threads.messages.create(
#         thread_id=thread.id,
#         role="user",
#         content=request.json.get('userInput')
#     )

#     # Run the assistant on the thread
#     run = client.beta.threads.runs.create(
#         thread_id=thread.id,
#         assistant_id=assistant.id,
#         #messages=messages_data,
#         instructions="Please address the user as User. Consider the user as beginner "
#     )

#     print(run)

#     while run.status != 'completed':
#         time.sleep(1);
#         run = client.beta.threads.runs.retrieve(thread_id = thread.id, run_id = run.id)
#         print(run.status)

#     messages = client.beta.threads.messages.list(
#         thread_id=thread.id,
#     )

#     print(messages)
#     print(messages.data[0].content[0].text.value)

# def openai_endpoint():
#     message = request.json.get('message')
#     # Use OpenAI logic here to generate response
#     response = openai.Completion.create(
#         engine="text-davinci-002",
#         prompt=message,
#         max_tokens=50
#     )
#     return jsonify({'message': response['choices'][0]['text']})

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)