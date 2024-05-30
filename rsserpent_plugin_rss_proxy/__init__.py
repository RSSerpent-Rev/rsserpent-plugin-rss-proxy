from rsserpent_rev.models import Persona, Plugin

from . import route


plugin = Plugin(
    name="rsserpent-plugin-rss-proxy",
    author=Persona(
        name="EkkoG",
        link="https://github.com/EkkoG",
        email="beijiu572@gmail.com",
    ),
    prefix="/proxy",
    repository="https://github.com/EkkoG/rsserpent-plugin-rss-proxy",
    routers={route.path: route.provider},
)
