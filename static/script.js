// Function to send user message
function sendMessage() {
    var userInput = document.getElementById("userInput").value;
    appendMessage(userInput, 'user');

    // Here you can implement OpenAI integration to get response
    var aiResponse = "This is a sample response from OpenAI.";
    appendMessage(aiResponse, 'ai');

    // Clear user input
    document.getElementById("userInput").value = "";
}

// Function to append message to conversation
function appendMessage(message, sender) {
    var messagesDiv = document.getElementById("messages");
    var messageDiv = document.createElement("div");
    messageDiv.classList.add("message");
    messageDiv.classList.add(sender);
    messageDiv.innerHTML = message;
    messagesDiv.appendChild(messageDiv);
}

// Function to send message to Flask server and get OpenAI response
function sendMessage(message) {
    var xhr = new XMLHttpRequest();
    xhr.open('POST', 'lang.py', true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            appendMessage(response.message, 'bot'); // Assuming the response contains a 'message' field
        }
    };
    xhr.send(JSON.stringify({ message: message }));
}

// Function to speak text using TTS
function speakText() {
    var textToSpeak = document.getElementById("textToSpeak").value;
    var utterance = new SpeechSynthesisUtterance(textToSpeak);
    window.speechSynthesis.speak(utterance);
}
