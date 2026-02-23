"""
Webhook.site integration extension (UI-only).
Stores config for token/Api-Key, and lets backend endpoints manage history.
"""

EXTENSION_META = {
    "name": "webhook_site",
    "title": "Webhook.site",
    "description": "Genera una URL de Webhook.site y guarda el historial localmente.",
    "tabs": [
        {"id": "main", "label": "🔗 Webhook.site"}
    ],
    "default_config": {
        "enabled": False,
        "token_id": None,
        "token_url": None,
        "api_key": None
    }
}


class WebhookSiteExtension:
    name = "webhook_site"

    def on_load(self, cfg: dict, full_config: dict):
        return


def register():
    return WebhookSiteExtension()
