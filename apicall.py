from twelvelabs import TwelveLabs
import os

client = TwelveLabs(api_key=os.getenv('TL_API_KEY'))

def chatbot_response(message):
    search_results = client.search.query(
    index_id="66ae77216222fe7b53fd787c",
    query_text=message,
    options=[]
    )



    return client.chatbot.get_response(message)
