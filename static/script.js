function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    if (userInput.trim() === '') return;

    const chatBox = document.getElementById("chat-box");
    const userMessage = document.createElement("div");
    userMessage.classList.add("chat-message", "user");

    const userIcon = document.createElement("img");
    userIcon.src = "https://cdn-icons-png.flaticon.com/512/2922/2922561.png"; // User icon URL
    userIcon.alt = "User Icon";
    userIcon.classList.add("icon");

    const userText = document.createElement("div");
    userText.classList.add("message", "user");
    userText.textContent = userInput;

    userMessage.appendChild(userText);
    userMessage.appendChild(userIcon);
    chatBox.appendChild(userMessage);

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    })
    .then(response => response.json())
    .then(data => {
        const botMessage = document.createElement("div");
        botMessage.classList.add("chat-message", "bot");

        const botIcon = document.createElement("img");
        botIcon.src = "https://cdn-icons-png.flaticon.com/512/4712/4712100.png";
        botIcon.alt = "ChatBot Icon";
        botIcon.classList.add("icon");

        const botText = document.createElement("div");
        botText.classList.add("message", "bot");
        botText.textContent = data.response;

        botMessage.appendChild(botIcon);
        botMessage.appendChild(botText);
        chatBox.appendChild(botMessage);

        chatBox.scrollTop = chatBox.scrollHeight;
    });

    document.getElementById("user-input").value = '';
}

document.getElementById("user-input").addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        sendMessage();
    }
});
