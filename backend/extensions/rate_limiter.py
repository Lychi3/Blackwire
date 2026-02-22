"""
Rate Limiter extension
Añade delays entre requests para evitar rate limiting
"""

EXTENSION_META = {
    "name": "rate_limiter",
    "title": "Rate Limiter",
    "description": "Añade delays entre requests para evitar rate limiting",
    "tabs": [],
    "ui_schema": {
        "type": "schema-driven",
        "fields": [
            {
                "name": "delay_ms",
                "label": "Delay (milliseconds)",
                "type": "number",
                "placeholder": "500",
                "default": 500,
                "min": 0,
                "max": 10000,
                "help": "Delay between each request in milliseconds"
            },
            {
                "name": "apply_to",
                "label": "Apply To",
                "type": "select",
                "options": [
                    {"value": "all", "label": "All Requests"},
                    {"value": "specific_host", "label": "Specific Host Only"}
                ],
                "default": "all"
            },
            {
                "name": "target_host",
                "label": "Target Host",
                "type": "text",
                "placeholder": "example.com",
                "default": "",
                "help": "Only used when 'Specific Host Only' is selected"
            }
        ]
    },
    "default_config": {
        "enabled": False,
        "delay_ms": 500,
        "apply_to": "all",
        "target_host": ""
    }
}

import time
from mitmproxy import http


class RateLimiterExtension:
    name = "rate_limiter"

    def on_request(self, flow: http.HTTPFlow, cfg: dict, full_config: dict):
        if not cfg.get("enabled", False):
            return

        delay_ms = cfg.get("delay_ms", 500)
        apply_to = cfg.get("apply_to", "all")
        target_host = cfg.get("target_host", "")

        should_delay = apply_to == "all" or (
            apply_to == "specific_host" and target_host in flow.request.pretty_host
        )

        if should_delay and delay_ms > 0:
            time.sleep(delay_ms / 1000.0)


def register():
    return RateLimiterExtension()
