"""
Headers Injector extension
Inyecta headers personalizados en todas las peticiones con UI dinámica
"""

EXTENSION_META = {
    "name": "headers_injector",
    "title": "Headers Injector",
    "description": "Inyecta múltiples headers personalizados en requests con UI avanzada",
    "tabs": [{"id": "main", "label": "📋 Headers Injector"}],
    "default_config": {
        "enabled": False,
        "headers": []  # Lista de {name: str, value: str, enabled: bool}
    }
}

from mitmproxy import http


class HeadersInjectorExtension:
    name = "headers_injector"

    def on_request(self, flow: http.HTTPFlow, cfg: dict, full_config: dict):
        if not cfg.get("enabled", False):
            return

        headers = cfg.get("headers", [])

        # Inyectar cada header habilitado
        for header in headers:
            if header.get("enabled", True) and header.get("name") and header.get("value"):
                flow.request.headers[header["name"]] = header["value"]


def register():
    return HeadersInjectorExtension()
