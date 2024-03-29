// Function to send a chat message
function sendChat() {
    const chatInput = document.getElementById('chat-input');
    const message = chatInput.value.trim();
  
    // Ensure there's a message before sending
    if (message) {
      displayUserMessage(message);
      chatInput.value = ''; // Clear the input field
  
      // Send the message to your API endpoint
      fetch('http://127.0.0.1:8000/chat/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: message })
      })
      .then(response => response.json())
      .then(data => {
        displayAIMessage(data.response);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    }
  }
  
  // Function to display user message in the chat window
  function displayUserMessage(message) {
    const chatWindow = document.getElementById('chat-window');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('chat-message', 'user-message');
    messageDiv.innerHTML = `<div class="message-content user">${message}</div>`;
    chatWindow.appendChild(messageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight; // Scroll to the bottom
  }
  
  // Function to display AI message in the chat window
  function displayAIMessage(message) {
    const chatWindow = document.getElementById('chat-window');
    const messageDiv = document.createElement('div');
    messageDiv.classList.add('chat-message', 'ai-message');
    messageDiv.innerHTML = `<div class="message-content ai">${message}</div>`;
    chatWindow.appendChild(messageDiv);
    chatWindow.scrollTop = chatWindow.scrollHeight; // Scroll to the bottom
  }
  
  // Function to handle fine-tuning with uploaded file
  function fineTuneAI() {
    const fileInput = document.getElementById('fine-tune-file');
    const file = fileInput.files[0];
  
    if (file) {
      const formData = new FormData();
      formData.append('file', file);
      formData.append('file_type', file.name.split('.').pop());
  
      // Send the file to your API endpoint
      fetch('http://127.0.0.1:8000/finetune/finetune', {
        method: 'POST',
        body: formData
      })
      .then(response => response.json())
      .then(data => {
        alert(data.message);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
    } else {
      alert('Please select a file to fine-tune the AI.');
    }
  }
  
  // Listens for changes on the file input to update the label dynamically
  document.querySelector('.custom-file-input').addEventListener('change',function(e){
    var fileName = document.getElementById("fine-tune-file").files[0].name;
    var nextSibling = e.target.nextElementSibling
    nextSibling.innerText = fileName
  });
  