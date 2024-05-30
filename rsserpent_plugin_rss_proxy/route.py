from typing import Any, Dict

import feedparser
from rsserpent_rev.utils import cached


path = "/proxy/{url:path}"


@cached
async def provider(url: str) -> Dict[str, Any]:
    """Return the latest news from the given RSS feed."""
    feed = feedparser.parse(url)

    items = [
        {
            "title": x.title,
            "description": x.summary,
            "link": x.link,
            "pub_date": x.published,
        }
        for x in feed.entries
    ]
    return {
        "title": feed.feed.title,
        "link": feed.feed.link,
        "description": feed.feed.description,
        "items": items,
    }
