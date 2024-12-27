const chatBox = document.getElementById('chatBox');
const userInput = document.getElementById('userInput');
const sendBtn = document.getElementById('sendBtn');

sendBtn.addEventListener('click', () => {
  const userMessage = userInput.value.trim();
  if (userMessage) {
    addMessage(userMessage, 'user');
    fetchBotResponse(userMessage);
    userInput.value = '';
  }
});

function addMessage(message, sender) {
  const messageDiv = document.createElement('div');
  messageDiv.classList.add('message', sender);
  const messageSpan = document.createElement('span');
  messageSpan.textContent = message;
  messageDiv.appendChild(messageSpan);
  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function fetchBotResponse(userMessage) {
  fetch(`http://127.0.0.1:5000/chat?q=${encodeURIComponent(userMessage)}`)
    .then(response => response.json())
    .then(data => {
      addMessage(data.response, 'bot');
    })
    .catch(() => {
      addMessage('Maaf, terjadi kesalahan.', 'bot');
    });
}
