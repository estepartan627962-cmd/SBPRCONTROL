from pathlib import Path
from urllib.parse import quote

import streamlit as st


# ============================================================
# CONFIGURACIÓN
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
ASSETS = BASE_DIR / "assets"

LOGO = ASSETS / "logo_sbpr.png"
BANNER = ASSETS / "banner_sbpr.jpg"
IMG_CONTABILIDAD = ASSETS / "servicios_contables.jpg"
IMG_SST = ASSETS / "servicios_sst.jpg"

st.set_page_config(
    page_title="SBPR Accounting & Control",
    page_icon=str(LOGO) if LOGO.exists() else "📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

WHATSAPP = "593995328482"
TELEFONO = "099 532 8482"
CORREO = "sbprcontrol@gmail.com"


# ============================================================
# IDENTIDAD VISUAL SBPR
# ============================================================

AZUL_SBPR = "#071F4B"
AZUL_SECUNDARIO = "#123A72"
DORADO_SBPR = "#C8921B"
DORADO_CLARO = "#E8C56A"
BLANCO = "#FFFFFF"
FONDO_CLARO = "#F5F7FB"
TEXTO = "#1D2A3A"


def aplicar_estilo_sbpr() -> None:
    """Aplica la identidad azul, dorada y blanca de SBPR."""
    st.markdown(
        f"""
        <style>
        :root {{
            --sbpr-azul: {AZUL_SBPR};
            --sbpr-azul-2: {AZUL_SECUNDARIO};
            --sbpr-dorado: {DORADO_SBPR};
            --sbpr-dorado-claro: {DORADO_CLARO};
            --sbpr-blanco: {BLANCO};
            --sbpr-fondo: {FONDO_CLARO};
            --sbpr-texto: {TEXTO};
        }}

        html, body, [class*="css"] {{
            color: var(--sbpr-texto);
        }}

        /* Fondo general */
        [data-testid="stAppViewContainer"] {{
            background:
                radial-gradient(circle at 92% 4%, rgba(200, 146, 27, 0.10), transparent 24rem),
                linear-gradient(180deg, #FFFFFF 0%, #F5F7FB 100%);
            color: var(--sbpr-texto);
        }}

        [data-testid="stHeader"] {{
            background: rgba(255, 255, 255, 0.90);
            border-bottom: 1px solid rgba(7, 31, 75, 0.08);
            backdrop-filter: blur(10px);
        }}

        .block-container {{
            max-width: 1280px;
            padding-top: 4.2rem;
            padding-bottom: 3rem;
        }}

        /* Barra lateral */
        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, var(--sbpr-azul) 0%, #0B2D63 100%);
            border-right: 3px solid var(--sbpr-dorado);
        }}

        [data-testid="stSidebar"] * {{
            color: var(--sbpr-blanco);
        }}

        [data-testid="stSidebar"] hr {{
            border-color: rgba(232, 197, 106, 0.35);
        }}

        [data-testid="stSidebar"] [data-testid="stImage"] {{
            background: var(--sbpr-blanco);
            border: 1px solid var(--sbpr-dorado-claro);
            border-radius: 18px;
            padding: 0.55rem;
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.18);
        }}

        /* Tipografía */
        h1, h2, h3 {{
            color: var(--sbpr-azul) !important;
            letter-spacing: -0.02em;
            line-height: 1.15 !important;
        }}

        h1 {{
            font-weight: 800 !important;
        }}

        h2, h3 {{
            font-weight: 700 !important;
        }}

        p, li, label, span, div {{
            color: var(--sbpr-azul);
        }}

        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] li,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] div {{
            color: var(--sbpr-blanco) !important;
        }}

        [data-testid="stSidebar"] a {{
            color: var(--sbpr-blanco) !important;
            text-decoration-color: rgba(255,255,255,0.7) !important;
        }}

        [data-testid="stCaptionContainer"] p {{
            color: var(--sbpr-azul-2) !important;
            font-weight: 700;
            letter-spacing: 0.04em;
        }}

        a {{
            color: var(--sbpr-azul-2);
        }}

        .stMarkdown, .stMarkdown p, .stMarkdown li, .stText, .stText p {{
            color: var(--sbpr-azul) !important;
        }}

        .stAlert p, .stAlert li, .stAlert span {{
            color: var(--sbpr-azul) !important;
        }}

        /* Botones generales */
        div[data-testid="stButton"] > button,
        div[data-testid="stLinkButton"] a,
        a[data-testid^="stBaseLinkButton"] {{
            border-radius: 14px !important;
            border: 1px solid var(--sbpr-azul) !important;
            font-weight: 700 !important;
            min-height: 3rem !important;
            padding: 0.65rem 1rem !important;
            transition: all 0.20s ease !important;
            box-shadow: 0 5px 14px rgba(7, 31, 75, 0.10);
            text-decoration: none !important;
        }}

        div[data-testid="stButton"] > button:not([kind="primary"]),
        div[data-testid="stLinkButton"] a,
        a[data-testid="stBaseLinkButton-secondary"] {{
            background: var(--sbpr-blanco) !important;
            color: var(--sbpr-azul) !important;
        }}

        div[data-testid="stButton"] > button:not([kind="primary"]) *,
        div[data-testid="stLinkButton"] a *,
        a[data-testid="stBaseLinkButton-secondary"] * {{
            color: var(--sbpr-azul) !important;
        }}

        div[data-testid="stButton"] > button[kind="primary"],
        a[data-testid="stBaseLinkButton-primary"] {{
            background: linear-gradient(135deg, var(--sbpr-azul), var(--sbpr-azul-2)) !important;
            color: var(--sbpr-blanco) !important;
            border-color: var(--sbpr-azul) !important;
        }}

        div[data-testid="stButton"] > button[kind="primary"] *,
        a[data-testid="stBaseLinkButton-primary"] * {{
            color: var(--sbpr-blanco) !important;
        }}

        div[data-testid="stButton"] > button:hover,
        div[data-testid="stLinkButton"] a:hover,
        a[data-testid^="stBaseLinkButton"]:hover {{
            background: linear-gradient(135deg, var(--sbpr-dorado), var(--sbpr-dorado-claro)) !important;
            color: var(--sbpr-azul) !important;
            border-color: var(--sbpr-dorado) !important;
            transform: translateY(-2px);
            box-shadow: 0 10px 22px rgba(200, 146, 27, 0.25);
        }}

        [data-testid="stSidebar"] div[data-testid="stButton"] > button,
        [data-testid="stSidebar"] div[data-testid="stLinkButton"] a,
        [data-testid="stSidebar"] a[data-testid^="stBaseLinkButton"] {{
            background: rgba(255,255,255,0.10) !important;
            color: var(--sbpr-blanco) !important;
            border: 1px solid rgba(255,255,255,0.18) !important;
        }}

        [data-testid="stSidebar"] div[data-testid="stButton"] > button:hover,
        [data-testid="stSidebar"] div[data-testid="stLinkButton"] a:hover,
        [data-testid="stSidebar"] a[data-testid^="stBaseLinkButton"]:hover {{
            background: linear-gradient(135deg, var(--sbpr-dorado), var(--sbpr-dorado-claro)) !important;
            color: var(--sbpr-azul) !important;
            border-color: var(--sbpr-dorado) !important;
        }}


        /* Refuerzo de contraste en sidebar */
        [data-testid="stSidebar"] .stMarkdown,
        [data-testid="stSidebar"] .stMarkdown p,
        [data-testid="stSidebar"] .stMarkdown li,
        [data-testid="stSidebar"] [data-testid="stCaptionContainer"] p,
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] strong {{
            color: var(--sbpr-blanco) !important;
        }}

        [data-testid="stSidebar"] div[data-testid="stButton"] > button *,
        [data-testid="stSidebar"] div[data-testid="stLinkButton"] a *,
        [data-testid="stSidebar"] a[data-testid^="stBaseLinkButton"] * {{
            color: var(--sbpr-blanco) !important;
            fill: var(--sbpr-blanco) !important;
        }}

        [data-testid="stSidebar"] div[data-testid="stButton"] > button:hover *,
        [data-testid="stSidebar"] div[data-testid="stLinkButton"] a:hover *,
        [data-testid="stSidebar"] a[data-testid^="stBaseLinkButton"]:hover * {{
            color: var(--sbpr-azul) !important;
            fill: var(--sbpr-azul) !important;
        }}

        /* Tarjetas, formularios y métricas */
        [data-testid="stVerticalBlockBorderWrapper"],
        [data-testid="stForm"],
        [data-testid="stExpander"],
        [data-testid="stMetric"] {{
            background: rgba(255, 255, 255, 0.97);
            border: 1px solid rgba(7, 31, 75, 0.12) !important;
            border-radius: 16px !important;
            box-shadow: 0 10px 28px rgba(7, 31, 75, 0.08);
        }}

        [data-testid="stMetric"] {{
            border-top: 4px solid var(--sbpr-dorado) !important;
            padding: 1rem 1.1rem;
        }}

        [data-testid="stMetricValue"] {{
            color: var(--sbpr-azul) !important;
            font-weight: 800;
        }}

        [data-testid="stMetricLabel"] *,
        [data-testid="stMetricDelta"] * {{
            color: var(--sbpr-azul-2) !important;
        }}

        /* Campos */
        input, textarea, [data-baseweb="select"] > div {{
            background-color: var(--sbpr-blanco) !important;
            color: var(--sbpr-texto) !important;
            border-color: rgba(7, 31, 75, 0.22) !important;
            border-radius: 10px !important;
        }}

        input:focus, textarea:focus {{
            border-color: var(--sbpr-dorado) !important;
            box-shadow: 0 0 0 2px rgba(200, 146, 27, 0.18) !important;
        }}

        /* Selects, pills y controles de formularios */
        [data-baseweb="select"] > div,
        [data-baseweb="select"] input,
        [data-baseweb="select"] span,
        [data-baseweb="select"] div {{
            color: var(--sbpr-azul) !important;
        }}

        [data-baseweb="select"] svg {{
            fill: var(--sbpr-azul) !important;
        }}

        div[data-baseweb="popover"] {{
            background: transparent !important;
        }}

        div[data-baseweb="popover"] ul {{
            background: var(--sbpr-blanco) !important;
            border: 1px solid rgba(7, 31, 75, 0.16) !important;
            border-radius: 14px !important;
            box-shadow: 0 16px 34px rgba(7, 31, 75, 0.16) !important;
            padding: 0.4rem !important;
        }}

        div[data-baseweb="popover"] li,
        div[data-baseweb="popover"] li * {{
            color: var(--sbpr-azul) !important;
            background: transparent !important;
        }}

        div[data-baseweb="popover"] li:hover,
        div[data-baseweb="popover"] li[aria-selected="true"] {{
            background: rgba(7, 31, 75, 0.10) !important;
            border-radius: 10px !important;
        }}

        div[data-testid="stPills"] {{
            gap: 0.5rem;
        }}

        div[data-testid="stPills"] button {{
            background: var(--sbpr-blanco) !important;
            color: var(--sbpr-azul) !important;
            border: 1px solid rgba(7, 31, 75, 0.28) !important;
            border-radius: 999px !important;
            padding: 0.6rem 1rem !important;
            box-shadow: 0 4px 12px rgba(7, 31, 75, 0.08);
        }}

        div[data-testid="stPills"] button * {{
            color: var(--sbpr-azul) !important;
        }}

        div[data-testid="stPills"] button[aria-selected="true"] {{
            background: linear-gradient(135deg, var(--sbpr-azul), var(--sbpr-azul-2)) !important;
            color: var(--sbpr-blanco) !important;
            border-color: var(--sbpr-dorado) !important;
        }}

        div[data-testid="stPills"] button[aria-selected="true"] * {{
            color: var(--sbpr-blanco) !important;
        }}

        div[data-testid="stPills"] button:hover {{
            background: linear-gradient(135deg, var(--sbpr-dorado), var(--sbpr-dorado-claro)) !important;
            color: var(--sbpr-azul) !important;
            border-color: var(--sbpr-dorado) !important;
        }}

        div[data-testid="stPills"] button:hover * {{
            color: var(--sbpr-azul) !important;
        }}

        [data-testid="stRadio"] label,
        [data-testid="stRadio"] div[role="radiogroup"] label {{
            color: var(--sbpr-azul) !important;
        }}

        [data-testid="stSelectSlider"] * {{
            color: var(--sbpr-azul) !important;
        }}

        [data-testid="stSelectSlider"] div[data-baseweb="slider"] > div > div:first-child {{
            background: rgba(7, 31, 75, 0.16) !important;
        }}

        [data-testid="stSelectSlider"] div[data-baseweb="slider"] [role="slider"] {{
            background: var(--sbpr-azul) !important;
            border-color: var(--sbpr-dorado) !important;
            box-shadow: 0 0 0 4px rgba(200, 146, 27, 0.16) !important;
        }}

        input::placeholder,
        textarea::placeholder {{
            color: #8A94A6 !important;
            opacity: 1 !important;
        }}

        /* Pestañas */
        [data-testid="stTabs"] [role="tablist"] {{
            gap: 0.5rem;
            flex-wrap: wrap;
        }}

        [data-testid="stTabs"] button[role="tab"] {{
            background: rgba(255, 255, 255, 0.96) !important;
            color: var(--sbpr-azul) !important;
            border: 1px solid rgba(7, 31, 75, 0.12) !important;
            border-radius: 12px 12px 0 0 !important;
            padding: 0.6rem 1rem !important;
        }}

        [data-testid="stTabs"] button[role="tab"] * {{
            color: var(--sbpr-azul) !important;
        }}

        [data-testid="stTabs"] button[aria-selected="true"] {{
            background: var(--sbpr-azul) !important;
            color: var(--sbpr-blanco) !important;
            border-bottom-color: var(--sbpr-dorado) !important;
            font-weight: 800;
        }}

        [data-testid="stTabs"] button[aria-selected="true"] * {{
            color: var(--sbpr-blanco) !important;
        }}

        /* Navegación superior */
        .sbpr-nav-label {{
            margin-top: 0.35rem;
            margin-bottom: 0.75rem;
            color: var(--sbpr-azul) !important;
            font-size: 0.85rem;
            font-weight: 800;
            letter-spacing: 0.05em;
            text-transform: uppercase;
        }}

        .sbpr-nav-spacer {{
            height: 0.2rem;
        }}

        /* Barras de progreso */
        [data-testid="stProgressBar"] > div > div {{
            background: linear-gradient(90deg, var(--sbpr-azul), var(--sbpr-dorado)) !important;
        }}

        hr {{
            border-color: rgba(200, 146, 27, 0.28) !important;
        }}

        /* Bloques visuales usados cuando no existe una imagen */
        .sbpr-visual {{
            min-height: 220px;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 2rem;
            border-radius: 18px;
            border: 1px solid rgba(200, 146, 27, 0.45);
            background:
                radial-gradient(circle at top right, rgba(232, 197, 106, 0.42), transparent 40%),
                linear-gradient(135deg, var(--sbpr-azul), var(--sbpr-azul-2));
            color: var(--sbpr-blanco) !important;
            box-shadow: 0 14px 30px rgba(7, 31, 75, 0.18);
        }}

        .sbpr-visual * {{
            color: var(--sbpr-blanco) !important;
        }}

        .sbpr-visual-icon {{
            font-size: 3rem;
            line-height: 1;
            margin-bottom: 0.8rem;
        }}

        .sbpr-visual-title {{
            font-size: 1.25rem;
            font-weight: 800;
        }}

        .sbpr-visual-line {{
            width: 72px;
            height: 3px;
            margin-top: 1rem;
            border-radius: 99px;
            background: var(--sbpr-dorado-claro);
        }}

        /* Ocultar elementos de Streamlit que ensucian la vista */
        [data-testid="stToolbar"], footer {{
            visibility: hidden;
            height: 0;
            position: fixed;
        }}

        /* Ajuste móvil */
        @media (max-width: 900px) {{
            .block-container {{
                padding-top: 4.4rem;
                padding-left: 1rem;
                padding-right: 1rem;
            }}

            h1 {{
                font-size: 2.1rem !important;
            }}

            h2 {{
                font-size: 1.6rem !important;
            }}

            div[data-testid="stButton"] > button,
            div[data-testid="stLinkButton"] a {{
                min-height: 3.1rem !important;
                white-space: normal !important;
            }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


aplicar_estilo_sbpr()


# ============================================================
# CATÁLOGO DE SERVICIOS
# ============================================================

SERVICIOS_CONTABLES = {
    "🧾 Declaración de IVA": (
        "Preparación, revisión y presentación de declaraciones "
        "dentro de los plazos correspondientes."
    ),
    "💰 Impuesto a la renta": (
        "Cálculo, planificación y presentación para cumplir "
        "correctamente y pagar lo justo."
    ),
    "📚 Contabilidad mensual": (
        "Registro, organización y análisis de la información "
        "financiera del negocio."
    ),
    "🔎 Obligaciones SRI": (
        "Revisión de pendientes, vencimientos y posibles riesgos "
        "tributarios."
    ),
    "📦 Inventarios": (
        "Control de existencias, movimientos, diferencias y valor "
        "de los productos."
    ),
    "🏦 Conciliaciones bancarias": (
        "Comparación de movimientos bancarios con los registros "
        "contables."
    ),
    "📈 Reportes y flujo de caja": (
        "Información clara para conocer liquidez, obligaciones "
        "y capacidad de crecimiento."
    ),
    "⚙️ Mejora de procesos": (
        "Optimización de controles administrativos para reducir "
        "errores, tiempo y costos."
    ),
    "👵 Devolución de IVA": (
        "Acompañamiento para personas de tercera edad durante "
        "todo el proceso."
    ),
}

SERVICIOS_SST = {
    "⚖️ Diagnóstico legal SST": (
        "Evaluación del cumplimiento y definición de prioridades "
        "de mejora."
    ),
    "⚠️ Matriz de riesgos": (
        "Identificación, valoración y control de peligros por "
        "puesto y proceso."
    ),
    "🛡️ Plan de prevención": (
        "Acciones concretas para reducir incidentes y fortalecer "
        "los controles."
    ),
    "🎓 Capacitaciones": (
        "Formación práctica para trabajadores, responsables y "
        "equipos de trabajo."
    ),
    "🔍 Inspecciones": (
        "Revisión de condiciones inseguras y elaboración de "
        "planes de acción."
    ),
    "🧩 Investigación de incidentes": (
        "Análisis de causas y establecimiento de medidas "
        "correctivas."
    ),
    "🚨 Planes de emergencia": (
        "Protocolos de evacuación, brigadas, simulacros y "
        "respuesta."
    ),
    "🗂️ Gestión documental": (
        "Organización de procedimientos, matrices, registros "
        "y evidencias."
    ),
    "🧠 Ergonomía y riesgo psicosocial": (
        "Evaluación preventiva para mejorar el bienestar y "
        "desempeño laboral."
    ),
}

SERVICIOS_POR_AREA = {
    "Contabilidad y tributación": list(SERVICIOS_CONTABLES),
    "Seguridad y salud ocupacional": list(SERVICIOS_SST),
    "Solución integral": [
        "Diagnóstico integral SBPR",
        "Acompañamiento mensual",
        "Propuesta personalizada",
    ],
}


# ============================================================
# FUNCIONES
# ============================================================

def url_whatsapp(mensaje: str) -> str:
    return f"https://wa.me/{WHATSAPP}?text={quote(mensaje)}"


def mostrar_logo() -> None:
    if LOGO.exists():
        try:
            st.logo(str(LOGO))
        except Exception:
            pass


def mostrar_imagen_o_bloque(
    ruta: Path,
    icono: str,
    titulo: str,
) -> None:
    """Muestra una imagen o un bloque corporativo de respaldo."""
    if ruta.exists():
        st.image(str(ruta), use_container_width=True)
        return

    st.markdown(
        f"""
        <div class="sbpr-visual">
            <div class="sbpr-visual-icon">{icono}</div>
            <div class="sbpr-visual-title">{titulo}</div>
            <div class="sbpr-visual-line"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def navegar(nombre: str) -> None:
    st.session_state.pagina = nombre
    st.rerun()


def tarjeta_servicio(
    titulo: str,
    descripcion: str,
    etiqueta: str,
) -> None:
    with st.container(border=True):
        st.subheader(titulo)
        st.write(descripcion)
        st.caption(f"✅ {etiqueta}")


def encabezado(
    etiqueta: str,
    titulo: str,
    descripcion: str,
) -> None:
    st.caption(etiqueta.upper())
    st.title(titulo)
    st.write(descripcion)


def selector_navegacion() -> str:
    opciones = [
        "🏠 Inicio",
        "📊 Contabilidad",
        "🛡️ Seguridad y salud",
        "🧭 Diagnóstico",
        "📞 Contacto",
    ]

    actual = st.session_state.pagina
    st.markdown('<div class="sbpr-nav-label">Navegación principal</div>', unsafe_allow_html=True)

    columnas = st.columns(len(opciones))
    seleccion = actual

    for columna, opcion in zip(columnas, opciones):
        with columna:
            if st.button(
                opcion,
                key=f"nav_{opcion}",
                type="primary" if opcion == actual else "secondary",
                use_container_width=True,
            ):
                seleccion = opcion

    st.markdown('<div class="sbpr-nav-spacer"></div>', unsafe_allow_html=True)
    return seleccion


def mostrar_catalogo(
    catalogo: dict[str, str],
    etiqueta: str,
) -> None:
    elementos = list(catalogo.items())

    for posicion in range(0, len(elementos), 3):
        columnas = st.columns(3)

        for columna, (titulo, descripcion) in zip(
            columnas,
            elementos[posicion:posicion + 3],
        ):
            with columna:
                tarjeta_servicio(
                    titulo,
                    descripcion,
                    etiqueta,
                )


def nivel_riesgo(valor: int) -> tuple[str, str]:
    if valor <= 4:
        return "BAJO", "success"
    if valor <= 9:
        return "MODERADO", "info"
    if valor <= 16:
        return "ALTO", "warning"
    return "CRÍTICO", "error"


# ============================================================
# ESTADO
# ============================================================

if "pagina" not in st.session_state:
    st.session_state.pagina = "🏠 Inicio"

if "url_consulta" not in st.session_state:
    st.session_state.url_consulta = ""

if "area_preseleccionada" not in st.session_state:
    st.session_state.area_preseleccionada = (
        "Contabilidad y tributación"
    )


mostrar_logo()


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    if LOGO.exists():
        st.image(str(LOGO), use_container_width=True)

    st.caption("ACCOUNTING · CONTROL · PREVENCIÓN")
    st.divider()

    st.subheader("Atención inmediata")

    st.link_button(
        "💬 WhatsApp Business",
        url_whatsapp(
            "Hola SBPR, deseo información sobre sus servicios."
        ),
        type="primary",
        use_container_width=True,
    )

    st.link_button(
        "✉️ Enviar correo",
        (
            f"mailto:{CORREO}"
            "?subject=Consulta%20de%20servicios%20SBPR"
        ),
        use_container_width=True,
    )

    st.divider()

    st.write("📍 **Quito, Ecuador**")
    st.write(f"📱 **{TELEFONO}**")
    st.write(f"📧 **{CORREO}**")

    st.divider()

    st.caption(
        "Soluciones para personas naturales, emprendedores, "
        "PYMES y empresas."
    )


# ============================================================
# NAVEGACIÓN SUPERIOR
# ============================================================

seleccion = selector_navegacion()

if seleccion != st.session_state.pagina:
    st.session_state.pagina = seleccion
    st.rerun()

pagina = st.session_state.pagina


# ============================================================
# INICIO
# ============================================================

if pagina == "🏠 Inicio":

    if BANNER.exists():
        st.image(str(BANNER), use_container_width=True)

    st.caption(
        "SOLUCIONES INTEGRALES PARA PERSONAS NATURALES Y EMPRESAS"
    )

    titulo, logo = st.columns(
        [1.45, 0.55],
        vertical_alignment="center",
    )

    with titulo:
        st.title(
            "Orden financiero, prevención y control "
            "para hacer crecer tu empresa."
        )

        st.write(
            """
            **SBPR Accounting & Control** integra servicios
            contables, tributarios, administrativos y de
            seguridad y salud ocupacional.

            Transformamos obligaciones, riesgos y procesos
            complejos en acciones claras, medibles y útiles.
            """
        )

        accion_1, accion_2 = st.columns(2)

        with accion_1:
            if st.button(
                "📊 Explorar contabilidad",
                type="primary",
                use_container_width=True,
            ):
                navegar("📊 Contabilidad")

        with accion_2:
            if st.button(
                "🛡️ Explorar seguridad y salud",
                use_container_width=True,
            ):
                navegar("🛡️ Seguridad y salud")

    with logo:
        if LOGO.exists():
            st.image(str(LOGO), use_container_width=True)

    st.divider()

    metrica_1, metrica_2, metrica_3, metrica_4 = st.columns(4)

    with metrica_1:
        st.metric(
            "Unidades especializadas",
            "2",
            "Solución integral",
        )

    with metrica_2:
        st.metric(
            "Visión de control",
            "360°",
            "Finanzas, procesos y personas",
        )

    with metrica_3:
        st.metric(
            "Atención",
            "Directa",
            "WhatsApp y correo",
        )

    with metrica_4:
        st.metric(
            "Cobertura",
            "Ecuador",
            "Presencial y remota",
        )

    st.divider()

    encabezado(
        "Unidades SBPR",
        "Dos áreas especializadas. Una estrategia integral.",
        (
            "Puedes contratar una solución puntual o combinar "
            "las dos unidades para obtener mayor control."
        ),
    )

    area_contable, area_sst = st.columns(2)

    with area_contable:
        with st.container(border=True):
            mostrar_imagen_o_bloque(
                IMG_CONTABILIDAD,
                "📊",
                "Contabilidad y tributación",
            )
            st.subheader("📊 Contabilidad y tributación")
            st.write(
                "Cumple con el SRI, organiza tus cuentas, "
                "controla inventarios y toma decisiones con "
                "información confiable."
            )
            st.progress(0.92, text="Nivel de control financiero")
            if st.button(
                "Ver soluciones contables",
                key="inicio_contable",
                type="primary",
                use_container_width=True,
            ):
                navegar("📊 Contabilidad")

    with area_sst:
        with st.container(border=True):
            mostrar_imagen_o_bloque(
                IMG_SST,
                "🛡️",
                "Seguridad y salud ocupacional",
            )
            st.subheader("🛡️ Seguridad y salud ocupacional")
            st.write(
                "Previene accidentes, cumple la normativa, "
                "controla riesgos y protege a tu equipo."
            )
            st.progress(0.90, text="Nivel de control preventivo")
            if st.button(
                "Ver soluciones SST",
                key="inicio_sst",
                use_container_width=True,
            ):
                navegar("🛡️ Seguridad y salud")

    st.divider()

    encabezado(
        "Asistente rápido",
        "Encuentra la solución que necesitas",
        (
            "Selecciona tu preocupación principal y te mostraremos "
            "la ruta recomendada."
        ),
    )

    problema = st.selectbox(
        "¿Cuál es tu necesidad principal?",
        [
            "Selecciona una necesidad",
            "Tengo obligaciones pendientes con el SRI",
            "No conozco la rentabilidad real de mi negocio",
            "Tengo diferencias de inventario o bancos",
            "Necesito organizar la contabilidad mensual",
            "No tengo una matriz de riesgos actualizada",
            "Necesito preparar un plan de emergencia",
            "Quiero capacitar al personal",
            "Necesito revisar toda la empresa",
        ],
    )

    recomendaciones = {
        "Tengo obligaciones pendientes con el SRI": (
            "📊 Contabilidad",
            "Revisión de obligaciones SRI",
        ),
        "No conozco la rentabilidad real de mi negocio": (
            "📊 Contabilidad",
            "Reportes financieros y flujo de caja",
        ),
        "Tengo diferencias de inventario o bancos": (
            "📊 Contabilidad",
            "Inventarios y conciliaciones bancarias",
        ),
        "Necesito organizar la contabilidad mensual": (
            "📊 Contabilidad",
            "Contabilidad mensual",
        ),
        "No tengo una matriz de riesgos actualizada": (
            "🛡️ Seguridad y salud",
            "Matriz de riesgos laborales",
        ),
        "Necesito preparar un plan de emergencia": (
            "🛡️ Seguridad y salud",
            "Plan de emergencia y evacuación",
        ),
        "Quiero capacitar al personal": (
            "🛡️ Seguridad y salud",
            "Capacitaciones SST",
        ),
        "Necesito revisar toda la empresa": (
            "🧭 Diagnóstico",
            "Diagnóstico integral SBPR",
        ),
    }

    if problema in recomendaciones:
        pagina_recomendada, servicio = recomendaciones[problema]
        st.success(
            f"Ruta recomendada: **{servicio}**."
        )
        if st.button(
            f"Abrir {pagina_recomendada}",
            use_container_width=True,
        ):
            navegar(pagina_recomendada)

    st.divider()

    st.subheader("Cómo trabaja SBPR")

    paso_1, paso_2, paso_3, paso_4 = st.columns(4)

    pasos = [
        ("01", "🔍 Escuchamos", "Conocemos tu necesidad."),
        ("02", "🧭 Diagnosticamos", "Priorizamos riesgos."),
        ("03", "⚙️ Implementamos", "Ejecutamos soluciones."),
        ("04", "📈 Acompañamos", "Medimos y mejoramos."),
    ]

    for columna, (numero, nombre, detalle) in zip(
        [paso_1, paso_2, paso_3, paso_4],
        pasos,
    ):
        with columna:
            with st.container(border=True):
                st.title(numero)
                st.subheader(nombre)
                st.write(detalle)


# ============================================================
# CONTABILIDAD
# ============================================================

elif pagina == "📊 Contabilidad":

    encabezado(
        "Unidad financiera",
        "Contabilidad y tributación con visión empresarial",
        (
            "No solo presentamos declaraciones. Organizamos tu "
            "información para cumplir, controlar y decidir."
        ),
    )

    texto, imagen = st.columns(
        [1, 1],
        vertical_alignment="center",
    )

    with texto:
        st.subheader(
            "Tu tranquilidad financiera empieza con orden"
        )

        st.write(
            """
            Diseñamos una ruta de trabajo según tu actividad,
            obligaciones y volumen de información.

            El objetivo es reducir riesgos tributarios,
            proteger la liquidez y entregar información
            comprensible para la toma de decisiones.
            """
        )

        st.success(
            "✅ Cumplimiento + control + información para decidir."
        )

        if st.button(
            "Solicitar diagnóstico contable",
            type="primary",
            use_container_width=True,
        ):
            st.session_state.area_preseleccionada = (
                "Contabilidad y tributación"
            )
            navegar("🧭 Diagnóstico")

    with imagen:
        mostrar_imagen_o_bloque(
            IMG_CONTABILIDAD,
            "📈",
            "Control financiero con visión empresarial",
        )

    st.divider()

    tab_personas, tab_pymes, tab_control = st.tabs(
        [
            "👤 Personas naturales",
            "🏢 PYMES",
            "📈 Control y decisiones",
        ]
    )

    with tab_personas:
        st.write(
            """
            **Soluciones principales**

            - Declaración de IVA.
            - Impuesto a la renta.
            - Devolución de IVA para tercera edad.
            - Revisión de obligaciones pendientes.
            - Organización de gastos deducibles.
            """
        )

    with tab_pymes:
        st.write(
            """
            **Soluciones principales**

            - Contabilidad mensual.
            - Declaraciones tributarias.
            - Inventarios y conciliaciones.
            - Reportes financieros.
            - Flujo de caja.
            """
        )

    with tab_control:
        st.write(
            """
            **Soluciones principales**

            - Mejora de procesos administrativos.
            - Controles internos.
            - Indicadores financieros.
            - Análisis de diferencias.
            - Información para decisiones gerenciales.
            """
        )

    st.divider()

    mostrar_catalogo(
        SERVICIOS_CONTABLES,
        "Control financiero",
    )

    st.divider()

    encabezado(
        "Semáforo tributario",
        "Evalúa rápidamente tu nivel de organización",
        (
            "Marca las situaciones que actualmente aplican "
            "a tu caso."
        ),
    )

    col_1, col_2 = st.columns(2)

    with col_1:
        pendiente = st.checkbox(
            "Tengo declaraciones u obligaciones pendientes"
        )
        documentos = st.checkbox(
            "Mis documentos contables están desorganizados"
        )
        inventario = st.checkbox(
            "Existen diferencias de inventario"
        )

    with col_2:
        bancos = st.checkbox(
            "No realizo conciliaciones bancarias"
        )
        reportes = st.checkbox(
            "No tengo reportes financieros mensuales"
        )
        flujo = st.checkbox(
            "No conozco con claridad mi flujo de caja"
        )

    total_alertas = sum(
        [
            pendiente,
            documentos,
            inventario,
            bancos,
            reportes,
            flujo,
        ]
    )

    st.progress(
        total_alertas / 6,
        text=f"Alertas identificadas: {total_alertas} de 6",
    )

    if total_alertas == 0:
        st.success(
            "Nivel favorable. Mantén controles y revisiones "
            "periódicas."
        )
    elif total_alertas <= 2:
        st.info(
            "Nivel preventivo. Conviene revisar los puntos "
            "seleccionados."
        )
    elif total_alertas <= 4:
        st.warning(
            "Nivel alto. Es recomendable organizar un plan "
            "de trabajo."
        )
    else:
        st.error(
            "Nivel crítico. Se recomienda una revisión integral "
            "prioritaria."
        )


# ============================================================
# SEGURIDAD Y SALUD OCUPACIONAL
# ============================================================

elif pagina == "🛡️ Seguridad y salud":

    encabezado(
        "Unidad preventiva",
        "Seguridad y salud ocupacional que sí se ejecuta",
        (
            "Soluciones prácticas para prevenir riesgos, cumplir "
            "la normativa y proteger a tu equipo."
        ),
    )

    imagen, texto = st.columns(
        [1, 1],
        vertical_alignment="center",
    )

    with imagen:
        mostrar_imagen_o_bloque(
            IMG_SST,
            "🦺",
            "Prevención, cumplimiento y protección",
        )

    with texto:
        st.subheader(
            "Cumplimiento visible. Prevención real."
        )

        st.write(
            """
            Adaptamos la gestión de SST al tamaño, actividad
            y realidad operativa de la empresa.

            Trabajamos con diagnósticos, matrices, planes,
            capacitación, inspecciones y seguimiento.
            """
        )

        st.success(
            "✅ Prevención + cumplimiento + protección."
        )

        if st.button(
            "Solicitar diagnóstico SST",
            type="primary",
            use_container_width=True,
        ):
            st.session_state.area_preseleccionada = (
                "Seguridad y salud ocupacional"
            )
            navegar("🧭 Diagnóstico")

    st.divider()

    mostrar_catalogo(
        SERVICIOS_SST,
        "Prevención y cumplimiento",
    )

    st.divider()

    encabezado(
        "Radar de riesgos",
        "Calcula el nivel inicial de un peligro",
        (
            "Selecciona la probabilidad y el impacto. El resultado "
            "es orientativo y no reemplaza una evaluación técnica."
        ),
    )

    probabilidad, impacto = st.columns(2)

    with probabilidad:
        valor_probabilidad = st.slider(
            "Probabilidad de ocurrencia",
            min_value=1,
            max_value=5,
            value=3,
            help="1: rara · 5: casi segura",
        )

    with impacto:
        valor_impacto = st.slider(
            "Impacto o consecuencia",
            min_value=1,
            max_value=5,
            value=3,
            help="1: menor · 5: crítica",
        )

    resultado = valor_probabilidad * valor_impacto
    nivel, tipo = nivel_riesgo(resultado)

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric("Probabilidad", valor_probabilidad)

    with m2:
        st.metric("Impacto", valor_impacto)

    with m3:
        st.metric("Nivel calculado", resultado)

    mensaje_nivel = (
        f"Resultado: **{nivel}**. "
        "Documenta el peligro y define controles proporcionales."
    )

    getattr(st, tipo)(mensaje_nivel)

    st.divider()

    st.subheader("Checklist preventivo")

    lista = {
        "Matriz de riesgos actualizada": st.checkbox(
            "Matriz de riesgos actualizada"
        ),
        "Plan de emergencia vigente": st.checkbox(
            "Plan de emergencia vigente"
        ),
        "Capacitaciones registradas": st.checkbox(
            "Capacitaciones registradas"
        ),
        "Inspecciones periódicas": st.checkbox(
            "Inspecciones periódicas"
        ),
        "Investigación de incidentes": st.checkbox(
            "Investigación de incidentes"
        ),
    }

    cumplimiento = sum(lista.values())
    st.progress(
        cumplimiento / len(lista),
        text=(
            f"Cumplimiento preliminar: "
            f"{cumplimiento} de {len(lista)} controles"
        ),
    )


# ============================================================
# DIAGNÓSTICO
# ============================================================

elif pagina == "🧭 Diagnóstico":

    encabezado(
        "Consulta inteligente",
        "Prepara tu solicitud en menos de dos minutos",
        (
            "Completa la información y la aplicación generará "
            "un mensaje organizado para WhatsApp Business."
        ),
    )

    st.info(
        "🔐 Los datos no se almacenan en esta página. "
        "Solo se utilizan para preparar el mensaje."
    )

    area_inicial = st.session_state.area_preseleccionada
    opciones_area = list(SERVICIOS_POR_AREA)

    if hasattr(st, "pills"):
        area = st.pills(
            "Área de interés",
            opciones_area,
            default=area_inicial,
            selection_mode="single",
        )
    else:
        area = st.radio(
            "Área de interés",
            opciones_area,
            index=opciones_area.index(area_inicial),
            horizontal=True,
        )

    area = area or area_inicial
    servicios = SERVICIOS_POR_AREA[area]

    with st.form(
        "consulta_sbpr",
        clear_on_submit=False,
        border=True,
    ):
        nombre_col, tipo_col = st.columns(2)

        with nombre_col:
            nombre = st.text_input(
                "Nombre o empresa",
                placeholder="Ej.: María Pérez / Empresa ABC",
            )

        with tipo_col:
            tipo_cliente = st.selectbox(
                "Tipo de cliente",
                [
                    "Persona natural",
                    "Emprendedor",
                    "PYME",
                    "Empresa",
                ],
            )

        servicio = st.selectbox(
            "Servicio requerido",
            servicios,
        )

        prioridad = st.select_slider(
            "Prioridad",
            options=[
                "Informativa",
                "Normal",
                "Importante",
                "Urgente",
            ],
            value="Normal",
        )

        descripcion = st.text_area(
            "Describe brevemente tu necesidad",
            placeholder=(
                "Ej.: Necesito revisar obligaciones pendientes "
                "y organizar la contabilidad mensual."
            ),
            height=140,
        )

        preparar = st.form_submit_button(
            "Preparar consulta",
            type="primary",
            use_container_width=True,
        )

    if preparar:
        if not nombre.strip():
            st.error(
                "Escribe tu nombre o el nombre de la empresa."
            )
        else:
            mensaje = (
                "Hola SBPR, deseo solicitar información.\n\n"
                f"Nombre / empresa: {nombre.strip()}\n"
                f"Tipo de cliente: {tipo_cliente}\n"
                f"Área: {area}\n"
                f"Servicio: {servicio}\n"
                f"Prioridad: {prioridad}\n"
                f"Detalle: "
                f"{descripcion.strip() or 'Sin detalle adicional'}"
                "\n\nPor favor, indíquenme cómo podemos "
                "coordinar una consulta."
            )

            st.session_state.url_consulta = url_whatsapp(
                mensaje
            )

            st.toast(
                "Consulta preparada correctamente",
                icon="✅",
            )

    if st.session_state.url_consulta:
        with st.status(
            "Consulta lista para enviar",
            expanded=True,
        ):
            st.write(
                "Revisa los datos y abre WhatsApp Business."
            )

            st.link_button(
                "💬 Enviar por WhatsApp",
                st.session_state.url_consulta,
                type="primary",
                use_container_width=True,
            )

            st.link_button(
                "✉️ Consultar por correo",
                (
                    f"mailto:{CORREO}"
                    "?subject=Consulta%20de%20servicios%20SBPR"
                ),
                use_container_width=True,
            )


# ============================================================
# CONTACTO
# ============================================================

elif pagina == "📞 Contacto":

    encabezado(
        "Atención directa",
        "Hablemos de tu necesidad",
        (
            "Coordina una consulta contable, tributaria o de "
            "seguridad y salud ocupacional."
        ),
    )

    whatsapp_col, correo_col, ubicacion_col = st.columns(3)

    with whatsapp_col:
        with st.container(border=True):
            st.title("💬")
            st.subheader("WhatsApp Business")
            st.write(TELEFONO)
            st.link_button(
                "Abrir conversación",
                url_whatsapp(
                    "Hola SBPR, deseo agendar una consulta."
                ),
                type="primary",
                use_container_width=True,
            )

    with correo_col:
        with st.container(border=True):
            st.title("✉️")
            st.subheader("Correo")
            st.write(CORREO)
            st.link_button(
                "Enviar correo",
                (
                    f"mailto:{CORREO}"
                    "?subject=Consulta%20SBPR"
                ),
                use_container_width=True,
            )

    with ubicacion_col:
        with st.container(border=True):
            st.title("📍")
            st.subheader("Cobertura")
            st.write("Quito y Ecuador")
            st.write(
                "Atención presencial y remota según el servicio."
            )

    st.divider()

    st.subheader("Preguntas frecuentes")

    with st.expander(
        "¿Atienden a personas naturales y empresas?"
    ):
        st.write(
            "Sí. Los servicios se adaptan a personas naturales, "
            "emprendedores, PYMES y empresas."
        )

    with st.expander(
        "¿Puedo contratar únicamente un servicio?"
    ):
        st.write(
            "Sí. Puedes solicitar una gestión puntual, un "
            "diagnóstico o acompañamiento mensual."
        )

    with st.expander(
        "¿Cómo se determina el costo?"
    ):
        st.write(
            "Depende del alcance, volumen de información, "
            "número de trabajadores y complejidad."
        )

    with st.expander(
        "¿Atienden fuera de Quito?"
    ):
        st.write(
            "Sí. Varias gestiones pueden realizarse de forma "
            "remota y otras se coordinan presencialmente."
        )


# ============================================================
# PIE DE PÁGINA
# ============================================================

st.divider()

pie_1, pie_2 = st.columns([2, 1])

with pie_1:
    st.caption(
        "SBPR ACCOUNTING & CONTROL · "
        "Orden, cumplimiento y protección."
    )

with pie_2:
    st.caption(
        f"Quito · Ecuador · {TELEFONO}"
    )
