import os
import tkinter as tk
from tkinter import filedialog
from datetime import datetime
import flet as ft
from flet import Colors, Icons
from procesador import procesar_reporte

def construir_interfaz(page: ft.Page):
    page.window.width = 500
    page.window.height = 560
    page.window.resizable = False
    page.window.icon = "/favicon.ico"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    imagen_local = ft.Image(
        src=r"/icon_report-wsp.png",
        width=90,
        height=90,
        margin=ft.Margin(left=0, top=20, right=0, bottom=-14),
        border_radius=8,
        fit="contain",
    )

    page.add(
        ft.Column(
            [imagen_local],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
    page.title = "Generador de Reportes de WhatsApp"

    ruta_archivo = {"txt": None}

    titulo = ft.Text(
        "Generador de Reportes de WhatsApp",
        size=22,
        weight=ft.FontWeight.BOLD
    )
    descripcion = ft.Text(
        "Convierte los chats exportados de WhatsApp en reportes formales de Excel.",
        size=13,
        color=Colors.GREY_700,
        text_align=ft.TextAlign.CENTER,
    )
    etiqueta_archivo = ft.Text(
        "Archivo seleccionado:",
        size=12,
        weight=ft.FontWeight.W_500,
        color=Colors.GREY_700,
        visible=False,
    )
    texto_archivo = ft.Text(
        "Ningún archivo seleccionado",
        size=13,
        italic=True,
        color=Colors.GREY_600
    )
    barra = ft.ProgressBar(
        width=340,
        visible=False,
        color=Colors.GREEN_700
    )
    mensaje_estado = ft.Text(
        "",
        size=13,
        text_align=ft.TextAlign.CENTER,
        max_lines=2,
    )
    
    def abrir_explorador(e):
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        
        ruta = filedialog.askopenfilename(
            title="Selecciona el archivo TXT de WhatsApp",
            filetypes=[("Archivos de texto", "*.txt")]
        )
        root.destroy()

        if ruta:
            ruta_archivo["txt"] = ruta
            
            etiqueta_archivo.visible = True

            texto_archivo.value = f"📄 {os.path.basename(ruta)}"
            texto_archivo.italic = False
            texto_archivo.weight = ft.FontWeight.BOLD
            texto_archivo.color = Colors.GREEN_900

            btn_procesar.disabled = False
            mensaje_estado.value = ""
            page.update()

    def iniciar_procesamiento(e):
        if not ruta_archivo["txt"]:
            return

        dias = ["Lun", "Mar", "Mie", "Jue", "Vie", "Sáb", "Dom"]
        meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Set", "Oct", "Nov", "Dic"]
        ahora = datetime.now()
        dia_sem = dias[ahora.weekday()]
        mes_nom = meses[ahora.month - 1]
        nombre_defecto = f"{ahora.strftime('%d')} {dia_sem} {mes_nom} {ahora.strftime('%y')} - Reporte de Monitoreo de Cámaras.xlsx"

        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        
        ruta_excel = filedialog.asksaveasfilename(
            title="Guardar reporte como...",
            initialfile=nombre_defecto,
            defaultextension=".xlsx",
            filetypes=[("Archivos Excel", "*.xlsx")]
        )
        root.destroy()

        if not ruta_excel:
            mensaje_estado.value = "Operación cancelada: no se eligió destino."
            mensaje_estado.color = Colors.AMBER_900
            page.update()
            return

        btn_seleccionar.disabled = True
        btn_procesar.disabled = True
        barra.visible = True
        mensaje_estado.value = "Leyendo mensajes y estructurando datos..."
        mensaje_estado.color = Colors.GREEN_800
        page.update()

        try:
            total_filas, ruta_final = procesar_reporte(ruta_archivo["txt"], ruta_excel)
            
            barra.visible = False
            if total_filas > 0:
                mensaje_estado.value = f"¡Éxito!\nSe generó el reporte de monitoreo de cámaras con {total_filas} filas"
                mensaje_estado.color = Colors.GREEN_700
                mensaje_estado.weight=ft.FontWeight.BOLD
            else:
                mensaje_estado.value = "⚠️ No se encontraron mensajes válidos de monitoreo."
                mensaje_estado.color = Colors.AMBER_900
                mensaje_estado.weight=ft.FontWeight.BOLD

        except Exception as ex:
            barra.visible = False
            mensaje_estado.value = f"Error durante el proceso: {ex}"
            mensaje_estado.color = Colors.RED_700
            mensaje_estado.weight=ft.FontWeight.BOLD

        btn_seleccionar.disabled = False
        btn_procesar.disabled = False
        page.update()

    def abrir_dialogo(e):
        dialogo_acerca.open = True
        page.update()

    def cerrar_dialogo(e):
        dialogo_acerca.open = False
        page.update()

    dialogo_acerca = ft.AlertDialog(
        title=ft.Text(
            "Generador de Reportes de WhatsApp",
            weight=ft.FontWeight.BOLD,
            text_align=ft.TextAlign.CENTER,
            size=19,
        ),
        content=ft.Column(
            [
                ft.Text(
                    spans=[
                        ft.TextSpan("Desarrollado por:", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                        ft.TextSpan(" Alexander Jesus Laura Julca"),
                    ],
                ),
                ft.Text(
                    spans=[
                        ft.TextSpan("Área:", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                        ft.TextSpan(" Tecnologías de la Información (TI)"),
                    ],
                ),
                ft.Text(
                    spans=[
                        ft.TextSpan("Versión:", style=ft.TextStyle(weight=ft.FontWeight.BOLD)),
                        ft.TextSpan(" 1.4.5"),
                    ],
                ),
                ft.Divider(height=10, color=ft.Colors.TRANSPARENT),
                ft.Row(
                    [
                        ft.Text(
                            "© 2026 Generador de Reportes. Todos los derechos reservados.",
                            size=11,
                            color=ft.Colors.GREY_600,
                            italic=True,
                            text_align=ft.TextAlign.CENTER,
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            tight=True,
            spacing=4,
        ),
        actions=[
            ft.TextButton("Aceptar", on_click=cerrar_dialogo),
        ],
    )

    page.overlay.append(dialogo_acerca)

    link_acerca_de = ft.Container(
        content=ft.Text(
            "Acerca de",
            size=12,
            color=ft.Colors.GREY_600,
            style=ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
        ),
        on_click=abrir_dialogo,
        ink=True,
        padding=6,
        margin=ft.Margin.only(top=15),
    )

    btn_seleccionar = ft.OutlinedButton(
        "Subir TXT",
        icon=Icons.FOLDER_OPEN,
        icon_color=Colors.GREEN_700,
        on_click=abrir_explorador,
        width=160,
        style=ft.ButtonStyle(
            color={
                "hovered": Colors.GREEN_900,
                "": Colors.GREEN_800,
            },
            side={
                "hovered": ft.BorderSide(1.5, Colors.GREEN_700),
                "": ft.BorderSide(1.2, Colors.GREEN_800),
            },
            bgcolor={
                "hovered": Colors.GREEN_50,
                "": Colors.TRANSPARENT,
            },
            overlay_color=Colors.TRANSPARENT,
        ),
    )

    btn_procesar = ft.ElevatedButton(
        "Generar Reporte",
        icon=Icons.ASSESSMENT,
        on_click=iniciar_procesamiento,
        disabled=True,
        width=180,
        style=ft.ButtonStyle(
            color=Colors.WHITE,
            bgcolor={
                "disabled": Colors.GREEN_300,
                "hovered": Colors.GREEN_500,
                "": Colors.GREEN_700,
            },
            elevation={"hovered": 4, "": 1},
            animation_duration=200,
        ),
    )

    fila_botones = ft.Row([btn_seleccionar, btn_procesar], alignment=ft.MainAxisAlignment.CENTER, spacing=15)

    page.add(
        ft.Container(
            content=ft.Column(
                [
                    titulo,
                    descripcion,
                    ft.Divider(height=15, color=Colors.TRANSPARENT),
                    etiqueta_archivo,
                    texto_archivo,
                    ft.Divider(height=10, color=Colors.TRANSPARENT),
                    fila_botones,
                    ft.Divider(height=15, color=Colors.TRANSPARENT),
                    barra,
                    mensaje_estado,
                    link_acerca_de,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            padding=20,
        )
    )