import gradio as gr
import time
import twelvelabs


sysprompt = "Hi! Tell me what kind of Hidden Gem you'd like to find."
with gr.Blocks() as app:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = twelvelabs.chatbot_response(message)
        chat_history.append((message, bot_message))
        time.sleep(2)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    app.launch()