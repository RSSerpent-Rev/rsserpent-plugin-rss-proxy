from starlette.testclient import TestClient


def test_route(client: TestClient) -> None:
    """Test `rsserpent_plugin_rss_proxy.route`."""
    response = client.get("/proxy/https://developer.apple.com/news/rss/news.rss")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/atom+xml"
    assert response.text.count("Latest News - Apple Developer") == 1
