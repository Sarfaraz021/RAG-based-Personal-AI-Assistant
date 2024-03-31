// frontend/src/pages/a-i-v-a-c-hatbot-u-i-blank.js
import React, { useRef, useState } from 'react';
import axios from 'axios';
import FrameComponent1 from "../components/frame-component1";
import FrameComponent from "../components/frame-component";
import styles from "./a-i-v-a-c-hatbot-u-i-blank.module.css";

const AIVACHatbotUIBlank = () => {
  const fileInputRef = useRef(null);
  const [message, setMessage] = useState("");
  const [uploading, setUploading] = useState(false);
  const [messages, setMessages] = useState([]);

  const handleUploadClick = () => {
    fileInputRef.current.click();
  };

  const handleFileUpload = async (files) => {
    const formData = new FormData();
    formData.append('file', files[0]); // Assuming single file upload

    try {
      setUploading(true); // Indicate the start of the upload process
      const response = await axios.post(
        'http://localhost:8000/finetune/finetune', // Replace with your FastAPI backend endpoint
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        },
      );
      console.log(response.data); // Handle the response from the backend
      alert('File uploaded successfully.');
    } catch (error) {
      console.error(error); // Handle error here
      alert('Error uploading file.');
    } finally {
      setUploading(false); // Reset the uploading status
    }
  };

  const handleFileChange = (event) => {
    handleFileUpload(event.target.files);
  };



  const handleMessageChange = (event) => {
    setMessage(event.target.value);
  };

  const handleSendMessage = async () => {
    // Add the user's message to the messages state
    const newUserMessage = { sender: 'You', text: message };
    setMessages(prevMessages => [...prevMessages, newUserMessage]);
  
    try {
      // Send the user's message to your backend
      const response = await axios.post('http://localhost:8000/chat/chat', { query: message });
  
      // Add the AI Assistant's response to the messages state
      const newAIMessage = { sender: 'AI Assistant', text: response.data.response };
      setMessages(prevMessages => [...prevMessages, newAIMessage]); // This should add the AI's response correctly
    } catch (error) {
      console.error(error);
      // In case of an error, add an error message to the messages state
      setMessages(prevMessages => [...prevMessages, { sender: 'AI Assistant', text: 'Error getting a response.' }]);
    }
  
    // Clear the message input after sending
    setMessage("");
  };

  return (
    <div className={styles.aivaChatbotUiBlank}>
      <FrameComponent1 />
      <main className={styles.frameParent}>
        <FrameComponent />
        <section className={styles.frameWrapper}>
          <div className={styles.frameGroup}>
            <div className={styles.frameContainer}>
              {/* <div className={styles.messagesDisplay}>
                {messages.map((m, index) => (
                  <div key={index} className={styles.messageBubble}>
                    <strong>{m.sender}:</strong> {m.text}
                  </div>
                ))}
              </div> */}
              <div className={styles.messagesDisplay}>
                {messages.map((m, index) => (
                  <div key={index} className={`${styles.messageBubble} ${m.sender === 'You' ? styles.userMessage : styles.assistantMessage}`}>
                    <strong>{m.sender}:</strong> {m.text}
                  </div>
                ))}
              </div>
              <div className={styles.inputParent}>
              <input
                  type="text"
                  value={message}
                  onChange={handleMessageChange}
                  onKeyPress={(event) => {
                    if (event.key === 'Enter') {
                      handleSendMessage();
                    }
                  }}
                  className={styles.input}
                  placeholder="Send a message..."
                />
                <button onClick={handleSendMessage} className={styles.rectangleParent}>
                  <div className={styles.frameChild} />
                  <img
                    className={styles.vectorIcon1}
                    alt=""
                    src="/vector-2.svg"
                  />
                </button>
              </div>
            </div>
            <div className={styles.rectangleGroup}>
              <div className={styles.frameItem} />
              <button onClick={handleUploadClick} className={styles.regenerateResponseButton}>
                <div className={styles.wrapperVector}>
                  <img
                    className={styles.vectorIcon2}
                    alt=""
                    src="/vector-3.svg"
                  />
                </div>
                <div className={styles.uploadDocsHere}>{uploading ? 'Uploading...' : 'Upload Docs here'}</div>
              </button>
              <input
                type="file"
                ref={fileInputRef}
                style={{ display: 'none' }}
                onChange={handleFileChange}
                multiple
              />
              <div className={styles.supportedPdfTxtCsvDocxWrapper}>
                <h2 className={styles.supportedPdfTxtContainer}>
                  <p className={styles.supported}>
                    <b>{`Supported: `}</b>
                  </p>
                  <p className={styles.blankLine}>&nbsp;</p>
                  <p className={styles.pdfTxtCsv}>pdf, txt, csv, docx, xlsx</p>
                </h2>
              </div>
            </div>
          </div>
        </section>
      </main>
    </div>
  );
};

export default AIVACHatbotUIBlank;