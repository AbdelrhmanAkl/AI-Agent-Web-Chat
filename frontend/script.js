const API_URL = "http://127.0.0.1:8000";

let conversationId = crypto.randomUUID();

const chatForm = document.getElementById("chatForm");
const messageInput = document.getElementById("messageInput");
const chatMessages = document.getElementById("chatMessages");
const sendBtn = document.getElementById("sendBtn");
const typing = document.getElementById("typing");
const newChatBtn = document.getElementById("newChatBtn");


function addMessage(message, sender) {

    const messageDiv = document.createElement("div");
    messageDiv.className = `message ${sender}`;

    const nameDiv = document.createElement("div");
    nameDiv.className = "message-name";
    nameDiv.textContent = sender === "user"
        ? "You"
        : "AI Assistant";

    const textDiv = document.createElement("div");
    textDiv.className = "message-text";
    textDiv.textContent = message;

    messageDiv.appendChild(nameDiv);
    messageDiv.appendChild(textDiv);

    chatMessages.appendChild(messageDiv);

    chatMessages.scrollTop = chatMessages.scrollHeight;
}


function setLoading(isLoading) {

    if (isLoading) {
        typing.classList.remove("hidden");
        sendBtn.disabled = true;
        messageInput.disabled = true;
    } else {
        typing.classList.add("hidden");
        sendBtn.disabled = false;
        messageInput.disabled = false;
        messageInput.focus();
    }
}


chatForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const message = messageInput.value.trim();

    if (!message) {
        return;
    }

    addMessage(message, "user");

    messageInput.value = "";

    setLoading(true);

    try {

        const response = await fetch(`${API_URL}/chat`, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message,
                conversation_id: conversationId
            })
        });


        const data = await response.json();


        if (!response.ok) {
            throw new Error(data.detail || "Something went wrong.");
        }


        addMessage(data.response, "assistant");


    } catch (error) {

        addMessage(
            `Error: ${error.message}`,
            "assistant"
        );

    } finally {

        setLoading(false);
    }
});


newChatBtn.addEventListener("click", async function () {

    try {

        await fetch(
            `${API_URL}/chat/${conversationId}`,
            {
                method: "DELETE"
            }
        );

    } catch (error) {

        console.error(
            "Failed to clear conversation:",
            error
        );
    }


    conversationId = crypto.randomUUID();

    chatMessages.innerHTML = `
        <div class="message assistant">
            <div class="message-name">AI Assistant</div>
            <div class="message-text">
                Hello! I'm your AI assistant. How can I help you today?
            </div>
        </div>
    `;

    messageInput.focus();
});


messageInput.addEventListener("keydown", function (event) {

    if (event.key === "Enter" && !event.shiftKey) {

        event.preventDefault();

        chatForm.requestSubmit();
    }
});