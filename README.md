# BlackWire

![Preview del proyecto](Blackwire_banner.png)

<h3 align="center">Security from México to all</h3>

![Estado](https://img.shields.io/badge/status-En_desarrollo-green)
![License](https://img.shields.io/badge/license-GNU_AGPLv3-blue)

---

## Descripción

**BlackWire** es un proxy interceptor HTTP/HTTPS de código abierto diseñado para pruebas de seguridad, análisis de tráfico web y debugging de aplicaciones. Ofrece una alternativa ligera, portable y extensible a herramientas como Burp Suite o OWASP ZAP, con un frontend web moderno y un potente backend basado en mitmproxy. Permite interceptar, modificar y reenviar peticiones en tiempo real, gestionar múltiples proyectos, y extender funcionalidades mediante plugins personalizados.

---

## Características

### Core
- **Proxy Interceptor**: Captura y modifica peticiones/respuestas HTTP/HTTPS en tiempo real con soporte para forward, drop y edición completa
- **Gestión de Proyectos**: Organiza sesiones de trabajo con proyectos independientes, cada uno con su propia base de datos SQLite
- **Repeater**: Reenvía y modifica peticiones capturadas con soporte para redirect automático/manual, historial de navegación y auto-guardado
- **Scope/Filtros**: Define reglas include/exclude con regex y wildcards para interceptar solo tráfico relevante

### Análisis
- **HTTPQL**: Lenguaje de consulta inspirado en Caido para filtrar requests con operadores avanzados (eq, cont, like, regex, gt, lt, etc.) sobre campos de request y response
- **Filter Presets**: Guarda y aplica filtros HTTPQL frecuentes desde un dropdown con CRUD completo
- **Compare**: Compara dos requests/responses lado a lado con highlighting de diferencias usando algoritmo LCS (diff)
- **Site Map**: Vista en árbol jerárquico de todos los hosts y endpoints capturados, agrupados por host → path segments
- **WebSocket Viewer**: Captura y visualiza conexiones WebSocket con sus frames en ambas direcciones, con soporte para reenviar mensajes

### Herramientas
- **Cipher**: Encoder/decoder visual con recetas encadenables — Base64, URL encoding, hashes criptográficos, gzip, hex, y 100+ operaciones
- **JWT Analyzer**: Decodifica y analiza tokens JWT con documentación de ataques comunes (None algorithm, Key confusion, Weak secrets)
- **Sensitive Discovery**: Escaneo automático de secrets en responses con 50+ patrones (API keys, tokens, passwords) y filtro Shannon Entropy
- **Collections**: Agrupa requests en secuencias ejecutables con extracción de variables y sustitución automática para workflows de testing
- **Session Rules & Macros**: Automatiza extracción de tokens/cookies y reinyección en requests subsecuentes para mantener sesiones activas
- **Git Integration**: Control de versiones integrado para commits y revisión de historial del proyecto

### Extensibilidad
- **Sistema de Extensiones Dinámicas**: Crea plugins en Python con UI generada automáticamente mediante schemas JSON
- **Schema-Driven UI**: Define formularios de configuración sin escribir React — solo metadata en Python
- **Tabs Dinámicas**: Las extensiones pueden crear pestañas propias en la UI automáticamente
- **Acceso Total al Proxy**: Manipula requests/responses en tiempo real con hooks de mitmproxy

### Operación
- **100% Portable**: Sin rutas hardcoded, funciona desde cualquier directorio
- **Import/Export**: Exporta proyectos completos (requests, repeater, collections, scope) en formato JSON para compartir con colegas
- **Burp Suite Integration**: Importa/exporta HTTP history en formato XML compatible con Burp Suite Pro
- **Desktop Launcher**: Integración con menú de aplicaciones sin terminal visible
- **Shutdown**: Botón ⏻ en la UI, script `stop.sh`, o endpoint API para apagar el server
- **Cross-Platform**: Compatible con cualquier distribución Linux
- **15 Temas**: Midnight, Dusk, Paper, Gruvbox, Solarized, Aurora, Noir, Glacier, Ember, Forest, Oceanic, Rose, Mono, Desert, Synth

---

## Instalación

### Instalación Rápida

```bash
# 1. Descarga el proyecto
git clone https://github.com/Glitchboi-sudo/Blackwire.git
cd Blackwire

# 2. Ejecuta el instalador
chmod +x install.sh
./install.sh

# 3. Lanza la aplicación
./launch-with-browser.sh
```

¡Eso es todo! El instalador se encarga de todo automáticamente.

---

### Requisitos

#### Dependencias del Sistema
```bash
# Ubuntu/Debian
sudo apt install python3 python3-pip python3-venv nodejs npm

# Fedora/RHEL/CentOS
sudo dnf install python3 python3-pip nodejs npm

# Arch Linux
sudo pacman -S python python-pip nodejs npm
```

> **Node.js** es necesario para la pre-transpilación de JSX con sucrase. Si no está disponible, la app funciona igual pero carga más lento (usa Babel en el browser como fallback).

---

### Métodos de Instalación

#### Método 1: Instalador Automático (Recomendado)

El script `install.sh` realiza todas las configuraciones necesarias:

```bash
chmod +x install.sh
./install.sh
```

**Qué hace el instalador:**
1. Verifica versión de Python (3.8+)
2. Verifica/instala pip
3. Crea entorno virtual
4. Instala dependencias desde requirements.txt
5. Crea directorios necesarios
6. Genera certificados SSL de mitmproxy
7. Hace ejecutables todos los scripts
8. Opcionalmente instala launcher en el menú

#### Método 2: Instalación Manual

Si prefieres control total sobre la instalación:

```bash
# 1. Crear entorno virtual
python3 -m venv venv

# 2. Activar entorno
source venv/bin/activate

# 3. Actualizar pip
pip install --upgrade pip

# 4. Instalar dependencias
pip install -r requirements.txt

# 5. Instalar sucrase para transpilación JSX (opcional pero recomendado)
npm install --save-dev sucrase

# 6. Crear directorios
mkdir -p projects

# 7. Hacer scripts ejecutables
chmod +x *.sh

# 8. Iniciar
./launch-with-browser.sh
```

---

### Desktop Launcher

#### Instalar Launcher en el Menú

```bash
./install-desktop.sh
```

Después de instalarlo, puedes:
- Buscar "Blackwire" en el menú de aplicaciones
- Fijarlo al dock/panel
- Asignarle un atajo de teclado

El launcher inicia el server en background y abre el navegador automáticamente. No se queda ninguna terminal abierta.

#### Desinstalar Launcher

```bash
./uninstall-desktop.sh
```

---

### Certificados SSL

BlackWire usa **mitmproxy** para interceptar tráfico HTTPS. Necesitas instalar el certificado CA:

#### Ubicación del Certificado

```bash
~/.mitmproxy/mitmproxy-ca-cert.pem
```

#### Instalar en Navegador

**Firefox:**
1. Preferencias → Privacidad y Seguridad → Certificados → Ver Certificados
2. Autoridades → Importar
3. Selecciona: `~/.mitmproxy/mitmproxy-ca-cert.pem`
4. Confía para: "Identificar sitios web"

**Chrome/Chromium:**
1. Configuración → Privacidad y Seguridad → Seguridad → Gestionar certificados
2. Autoridades → Importar
3. Selecciona: `~/.mitmproxy/mitmproxy-ca-cert.pem`

**Sistema (Linux):**
```bash
# Ubuntu/Debian
sudo cp ~/.mitmproxy/mitmproxy-ca-cert.pem /usr/local/share/ca-certificates/mitmproxy.crt
sudo update-ca-certificates

# Fedora/RHEL
sudo cp ~/.mitmproxy/mitmproxy-ca-cert.pem /etc/pki/ca-trust/source/anchors/
sudo update-ca-trust
```

---

## Uso

### Inicio y Parada

```bash
# Iniciar (abre navegador automáticamente)
./launch-with-browser.sh

# Iniciar sin navegador
./start.sh

# Parar el server
./stop.sh
```

También puedes apagar desde la interfaz web con el botón ⏻ en la esquina superior derecha, o vía API:
```bash
curl -X POST http://localhost:5000/api/shutdown
```

Una vez iniciado:
- **Frontend**: http://localhost:5000
- **API Docs**: http://localhost:5000/docs
- **Proxy**: http://localhost:8080 (configura este proxy en tu navegador/herramienta)

---

### Proxy Interceptor

1. **Iniciar Proxy**: Botón "▶ Start" en la interfaz
2. **Configurar Navegador**: Proxy HTTP en `localhost:8080`
3. **Habilitar Intercept**: Activa el interceptor para pausar peticiones
4. **Modificar Peticiones**: Edita headers, body, método, URL
5. **Forward/Drop**: Envía o descarta la petición modificada

Soporta modos: regular, upstream, socks5, reverse, transparent.

---

### Repeater

Reenvía peticiones capturadas para pruebas iterativas:

1. Click derecho en una petición → "Send to Repeater" (o botón "→ Rep")
2. Modifica método, URL, headers o body
3. Click "Send" para enviar
4. Inspecciona headers y body de la respuesta
5. Pretty Print / Minify para formatear

**Características:**
- Historial de navegación por request (atrás/adelante)
- Auto-guardado de requests
- Modo redirect: No Redirect (manual) o Auto Follow
- Visualización de redirect chain completa
- Colorización de sintaxis en body (JSON, HTML, XML)

---

### HTTPQL - Filtrado Avanzado

El campo de búsqueda en History soporta HTTPQL, un lenguaje de consulta para filtrar requests:

```
# Filtrar por método
req.method eq GET

# Filtrar por host
req.host cont example.com

# Filtrar por status code
resp.code gte 400

# Combinar con operadores lógicos
req.method eq POST AND resp.code eq 200

# Usar regex
req.path regex /api/v[0-9]+/users

# Negar
NOT req.host cont google.com

# Agrupar
(req.method eq POST OR req.method eq PUT) AND resp.code lt 300
```

**Campos disponibles:**
- Request: `method`, `host`, `path`, `port`, `ext`, `query`, `raw`, `len`, `tls`
- Response: `code`, `raw`, `len`

**Operadores:**
- String: `eq`, `ne`, `cont`, `ncont`, `like`, `nlike`, `regex`, `nregex`
- Numéricos: `eq`, `ne`, `gt`, `gte`, `lt`, `lte`

**Filter Presets**: Guarda queries frecuentes con nombre para acceso rápido desde el dropdown.

---

### Compare

Compara dos requests o responses lado a lado con diff visual:

1. Click derecho en un request → "Compare (A)" para establecer el lado izquierdo
2. Click derecho en otro → "Compare (B)" para el lado derecho
3. Ve a la pestaña Compare
4. Alterna entre vista de Request y Response
5. Las diferencias se resaltan: verde = añadido, rojo = eliminado

---

### Site Map

Vista en árbol de todos los hosts y endpoints capturados:

1. Ve a History → sub-tab "Site Map"
2. El panel izquierdo muestra el árbol: Host → /path → /subpath
3. Click en un nodo para ver sus requests
4. Click en un request para ver su detalle completo

Los nodos muestran badges con el conteo de requests y los métodos HTTP vistos (GET, POST, etc.).

---

### Cipher

Encoder/decoder con recetas encadenables:

1. Ingresa datos en el panel de input
2. Busca y agrega operaciones desde la lista (Base64, URL encode, SHA256, etc.)
3. Las operaciones se encadenan: la salida de una es la entrada de la siguiente
4. El resultado aparece en el panel de output
5. Configura parámetros por operación cuando aplique

**Categorías de operaciones:**
- Encoding: Base64, URL, Hex, HTML entities
- Hashing: MD5, SHA1, SHA256, SHA512, HMAC
- Compression: Gzip compress/decompress
- Encryption: AES, DES, 3DES, Blowfish, RC4, ChaCha20, XOR
- Conversión: Decimal, Octal, Binary, Morse, ROT13
- String: Reverse, Upper/Lower, Count, Length, Split, Replace
- Y más...

---

### Collections

Agrupa requests en secuencias ejecutables con variables:

1. Crea una colección con nombre
2. Agrega requests desde el context menu → "Add to Collection"
3. Configura extractores de variables (extraer tokens, IDs, etc. de responses)
4. Ejecuta la secuencia — las variables se sustituyen automáticamente
5. Revisa resultados de cada paso

Ideal para testing de flujos multi-paso como login → obtener token → usar token.

---

### Session Rules & Macros

Automatiza la extracción y reinyección de tokens/cookies para mantener sesiones:

#### Session Rules
1. Ve a Extensions → Session → sub-tab "Rules"
2. Crea una regla con:
   - **When**: Cuándo ejecutar (After Request, After Response, Before Request)
   - **Target**: De dónde extraer (Response Headers, Response Body)
   - **Extract**: Regex para capturar el valor (ej. `"token":"([^"]+)"`)
   - **Variable**: Nombre para guardar el valor extraído
3. La variable se extrae automáticamente cuando coincide el patrón

#### Session Macros
1. Crea un macro con la petición que obtiene el token (ej. POST /login)
2. Ejecuta el macro manualmente o desde reglas
3. El macro envía la request y extrae variables según las reglas definidas

**Uso común**: Extraer token de `/auth/login` y reinyectarlo automáticamente en el header `Authorization` de requests subsecuentes.

---

### JWT Analyzer

Analiza y ataca tokens JWT:

1. Ve a la pestaña Cipher → sub-tab "JWT"
2. Pega un token JWT en el campo de input
3. Visualiza header, payload y signature decodificados
4. Revisa la documentación de ataques comunes:
   - **None Algorithm Attack**: Eliminar signature y cambiar alg a "none"
   - **Key Confusion**: Confundir RS256 con HS256 usando clave pública como secret
   - **Weak Secret**: Bruteforce de secrets débiles con herramientas como hashcat

El analyzer resalta automáticamente tokens con algoritmos inseguros.

---

### Sensitive Discovery

Escanea responses en busca de secrets y credenciales:

1. Ve a Extensions → sub-tab "Sensitive"
2. Click "Scan All Requests" para escanear el historial completo
3. Ajusta el umbral de Shannon Entropy para reducir falsos positivos
4. Revisa los hallazgos por categoría:
   - AWS Keys, API Tokens, Private Keys, Database URLs
   - Passwords, JWT tokens, OAuth secrets
   - Cloud credentials (Azure, GCP, DigitalOcean)
   - Webhooks (Slack, Discord, Teams)
5. Click en un hallazgo para ver el request completo

**Filtro de Entropía**: Shannon Entropy mide la aleatoriedad de strings. Ajustar el threshold (default: 3.5) filtra falsos positivos eliminando strings con baja entropía.

---

### Import/Export de Proyectos

Comparte proyectos completos con colegas:

#### Exportar Proyecto
1. Ve a la pestaña Projects
2. Click en "↑ ▼" junto al proyecto
3. Selecciona formato:
   - **↑ Blackwire Format**: JSON con todos los datos (requests, repeater, collections, filter presets, session rules, scope)
   - **↑ Burp Suite XML**: Formato XML compatible con Burp Suite Pro (solo HTTP history)
4. Descarga el archivo

#### Importar Proyecto
1. Click en "↓ ▼" junto al proyecto destino
2. Selecciona modo:
   - **↓ Merge Data**: Combina datos del archivo con el proyecto existente
   - **🔄 Replace All**: Elimina datos existentes y reemplaza con el archivo
   - **↓ Burp Suite XML**: Importa HTTP history desde archivo XML de Burp Suite Pro
3. Selecciona el archivo y confirma

**Crear Proyecto Nuevo desde Export**:
1. Click en "↓ New Project"
2. Selecciona archivo de export en formato Blackwire
3. El proyecto se crea con todos sus datos

---

### Burp Suite Integration

Intercambia datos con Burp Suite Pro:

#### Exportar a Burp Suite
1. Exporta proyecto en formato "↑ Burp Suite XML"
2. Abre Burp Suite Pro
3. Proxy → HTTP History → Import → Selecciona el XML
4. Todo el historial HTTP aparece en Burp

#### Importar desde Burp Suite
1. En Burp Suite: Proxy → HTTP History → Selecciona requests → Save Items
2. Guarda como XML
3. En Blackwire: Click "↓ Burp Suite XML" → Selecciona el archivo
4. Las requests se importan al proyecto actual

**Nota**: El formato XML preserva método, URL, headers, body, status code, response headers/body y timestamps.

---

### WebSocket Viewer

Captura y visualiza tráfico WebSocket:

1. Ve a History → sub-tab "WS"
2. Panel izquierdo: lista de conexiones WebSocket por URL
3. Panel central: frames de la conexión seleccionada (↑ enviado, ↓ recibido)
4. Panel derecho: detalle del frame seleccionado
5. Reenvía frames editados con el campo de input

---

### Webhook.site

Captura webhooks entrantes:

1. Ve a la pestaña Webhook
2. Genera un token para obtener una URL única de webhook.site
3. Usa esa URL como callback en tus pruebas
4. Los requests entrantes aparecen automáticamente en la lista
5. Inspecciona headers, body y metadata de cada webhook

---

### Temas

BlackWire incluye 15 temas de color:

| Tema | Estilo |
|------|--------|
| Midnight | Oscuro azul (default) |
| Dusk | Oscuro púrpura |
| Paper | Claro cálido |
| Gruvbox | Retro cálido |
| Solarized | Claro precision |
| Aurora | Oscuro azul profundo |
| Noir | Negro puro |
| Glacier | Oscuro azul hielo |
| Ember | Oscuro rojo cálido |
| Forest | Oscuro verde |
| Oceanic | Oscuro azul océano |
| Rose | Oscuro rosa |
| Mono | Oscuro desaturado |
| Desert | Oscuro arena |
| Synth | Oscuro neón púrpura |

Selecciona el tema desde el dropdown en la esquina superior derecha. La preferencia se guarda en localStorage.

---

### Scope

Define reglas para filtrar qué tráfico interceptar:

```
Include: *.example.com/*      (solo example.com)
Exclude: *.google.com/*       (ignora Google)
Include: /api/.*              (solo endpoints de API)
```

**Tipos de reglas:**
- **Include**: Solo intercepta URLs que coincidan
- **Exclude**: Ignora URLs que coincidan
- Soporta regex y wildcards

También puedes agregar hosts al scope directamente desde el context menu sobre cualquier request.

---

### Extensiones

BlackWire cuenta con un **sistema de extensiones dinámicas** que te permite extender funcionalidades sin tocar el frontend. Las extensiones pueden manipular tráfico HTTP, agregar tabs personalizadas en la UI, y configurarse con formularios generados automáticamente.

#### Sistema de Extensiones

**Ubicación:** `backend/extensions/`

**Características:**
- **UI Generada Automáticamente**: Define un schema JSON y el frontend genera formularios de configuración
- **Descubrimiento Automático**: Solo crea el archivo `.py` y la extensión aparece automáticamente
- **Tabs Dinámicas**: Crea pestañas completas en la UI sin modificar código frontend
- **Auto-Inicialización**: Nuevos proyectos incluyen automáticamente todas las extensiones
- **Acceso Total al Proxy**: Manipula requests/responses con el objeto `flow` de mitmproxy

#### Extensiones Incluidas

| Extensión | Descripción | UI |
|-----------|-------------|-----|
| **Match & Replace** | Modifica URLs, headers o body con regex | Custom |
| **Webhook.site** | Integración con webhook.site para capturar webhooks | Custom |
| **Sensitive Discovery** | Escaneo de secrets con patrones y Shannon Entropy | Custom |
| **Rate Limiter** | Añade delays entre requests para evitar rate limiting | Schema-driven |

---

### Tutorial: Crear tu Primera Extensión

#### Extensión Simple (Schema-Driven)

Vamos a crear una extensión que añade un header personalizado a todas las peticiones. **Solo necesitas crear 1 archivo Python**.

**1. Crear archivo `backend/extensions/custom_header.py`:**

```python
"""
Custom Header Injector
Inyecta headers personalizados en requests
"""

EXTENSION_META = {
    "name": "custom_header",
    "title": "Custom Header",
    "description": "Inyecta headers personalizados en todas las peticiones",
    "tabs": [],  # Sin tab propia, solo configuración en Extensions

    # UI generada automáticamente
    "ui_schema": {
        "type": "schema-driven",
        "fields": [
            {
                "name": "header_name",
                "label": "Header Name",
                "type": "text",
                "placeholder": "X-Custom-Header",
                "default": "X-Custom-Header",
                "help": "Nombre del header a inyectar"
            },
            {
                "name": "header_value",
                "label": "Header Value",
                "type": "text",
                "placeholder": "my-value",
                "default": "",
                "help": "Valor del header"
            },
            {
                "name": "overwrite",
                "label": "Overwrite if exists",
                "type": "checkbox",
                "default": False,
                "help": "Sobrescribir si el header ya existe"
            }
        ]
    },

    # Configuración por defecto para nuevos proyectos
    "default_config": {
        "enabled": False,
        "header_name": "X-Custom-Header",
        "header_value": "",
        "overwrite": False
    }
}

from mitmproxy import http

class CustomHeaderExtension:
    name = "custom_header"

    def on_request(self, flow: http.HTTPFlow, cfg: dict, full_config: dict):
        if not cfg.get("enabled", False):
            return

        header_name = cfg.get("header_name", "X-Custom-Header")
        header_value = cfg.get("header_value", "")
        overwrite = cfg.get("overwrite", False)

        # Inyectar header
        if header_value:
            if overwrite or header_name not in flow.request.headers:
                flow.request.headers[header_name] = header_value

def register():
    return CustomHeaderExtension()
```

**2. Reiniciar el servidor:**

```bash
./stop.sh
./start.sh
```

**3. ¡Listo!**

- Ve a la pestaña **Extensions** en la UI
- Verás "Custom Header" con un formulario generado automáticamente
- Habilita la extensión
- Configura el nombre y valor del header
- Todas tus peticiones llevarán ese header

---

#### Tipos de Campo UI Soportados

El sistema `ui_schema` soporta múltiples tipos de inputs:

```python
"fields": [
    # Input de texto
    {
        "name": "api_key",
        "label": "API Key",
        "type": "text",  # o "password" para oscurecer
        "placeholder": "Enter key...",
        "default": "",
        "help": "Tu API key"
    },

    # Input numérico
    {
        "name": "timeout",
        "label": "Timeout (ms)",
        "type": "number",
        "default": 5000,
        "min": 1000,
        "max": 60000,
        "help": "Timeout en milisegundos"
    },

    # Checkbox
    {
        "name": "enabled",
        "label": "Enable logging",
        "type": "checkbox",
        "default": True,
        "help": "Activar logs detallados"
    },

    # Dropdown/Select
    {
        "name": "mode",
        "label": "Operation Mode",
        "type": "select",
        "options": [
            {"value": "auto", "label": "Automatic"},
            {"value": "manual", "label": "Manual"},
            {"value": "disabled", "label": "Disabled"}
        ],
        "default": "auto"
    },

    # Área de texto multilinea
    {
        "name": "payload",
        "label": "Payload Template",
        "type": "textarea",
        "rows": 8,
        "placeholder": "Enter JSON...",
        "default": "{}"
    }
]
```

---

#### Extensión Avanzada (Con Tab Propia)

Para crear una extensión con su propia pestaña en la UI (como Webhook.site):

**1. Definir tab en `EXTENSION_META`:**

```python
EXTENSION_META = {
    "name": "my_tool",
    "title": "My Tool",
    "description": "Una herramienta personalizada",
    "tabs": [
        {"id": "main", "label": "🔧 My Tool"}
    ],
    "ui_schema": {
        "type": "schema-driven",
        "fields": [...]
    },
    "default_config": {"enabled": False}
}
```

**2. Crear componente React custom (solo si necesitas UI compleja):**

Edita `frontend/App.jsx` y agrega:

```javascript
// Después de línea 2437
function MyToolUI({ ext, updateExtCfg }) {
  return (
    <div>
      {/* Tu UI personalizada aquí */}
    </div>
  );
}

// Agregar al registry
const EXTENSION_CUSTOM_COMPONENTS = {
  'match_replace': MatchReplaceUI,
  'webhook_site': WebhookSiteUI,
  'my_tool': MyToolUI,  // NUEVO
};
```

**3. Recompilar frontend:**

```bash
cd frontend && mkdir -p /tmp/bw_src && cp App.jsx /tmp/bw_src/ && \
npx sucrase /tmp/bw_src -d /tmp/bw_build --transforms jsx \
--jsx-pragma React.createElement --jsx-fragment-pragma React.Fragment && \
cp /tmp/bw_build/App.js App.compiled.js && rm -rf /tmp/bw_src /tmp/bw_build
```

**Cuando la extensión esté habilitada**, aparecerá automáticamente una nueva pestaña "🔧 My Tool" en la barra de navegación principal.

---

#### Hooks Disponibles

Las extensiones tienen acceso a estos hooks de mitmproxy:

```python
class MiExtension:
    name = "mi_extension"

    def on_load(self, cfg: dict, full_config: dict):
        """Llamado cuando se carga la extensión (al iniciar proxy)"""
        pass

    def on_request(self, flow: http.HTTPFlow, cfg: dict, full_config: dict):
        """Llamado ANTES de enviar cada petición

        Args:
            flow: Objeto HTTPFlow de mitmproxy
            cfg: Configuración específica de esta extensión
            full_config: Configuración completa del proyecto
        """
        # Modificar request
        flow.request.url = "https://example.com/modified"
        flow.request.headers["X-Modified"] = "true"
        flow.request.content = b"nuevo body"

    def on_response(self, flow: http.HTTPFlow, cfg: dict, full_config: dict):
        """Llamado DESPUÉS de recibir cada respuesta"""
        # Modificar response
        flow.response.status_code = 200
        flow.response.headers["X-Injected"] = "by-extension"
        flow.response.content = b"modified response"

    def on_websocket_message(self, flow: http.HTTPFlow, cfg: dict, full_config: dict):
        """Llamado cuando se recibe un mensaje WebSocket"""
        pass
```

**Objeto `flow` de mitmproxy:**

```python
# Request
flow.request.method          # "GET", "POST", etc.
flow.request.url             # URL completa
flow.request.pretty_host     # Host sin puerto
flow.request.port            # Puerto
flow.request.path            # Path + query string
flow.request.headers         # Dict-like de headers
flow.request.content         # Body (bytes)
flow.request.text            # Body como string

# Response (solo en on_response)
flow.response.status_code    # 200, 404, etc.
flow.response.headers        # Dict-like de headers
flow.response.content        # Body (bytes)
flow.response.text           # Body como string
```

---

#### Ejemplo Completo: Rate Limiter

Esta extensión incluida añade delays configurables entre peticiones:

```python
EXTENSION_META = {
    "name": "rate_limiter",
    "title": "Rate Limiter",
    "description": "Añade delays entre requests para evitar rate limiting",
    "tabs": [
        {"id": "main", "label": "⏱️ Rate Limiter"}
    ],
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
```

**Uso:**
1. Ve a Extensions → habilita "Rate Limiter"
2. Configura delay (ej. 1000ms = 1 segundo entre requests)
3. Elige si aplicar a todos los hosts o uno específico
4. ¡Listo! Tus requests tendrán delay automático

---

#### Ideas para Extensiones

**Automatización:**
- Auto-login: Extrae tokens de `/login` y los inyecta automáticamente
- Session keeper: Renueva sesiones expiradas automáticamente
- Retry on error: Reintenta peticiones fallidas con backoff exponencial

**Seguridad:**
- SQL injection scanner: Detecta parámetros vulnerables a SQLi
- XSS detector: Analiza responses en busca de reflejos sin sanitizar
- SSRF fuzzer: Inyecta payloads SSRF en parámetros de URL

**Análisis:**
- Response time logger: Guarda métricas de latencia por endpoint
- Size tracker: Monitorea tamaño de requests/responses para detectar anomalías
- Header collector: Extrae headers interesantes (CSP, CORS, Security headers)

**Modificación:**
- User-Agent rotator: Rota User-Agents automáticamente
- Encoding fuzzer: Prueba diferentes encodings en parámetros
- Cache buster: Añade parámetros random para evitar caché

---

#### Estructura de Archivos

```
backend/extensions/
├── __init__.py               # Archivo vacío (requerido)
├── match_replace.py          # Extensión con componente React custom
├── webhook_site.py           # Extensión con tab propia
├── sensitive_discoverer.py   # Extensión UI-only
├── rate_limiter.py           # Extensión schema-driven
└── mi_extension.py           # Tu extensión personalizada
```

Cada archivo debe:
1. Definir `EXTENSION_META` con metadata
2. Implementar una clase con hooks (`on_request`, `on_response`, etc.)
3. Exportar función `register()` que retorna una instancia

---

#### Debugging de Extensiones

**Ver logs del proxy:**

```bash
# El proxy de mitmproxy muestra logs en la terminal donde corrió start.sh
# Busca líneas con [blackwire][ext]
```

**Agregar prints en tu extensión:**

```python
def on_request(self, flow, cfg, full_config):
    print(f"[mi_extension] Processing: {flow.request.url}")
    # Los prints aparecen en la terminal del proxy
```

**Verificar que se cargó:**

```bash
# Buscar en logs al iniciar proxy:
# [blackwire][ext] Loaded extensions: ['match_replace', 'webhook_site', 'mi_extension']
```

---

**¡Crea extensiones y compártelas con la comunidad!** Abre un Pull Request en el repo para incluir tu extensión en BlackWire.

---

### Git Integration

Control de versiones integrado para el proyecto:

1. Ve a la pestaña Git
2. Escribe un mensaje de commit
3. Realiza commits del estado actual del proyecto
4. Revisa el historial de commits

---

## Arquitectura

```
Blackwire/
├── backend/
│   ├── main.py              # API FastAPI + servidor principal
│   ├── frontend.html         # HTML con CSS embebido
│   ├── extensions/           # Plugins Python
│   └── chepy_compat.py       # Motor de operaciones Cipher
├── frontend/
│   ├── App.jsx               # Aplicación React completa (~5400 líneas)
│   ├── App.compiled.js       # JSX pre-transpilado (generado automáticamente)
│   ├── themes.js             # Definiciones de temas
│   └── index.html            # HTML standalone
├── projects/                 # Bases de datos SQLite por proyecto
│   └── {project_name}/
│       ├── config.json       # Configuración del proyecto (scope, settings)
│       └── data.db           # SQLite con requests, repeater, collections,
│                             # session rules, filter presets
├── launch-with-browser.sh    # Launcher principal (sin terminal)
├── start.sh                  # Inicio manual
├── stop.sh                   # Parar el server
├── install.sh                # Instalador automático
├── install-desktop.sh        # Instalar launcher en menú
└── requirements.txt          # Dependencias Python
```

**Stack tecnológico:**
- **Backend**: Python 3.8+ / FastAPI / Uvicorn
- **Proxy Engine**: mitmproxy
- **Frontend**: React 18 (single-file, pre-transpilado con Sucrase)
- **Database**: SQLite (una DB por proyecto)
- **Compression**: GZip middleware

---

## Portabilidad

BlackWire es **100% portable**. Todos los scripts detectan automáticamente su ubicación.

### Mover a otro directorio
```bash
mv Blackwire /opt/Blackwire
cd /opt/Blackwire
./launch-with-browser.sh
```

### Copiar a otra máquina
```bash
# En máquina origen
tar -czf blackwire.tar.gz Blackwire/

# En máquina destino
tar -xzf blackwire.tar.gz
cd Blackwire
./install.sh
```

### Reinstalar desktop launcher tras mover
```bash
./uninstall-desktop.sh
./install-desktop.sh
```

### Limitaciones

⚠️ **Entorno Virtual no portable**: El `venv/` contiene rutas absolutas. Solución: `rm -rf venv && ./install.sh`

⚠️ **Desktop Launcher**: Actualizar después de mover el proyecto con `./uninstall-desktop.sh && ./install-desktop.sh`

---

## Verificación y Troubleshooting

### Verificar Instalación

```bash
./verify-install.sh
```

### Troubleshooting Común

| Problema | Solución |
|----------|----------|
| Python version too old | Instala Python 3.8+ o usa pyenv |
| pip not found | `sudo apt install python3-pip` |
| Permission denied | `chmod +x *.sh` |
| Port 5000 in use | `lsof -i :5000` → `kill <PID>`, o usa `./stop.sh` |
| Port 8080 in use | `lsof -i :8080` → `kill <PID>` |
| Certificado no funciona | `rm -rf ~/.mitmproxy && ./install.sh` |
| App carga lento | Verifica que Node.js/npm están instalados para pre-transpilación |
| Server no para | `./stop.sh` o `curl -X POST http://localhost:5000/api/shutdown` |

---

## API

La documentación interactiva del API está disponible en http://localhost:5000/docs cuando el server está corriendo.

---

## Contribuir

Este proyecto es un espacio abierto para aprender, experimentar y construir juntos. **Buscamos activamente contribuciones**:

- **Funcionalidades**: Ideas para nuevas características, integraciones, mejoras en el interceptor
- **Código**: Corrección de bugs, optimización de rendimiento, mejoras en legibilidad
- **Extensiones**: Plugins para automatizar tareas de pentesting o análisis
- **Temas**: Nuevos esquemas de color para la interfaz

No necesitas ser experto para ayudar. Si crees que algo puede explicarse mejor o hacerse de forma más elegante, **abre un Pull Request**.

---

## Créditos

Proyecto inspirado en [Burp Suite](https://portswigger.net/burp), [OWASP ZAP](https://www.zaproxy.org/), [mitmproxy](https://mitmproxy.org/) y [Caido](https://caido.io/).

Creado por **[Erik Alcantara](https://www.linkedin.com/in/erik-alc%C3%A1ntara-covarrubias-29a97628a/)**.

**Tecnologías:**
- [mitmproxy](https://mitmproxy.org/) — Motor de proxy
- [FastAPI](https://fastapi.tiangolo.com/) — Backend API
- [React](https://react.dev/) — Frontend
- [Sucrase](https://github.com/alangpierce/sucrase) — Transpilación JSX
- [SQLite](https://www.sqlite.org/) — Base de datos
