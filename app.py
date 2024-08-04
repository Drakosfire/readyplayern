import gradio as gr
import time
import apicall
from apicall import SearchResult


sysprompt = "Hi! Tell me what kind of Hidden Gem you'd like to find."
with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="tuples")
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = apicall.search(message)
        print(f"Bot Message = {bot_message}")
        print(f"Bot Message 0 = {bot_message[0]}")
        print(f"Bot Message 1 = {bot_message[1]}")
        thumbnail = gr.Image(bot_message[0])
        video = gr.Video(bot_message[1])
        text = bot_message[2]
        chat_history.append([(message,text)])
        chat_history.append([ (thumbnail, video)])
        time.sleep(2)
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    demo.launch()