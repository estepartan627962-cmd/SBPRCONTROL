from pathlib import Path
from urllib.parse import quote

import streamlit as st


# =========================================================
# CONFIGURACIÓN GENERAL
# =========================================================

st.set_page_config(
    page_title="SBPR Accounting & Control",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

WHATSAPP_NUMBER = "593995328482"
EMAIL = "sbprcontrol@gmail.com"

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"

LOGO_PATH = ASSETS_DIR / "logo.png"
CONTABILIDAD_IMAGE = ASSETS_DIR / "contabilidad.png"
SST_IMAGE = ASSETS_DIR / "sst.png"


# =========================================================
# INFORMACIÓN DE SERVICIOS
# =========================================================

SERVICIOS_CONTABLES = {
    "Declaración de IVA": (
        "Preparación, revisión y presentación correcta de "
        "declaraciones dentro de los plazos establecidos."
    ),
    "Impuesto a la renta": (
        "Cálculo, planificación y presentación de la declaración "
        "para cumplir correctamente con las obligaciones tributarias."
    ),
    "Contabilidad mensual": (
        "Registro y organización de la información contable para "
        "mantener una visión clara del negocio."
    ),
    "Revisión de obligaciones SRI": (
        "Verificación de obligaciones pendientes, vencimientos "
        "y posibles riesgos tributarios."
    ),
    "Devolución de IVA": (
        "Acompañamiento en procesos de devolución de IVA para "
        "personas de tercera edad."
    ),
    "Control de inventarios": (
        "Organización y control de existencias, movimientos "
        "y diferencias de inventario."
    ),
    "Conciliaciones bancarias": (
        "Comparación de movimientos bancarios con los registros "
        "contables de la empresa."
    ),
    "Reportes financieros": (
        "Preparación de información financiera y flujo de caja "
        "para apoyar la toma de decisiones."
    ),
    "Mejora de procesos": (
        "Optimización de procesos administrativos y financieros "
        "para reducir errores y ahorrar recursos."
    ),
}

SERVICIOS_SST = {
    "Diagnóstico de cumplimiento legal": (
        "Evaluación inicial del cumplimiento de seguridad y salud "
        "ocupacional de la organización."
    ),
    "Matriz de riesgos laborales": (
        "Identificación, análisis y valoración de peligros "
        "por puesto de trabajo y proceso."
    ),
    "Plan de prevención de riesgos": (
        "Definición de controles y acciones para reducir accidentes "
        "y enfermedades laborales."
    ),
    "Capacitaciones SST": (
        "Formación práctica para trabajadores, responsables "
        "y equipos de trabajo."
    ),
    "Inspecciones de seguridad": (
        "Revisión de instalaciones, condiciones inseguras "
        "y oportunidades de mejora."
    ),
    "Investigación de accidentes": (
        "Análisis de causas de accidentes e incidentes "
        "y establecimiento de medidas correctivas."
    ),
    "Gestión documental SST": (
        "Organización de registros, procedimientos, matrices "
        "y documentos de seguridad ocupacional."
    ),
    "Planes de emergencia": (
        "Desarrollo de protocolos de evacuación, brigadas, "
        "simulacros y respuesta ante emergencias."
    ),
    "Ergonomía y riesgo psicosocial": (
        "Evaluación de condiciones ergonómicas y factores "
        "que afectan el bienestar de los trabajadores."
    ),
}

TODOS_LOS_SERVICIOS = {
    "Contabilidad y tributación": list(SERVICIOS_CONTABLES.keys()),
    "Seguridad y salud ocupacional": list(SERVICIOS_SST.keys()),
    "Solución integral": [
        "Diagnóstico integral SBPR",
        "Acompañamiento mensual integral",
        "Propuesta personalizada",
    ],
}


# =========================================================
# FUNCIONES
# =========================================================

def crear_url_whatsapp(mensaje: str) -> str:
    """Construye el enlace de WhatsApp con el mensaje preparado."""
    return (
        f"https://wa.me/{WHATSAPP_NUMBER}"
        f"?text={quote(mensaje)}"
    )


def mostrar_imagen(ruta: Path, texto_alternativo: str) -> None:
    """Muestra una imagen únicamente cuando el archivo existe."""
    if ruta.exists():
        st.image(
            str(ruta),
            caption=texto_alternativo,
            use_container_width=True,
        )
    else:
        st.info(
            f"Puedes agregar la imagen en: assets/{ruta.name}"
        )


def mostrar_tarjetas_servicios(servicios: dict[str, str]) -> None:
    """Presenta los servicios en tarjetas distribuidas en columnas."""
    nombres = list(servicios.keys())

    for posicion in range(0, len(nombres), 3):
        columnas = st.columns(3)

        for columna, nombre in zip(
            columnas,
            nombres[posicion:posicion + 3],
        ):
            with columna:
                with st.container(border=True):
                    st.subheader(nombre)
                    st.write(servicios[nombre])
                    st.caption("✓ Atención personalizada")


def encabezado_seccion(
    etiqueta: str,
    titulo: str,
    descripcion: str,
) -> None:
    st.caption(etiqueta.upper())
    st.header(titulo)
    st.write(descripcion)


def cambiar_pagina(nombre: str) -> None:
    st.session_state["pagina_actual"] = nombre


# =========================================================
# ESTADO DE LA APLICACIÓN
# =========================================================

if "pagina_actual" not in st.session_state:
    st.session_state["pagina_actual"] = "Inicio"

if "consulta_url" not in st.session_state:
    st.session_state["consulta_url"] = ""


# =========================================================
# BARRA LATERAL
# =========================================================

with st.sidebar:

    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), use_container_width=True)
    else:
        st.title("SBPR")
        st.caption("ACCOUNTING & CONTROL")

    st.divider()

    pagina = st.radio(
        "Navegación",
        [
            "Inicio",
            "Servicios contables",
            "Seguridad y salud",
            "Diagnóstico",
            "Contacto",
        ],
        key="pagina_actual",
    )

    st.divider()

    st.subheader("Atención directa")

    mensaje_general = (
        "Hola SBPR, deseo recibir información "
        "sobre sus servicios."
    )

    st.link_button(
        "💬 Abrir WhatsApp",
        crear_url_whatsapp(mensaje_general),
        type="primary",
        width="stretch",
    )

    st.link_button(
        "✉️ Enviar correo",
        f"mailto:{EMAIL}?subject=Consulta%20de%20servicios%20SBPR",
        width="stretch",
    )

    st.caption("Quito · Ecuador")
    st.caption("099 532 8482")


# =========================================================
# PÁGINA DE INICIO
# =========================================================

if pagina == "Inicio":

    columna_texto, columna_logo = st.columns(
        [1.4, 0.6],
        vertical_alignment="center",
    )

    with columna_texto:
        st.caption(
            "CONTABILIDAD · CONTROL · PREVENCIÓN"
        )

        st.title(
            "Tu empresa en orden, tu equipo protegido "
            "y tus decisiones bajo control."
        )

        st.write(
            """
            **SBPR Accounting & Control** ofrece soluciones para
            personas naturales, emprendedores, PYMES y empresas.

            Integramos servicios contables, tributarios,
            administrativos y de seguridad y salud ocupacional
            para reducir riesgos, prevenir multas y fortalecer
            la gestión empresarial.
            """
        )

        boton_1, boton_2 = st.columns(2)

        with boton_1:
            if st.button(
                "📊 Conocer servicios contables",
                type="primary",
                width="stretch",
            ):
                cambiar_pagina("Servicios contables")
                st.rerun()

        with boton_2:
            if st.button(
                "🛡️ Conocer servicios SST",
                width="stretch",
            ):
                cambiar_pagina("Seguridad y salud")
                st.rerun()

    with columna_logo:
        if LOGO_PATH.exists():
            st.image(str(LOGO_PATH), use_container_width=True)
        else:
            with st.container(border=True):
                st.title("SBPR")
                st.subheader("Accounting & Control")
                st.caption(
                    "Orden · Cumplimiento · Protección"
                )

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
            "Atención",
            "Personalizada",
            "Según cada necesidad",
        )

    with metrica_3:
        st.metric(
            "Cobertura",
            "Ecuador",
            "Atención presencial y remota",
        )

    with metrica_4:
        st.metric(
            "Contacto",
            "Directo",
            "WhatsApp y correo",
        )

    st.divider()

    encabezado_seccion(
        "Unidades de servicio",
        "Dos áreas especializadas, una misma visión de control",
        (
            "Selecciona la solución que necesita tu negocio "
            "o combina ambas áreas."
        ),
    )

    contabilidad, seguridad = st.columns(2)

    with contabilidad:
        with st.container(border=True):
            st.subheader("📊 Contabilidad y tributación")

            st.write(
                """
                Para personas naturales y empresas que necesitan:

                - Cumplir correctamente con el SRI.
                - Organizar su información financiera.
                - Controlar inventarios y bancos.
                - Mejorar sus procesos administrativos.
                - Tomar decisiones con información confiable.
                """
            )

            st.progress(100)

            if st.button(
                "Explorar contabilidad",
                key="inicio_contabilidad",
                width="stretch",
            ):
                cambiar_pagina("Servicios contables")
                st.rerun()

    with seguridad:
        with st.container(border=True):
            st.subheader(
                "🛡️ Seguridad y salud ocupacional"
            )

            st.write(
                """
                Para empresas que necesitan:

                - Prevenir accidentes e incidentes.
                - Identificar riesgos laborales.
                - Cumplir las obligaciones de SST.
                - Capacitar a sus trabajadores.
                - Prepararse para emergencias.
                """
            )

            st.progress(100)

            if st.button(
                "Explorar seguridad y salud",
                key="inicio_sst",
                width="stretch",
            ):
                cambiar_pagina("Seguridad y salud")
                st.rerun()

    st.divider()

    st.subheader("Nuestro método de trabajo")

    paso_1, paso_2, paso_3, paso_4 = st.columns(4)

    with paso_1:
        with st.container(border=True):
            st.title("01")
            st.subheader("Escuchamos")
            st.write(
                "Conocemos tu actividad, necesidad y objetivo."
            )

    with paso_2:
        with st.container(border=True):
            st.title("02")
            st.subheader("Diagnosticamos")
            st.write(
                "Identificamos riesgos, brechas y prioridades."
            )

    with paso_3:
        with st.container(border=True):
            st.title("03")
            st.subheader("Implementamos")
            st.write(
                "Ejecutamos soluciones con acciones claras."
            )

    with paso_4:
        with st.container(border=True):
            st.title("04")
            st.subheader("Acompañamos")
            st.write(
                "Realizamos seguimiento y mejora continua."
            )

    st.divider()

    st.info(
        "SBPR busca convertir obligaciones y riesgos "
        "en acciones claras para tu empresa."
    )


# =========================================================
# SERVICIOS CONTABLES
# =========================================================

elif pagina == "Servicios contables":

    encabezado_seccion(
        "Unidad financiera",
        "Servicios contables y tributarios",
        (
            "Organizamos tu información financiera para que "
            "cumplas, controles tu negocio y tomes mejores decisiones."
        ),
    )

    izquierda, derecha = st.columns(
        [1, 1],
        vertical_alignment="center",
    )

    with izquierda:
        mostrar_imagen(
            CONTABILIDAD_IMAGE,
            "Servicios contables y tributarios SBPR",
        )

    with derecha:
        st.subheader(
            "Tu tranquilidad financiera empieza con orden"
        )

        st.write(
            """
            Nuestro enfoque combina cumplimiento tributario,
            organización documental y análisis financiero.

            No se trata únicamente de presentar declaraciones.
            Se trata de ayudarte a comprender qué ocurre con
            tus ingresos, gastos, obligaciones y liquidez.
            """
        )

        st.success(
            "Cumplimiento + control + información para decidir."
        )

        if st.button(
            "Solicitar diagnóstico contable",
            type="primary",
            width="stretch",
        ):
            cambiar_pagina("Diagnóstico")
            st.session_state["area_preseleccionada"] = (
                "Contabilidad y tributación"
            )
            st.rerun()

    st.divider()

    mostrar_tarjetas_servicios(SERVICIOS_CONTABLES)

    st.divider()

    st.subheader("Beneficios para el cliente")

    beneficio_1, beneficio_2, beneficio_3 = st.columns(3)

    with beneficio_1:
        st.success("✅ Menor riesgo de multas")
        st.write(
            "Control de obligaciones, vencimientos "
            "y documentación."
        )

    with beneficio_2:
        st.info("📈 Mejores decisiones")
        st.write(
            "Información financiera clara para dirigir "
            "el negocio."
        )

    with beneficio_3:
        st.warning("💰 Mayor control")
        st.write(
            "Visibilidad de inventarios, bancos, "
            "gastos y flujo de caja."
        )


# =========================================================
# SEGURIDAD Y SALUD OCUPACIONAL
# =========================================================

elif pagina == "Seguridad y salud":

    encabezado_seccion(
        "Unidad preventiva",
        "Seguridad y salud ocupacional",
        (
            "Soluciones prácticas para prevenir riesgos, "
            "cumplir la normativa y proteger a tu equipo."
        ),
    )

    izquierda, derecha = st.columns(
        [1, 1],
        vertical_alignment="center",
    )

    with izquierda:
        st.subheader(
            "Cumplir, prevenir y proteger"
        )

        st.write(
            """
            Diseñamos herramientas adaptadas a la actividad,
            tamaño y realidad operativa de cada empresa.

            El objetivo es fortalecer el control preventivo,
            reducir incidentes y construir una cultura
            de seguridad sostenible.
            """
        )

        st.success(
            "Prevención + cumplimiento + protección."
        )

        if st.button(
            "Solicitar diagnóstico SST",
            type="primary",
            width="stretch",
        ):
            cambiar_pagina("Diagnóstico")
            st.session_state["area_preseleccionada"] = (
                "Seguridad y salud ocupacional"
            )
            st.rerun()

    with derecha:
        mostrar_imagen(
            SST_IMAGE,
            "Servicios de seguridad y salud ocupacional",
        )

    st.divider()

    mostrar_tarjetas_servicios(SERVICIOS_SST)

    st.divider()

    st.subheader("Resultados que buscamos")

    resultado_1, resultado_2, resultado_3, resultado_4 = (
        st.columns(4)
    )

    with resultado_1:
        st.metric(
            "Cumplimiento",
            "Normativo",
            "Documentación organizada",
        )

    with resultado_2:
        st.metric(
            "Prevención",
            "Activa",
            "Identificación de riesgos",
        )

    with resultado_3:
        st.metric(
            "Respuesta",
            "Preparada",
            "Planes de emergencia",
        )

    with resultado_4:
        st.metric(
            "Cultura",
            "Segura",
            "Capacitación del personal",
        )


# =========================================================
# DIAGNÓSTICO
# =========================================================

elif pagina == "Diagnóstico":

    encabezado_seccion(
        "Consulta personalizada",
        "Solicita un diagnóstico inicial",
        (
            "Completa la información y la aplicación preparará "
            "un mensaje para enviarlo por WhatsApp."
        ),
    )

    st.info(
        "La información ingresada no se guarda en esta "
        "aplicación. Solo se utiliza para preparar el mensaje."
    )

    area_inicial = st.session_state.pop(
        "area_preseleccionada",
        "Contabilidad y tributación",
    )

    opciones_area = list(TODOS_LOS_SERVICIOS.keys())

    indice_inicial = (
        opciones_area.index(area_inicial)
        if area_inicial in opciones_area
        else 0
    )

    area = st.radio(
        "Selecciona el área de interés",
        opciones_area,
        index=indice_inicial,
        horizontal=True,
    )

    servicios_disponibles = TODOS_LOS_SERVICIOS[area]

    with st.form(
        "formulario_consulta",
        clear_on_submit=False,
        border=True,
    ):

        nombre, cliente = st.columns(2)

        with nombre:
            nombre_empresa = st.text_input(
                "Nombre o empresa",
                placeholder="Ej.: María Pérez / Empresa ABC",
            )

        with cliente:
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
            servicios_disponibles,
        )

        urgencia = st.select_slider(
            "Prioridad de la consulta",
            options=[
                "Informativa",
                "Normal",
                "Importante",
                "Urgente",
            ],
            value="Normal",
        )

        detalle = st.text_area(
            "Describe brevemente tu necesidad",
            placeholder=(
                "Ej.: Necesito revisar mis obligaciones "
                "tributarias pendientes."
            ),
            height=130,
        )

        enviar = st.form_submit_button(
            "Preparar mensaje para WhatsApp",
            type="primary",
            width="stretch",
        )

    if enviar:

        if not nombre_empresa.strip():
            st.error(
                "Escribe tu nombre o el nombre de la empresa."
            )

        else:
            mensaje = (
                "Hola SBPR, deseo solicitar información.\n\n"
                f"Nombre / empresa: {nombre_empresa.strip()}\n"
                f"Tipo de cliente: {tipo_cliente}\n"
                f"Área: {area}\n"
                f"Servicio: {servicio}\n"
                f"Prioridad: {urgencia}\n"
                f"Detalle: {detalle.strip() or 'Sin detalle adicional'}\n\n"
                "Por favor, indíquenme cómo podemos "
                "coordinar una consulta."
            )

            st.session_state["consulta_url"] = (
                crear_url_whatsapp(mensaje)
            )

            st.success(
                "Mensaje preparado correctamente."
            )

    if st.session_state["consulta_url"]:
        st.link_button(
            "💬 Enviar ahora por WhatsApp",
            st.session_state["consulta_url"],
            type="primary",
            width="stretch",
        )

    st.divider()

    st.subheader("Diagnóstico express")

    st.caption(
        "Orientación preliminar. No reemplaza una revisión profesional."
    )

    diagnostico_1, diagnostico_2 = st.columns(2)

    with diagnostico_1:
        obligaciones_pendientes = st.selectbox(
            "¿Tienes obligaciones o documentos pendientes?",
            [
                "No estoy seguro",
                "No",
                "Sí, algunos",
                "Sí, varios",
            ],
        )

        procesos_ordenados = st.selectbox(
            "¿Tus procesos están documentados?",
            [
                "No estoy seguro",
                "Sí",
                "Parcialmente",
                "No",
            ],
        )

    with diagnostico_2:
        reportes_disponibles = st.selectbox(
            "¿Cuentas con reportes o indicadores?",
            [
                "No estoy seguro",
                "Sí",
                "Algunos",
                "No",
            ],
        )

        controles_actualizados = st.selectbox(
            "¿Tus controles se revisan periódicamente?",
            [
                "No estoy seguro",
                "Sí",
                "Ocasionalmente",
                "No",
            ],
        )

    if st.button(
        "Evaluar situación",
        width="stretch",
    ):
        respuestas_criticas = {
            "Sí, varios",
            "No",
        }

        respuestas_intermedias = {
            "Sí, algunos",
            "Parcialmente",
            "Algunos",
            "Ocasionalmente",
            "No estoy seguro",
        }

        respuestas = [
            obligaciones_pendientes,
            procesos_ordenados,
            reportes_disponibles,
            controles_actualizados,
        ]

        puntaje = 0

        for respuesta in respuestas:
            if respuesta in respuestas_criticas:
                puntaje += 2
            elif respuesta in respuestas_intermedias:
                puntaje += 1

        if puntaje >= 6:
            st.error(
                "Prioridad alta: conviene realizar un "
                "diagnóstico integral."
            )

        elif puntaje >= 3:
            st.warning(
                "Prioridad media: existen áreas que deberían "
                "revisarse y organizarse."
            )

        else:
            st.success(
                "Situación inicial favorable. Se recomienda "
                "mantener revisiones periódicas."
            )


# =========================================================
# CONTACTO
# =========================================================

elif pagina == "Contacto":

    encabezado_seccion(
        "Atención directa",
        "Hablemos de tu empresa",
        (
            "Coordina una consulta sobre contabilidad, "
            "tributación o seguridad y salud ocupacional."
        ),
    )

    contacto_1, contacto_2, contacto_3 = st.columns(3)

    with contacto_1:
        with st.container(border=True):
            st.title("💬")
            st.subheader("WhatsApp")
            st.write("099 532 8482")

            st.link_button(
                "Abrir conversación",
                crear_url_whatsapp(
                    "Hola SBPR, deseo agendar una consulta."
                ),
                type="primary",
                width="stretch",
            )

    with contacto_2:
        with st.container(border=True):
            st.title("✉️")
            st.subheader("Correo")
            st.write(EMAIL)

            st.link_button(
                "Enviar correo",
                (
                    f"mailto:{EMAIL}"
                    "?subject=Consulta%20de%20servicios%20SBPR"
                ),
                width="stretch",
            )

    with contacto_3:
        with st.container(border=True):
            st.title("📍")
            st.subheader("Ubicación")
            st.write("Quito, Ecuador")
            st.write(
                "Atención a personas naturales, "
                "PYMES y empresas."
            )

    st.divider()

    st.subheader("¿Qué puedes consultar?")

    tab_contable, tab_sst = st.tabs(
        [
            "📊 Contabilidad",
            "🛡️ Seguridad y salud",
        ]
    )

    with tab_contable:
        st.write(
            """
            - Declaraciones tributarias.
            - Obligaciones pendientes.
            - Contabilidad mensual.
            - Control de inventarios.
            - Reportes financieros.
            - Procesos administrativos.
            """
        )

    with tab_sst:
        st.write(
            """
            - Diagnóstico legal.
            - Matrices de riesgos.
            - Planes de prevención.
            - Capacitaciones.
            - Inspecciones.
            - Planes de emergencia.
            """
        )


# =========================================================
# PIE DE PÁGINA
# =========================================================

st.divider()

pie_1, pie_2 = st.columns([2, 1])

with pie_1:
    st.caption(
        "SBPR ACCOUNTING & CONTROL · "
        "Orden, cumplimiento y protección."
    )

with pie_2:
    st.caption(
        "Quito · Ecuador · 099 532 8482"
    )