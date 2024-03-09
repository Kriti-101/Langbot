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

// Function to speak text using TTS
function speakText() {
    var textToSpeak = document.getElementById("textToSpeak").value;
    var utterance = new SpeechSynthesisUtterance(textToSpeak);
    window.speechSynthesis.speak(utterance);
}
