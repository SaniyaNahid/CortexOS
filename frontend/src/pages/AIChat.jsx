import { useState } from "react";

import DashboardLayout from "../components/layout/DashboardLayout";
import "../styles/AIChat.css";


function AIChat() {

  const [message, setMessage] = useState("");

  const [chat, setChat] = useState([
    {
      type: "bot",
      text: "Hello! I am CortexOS AI Assistant. How can I help you?"
    }
  ]);


  const sendMessage = () => {

    if(message.trim() === "")
      return;


    setChat([
      ...chat,
      {
        type:"user",
        text:message
      },
      {
        type:"bot",
        text:"I received your query. AI response will be connected with backend soon."
      }
    ]);


    setMessage("");

  };


  return (
    <DashboardLayout>

      <h1>
        AI Assistant
      </h1>

      <p>
        Ask questions from your enterprise knowledge base.
      </p>


      <div className="chat-container">


        <div className="chat-messages">

          {
            chat.map((msg,index)=>(

              <div 
                key={index}
                className={`message ${
                  msg.type === "user"
                  ? "user-message"
                  : "bot-message"
                }`}
              >

                {msg.text}

              </div>

            ))
          }


        </div>



        <div className="chat-input">


          <input

            type="text"

            placeholder="Ask your question..."

            value={message}

            onChange={(e)=>setMessage(e.target.value)}

            onKeyDown={(e)=>{

              if(e.key==="Enter")
                sendMessage();

            }}

          />


          <button onClick={sendMessage}>
            Send
          </button>


        </div>


      </div>


    </DashboardLayout>
  );
}


export default AIChat;