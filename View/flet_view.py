import flet as ft
from NotesApp.Presenter.App import *

app = App()
def main(page: ft.Page):
    page.title = "Notes App"
    page.window_width = "640"
    page.window_height = "650"
    page.bgcolor = ft.colors.INDIGO_100
    BG = '#bcc0d2'
    FWG = '#4a5675'
    FG = '#415587'
    BC = '#8b96b1'
    WH = '#ffffff'
    BL = '#000000'

    notes = ft.Column(
        scroll="auto"
    )

    tb1 = ft.TextField(label="Название", width="350", bgcolor=WH, border_color=BG)
    tb2 = ft.TextField(label="Описание", width="350", bgcolor=WH,
                       multiline=True,
                       min_lines=4,
                       max_lines=4,
                       )
    info_text = ft.Text()

    def note_update():
        notes.controls.clear()
        for note in app.note_list.get_list():
            notes.controls.append(
                ft.Container(
                    width="295", height="30", bgcolor=BC, border_radius=14,
                    margin=ft.margin.symmetric(horizontal=5, vertical=5),
                    alignment=ft.alignment.center,
                    shadow=ft.BoxShadow(
                        blur_radius=5,
                        color=ft.colors.BLACK,
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    content=ft.Text(note.get_title())
                )
            )
    def button_clicked(e):
        info_text.value = f"{tb1.value}"
        page.update()

    def button_create(e):
        app.create_note(tb1.value, tb2.value)
        app.add_list()
        info_text.value = f"Заметка {tb1.value} создана"
        note_update()
        page.update()

    def button_edit(e):
        if app.note_list.check_note(tb1.value):
            note = app.note_list.get_note(tb1.value)
            descr = tb2.value
            note.set_description(descr)
            info_text.value = f"Заметка {tb1.value} изменена"
            page.update()
        else:
            info_text.value = f"Заметки {tb1.value} нет"
            page.update()

    def button_delete(e):
        if app.note_list.check_note(tb1.value):
            app.del_note(tb1.value)
            info_text.value = f"Заметка {tb1.value} удалена"
            note_update()
            page.update()
        else:
            info_text.value = f"Заметки {tb1.value} нет"
            page.update()

    def button_save(e):
        app.save_notes()
        info_text.value = f"Заметки сохранены"
        page.update()

    def button_load(e):
        app.read_from_csv()
        info_text.value = f"Заметки загружены"
        note_update()
        page.update()



    container = ft.Container(
        width="600", height="400",
        content=ft.Column(
            controls=[
                ft.Container(
                    width="600", height="250", bgcolor=FWG, padding=10, border_radius=10,
                    shadow=ft.BoxShadow(
                        blur_radius=5,
                        color=ft.colors.BLACK,
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    content=ft.Row(
                        controls=[
                            #Notes
                            ft.Container(
                                width="400", height="230", border_radius=5, padding=20,
                                content=ft.Column(
                                    controls=[
                                        tb1,
                                        tb2
                                    ]
                                )
                            ),
                            # Buttons
                            ft.Container(
                                width="170", height="230", border_radius=5, padding=6,
                                content=ft.Column(
                                    controls=[
                                        ft.ElevatedButton(text="Создать    ", bgcolor=BC,
                                                          on_click=button_create, width=200,
                                                          icon=ft.icons.FILE_DOWNLOAD_DONE_SHARP,
                                                          color=BL
                                                          ),
                                        ft.ElevatedButton(text="Изменить", bgcolor=BC,
                                                          on_click=button_edit, width=200,
                                                          icon=ft.icons.EDIT_NOTE, color=BL
                                                          ),
                                        ft.ElevatedButton(text="Удалить   ", bgcolor=BC,
                                                          on_click=button_delete, width=200,
                                                          icon=ft.icons.DELETE_SWEEP_OUTLINED,
                                                          color=BL
                                                          ),
                                        ft.ElevatedButton(text="Сохранить", bgcolor=BC,
                                                          on_click=button_save, width=200,
                                                          icon=ft.icons.FILE_DOWNLOAD_OUTLINED,
                                                          color=BL
                                                          ),
                                        ft.ElevatedButton(text="Загрузить ", bgcolor=BC,
                                                          on_click=button_load, width=200,
                                                          icon=ft.icons.FILE_UPLOAD_OUTLINED,
                                                          color=BL
                                                          ),
                                    ]
                                )
                            )
                        ]
                    )
                ),
                # Down
                ft.Container(
                    width="600", height="300", bgcolor=FWG, border_radius=10,
                    shadow=ft.BoxShadow(
                        blur_radius=5,
                        color=ft.colors.BLACK,
                        offset=ft.Offset(0, 0),
                        blur_style=ft.ShadowBlurStyle.OUTER,
                    ),
                    content=ft.Container(
                        width="600", height="300", padding=20,
                        content=ft.Row(
                            controls=[
                                # info
                                ft.Container(
                                    width="200", height="250", bgcolor=WH, border_radius=5, padding=10,
                                    content=info_text,
                                    shadow=ft.BoxShadow(
                                        spread_radius=2,
                                        color=ft.colors.BLUE_GREY_900,
                                    ),
                                ),
                                #Notes list
                                ft.Container(
                                    width="350", height="250", bgcolor=BG, border_radius=5, padding=20,
                                    content=notes,
                                    shadow=ft.BoxShadow(
                                        spread_radius=2,
                                        blur_radius=5,
                                        color=ft.colors.BLACK,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.OUTER,
                                    ),
                                ),
                            ]
                        )
                    )
                ),
                # Text App
                ft.Row(
                        spacing=4,
                        alignment="center",
                        controls=[
                            #title
                            ft.Column(
                                alignment="center",
                                horizontal_alignment="start",
                                controls=[
                                    ft.Text(
                                        "Notes App",
                                        weight="bold",
                                    )
                                ],
                            ),
                            ft.Column(
                                alignment="center",
                                horizontal_alignment="start",
                                controls=[
                                    ft.Text(
                                        "- Zandrex",
                                        weight="bold",
                                    )
                                ],
                            )
                        ]
                )
            ]
        )
    )

    page.add(container)

ft.app(target=main, assets_dir="assets")