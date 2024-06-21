from typing import Any

import feedparser
from feedparser_to_feedgen import to_feedgen  # type: ignore[import-not-found]
from rsserpent_rev.models import Feed
from rsserpent_rev.utils import cached

path = "/proxy/{url:path}"


@cached
async def provider(url: str) -> Feed:
    """Return the latest news from the given RSS feed."""
    feed = feedparser.parse(url)
    return to_feedgen(feed)
