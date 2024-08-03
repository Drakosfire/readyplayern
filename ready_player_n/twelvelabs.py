import os

from twelvelabs import TwelveLabs

from ready_player_n.trail_metadata import TrailMetadata


class SearchResult:
    def __init__(self, item, youtube_link, trail):
        self.thumbnail_url = f"{item.thumbnail_url}&t={item.start}s"
        self.youtube_link = f"{youtube_link}&t={item.start}s"
        self.metadata = item.metadata
        self.trail = trail

    def __repr__(self):
        return f"SearchResult(thumbnail_url={self.thumbnail_url}, youtube_link={self.youtube_link}, metadata={self.metadata}, trail={self.trail})"


def search(
    query,
    index_id="66ae77216222fe7b53fd787c",
    options=["visual", "conversation", "text_in_video"],
    youtube_link="https://www.youtube.com/watch?v=KKeZPA-Gvs4",
    n=3,
):
    trail_metadata = TrailMetadata()

    client = TwelveLabs(api_key=os.getenv("TL_API_KEY"))
    result = client.search.query(
        index_id=index_id,
        query=query,
        options=options,
        page_limit=n,
    )

    results = []
    for item in result.data:
        youtube_link = f"{youtube_link}&t={item.start}s"
        trail = trail_metadata.get_trail_by_timestamp(item.start)

        result = SearchResult(item, youtube_link, trail)
        results.append(result)

    return results
