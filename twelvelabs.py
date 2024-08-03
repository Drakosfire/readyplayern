from twelvelabs import TwelveLabs

client = TwelveLabs(api_key=os.getenv('TL_API_KEY'))

def chatbot_response(message):
    search_results = client.search.query(
    index_id="<YOUR_INDEX_ID>",
    query_text="<YOUR_QUERY>",
    options=["<YOUR_SEARCH_OPTIONS>"]
    )

# Utility function to print a specific page
def print_page(page):
    for clip in page:
        print(
            f" video_id={clip.video_id} score={clip.score} start={clip.start} end={clip.end} confidence={clip.confidence}"
        )

    print_page(search_results.data)

    while True:
        try:
            print_page(next(search_results))
        except StopIteration:
            break

    return client.chatbot.get_response(message)
