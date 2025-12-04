import flet as ft
import random

def main(page: ft.Page):
    page.title = "Jogo da Velha - Aluno Glauber Ulisses Oliveira Silva"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window.width = 850
    page.window.height = 680
    page.window.resizable = False

    plPlayer = 0
    plBot = 0

    txt1 = ft.Text("", size=140, weight=ft.FontWeight.BOLD)
    txt2 = ft.Text("", size=140, weight=ft.FontWeight.BOLD)
    txt3 = ft.Text("", size=140, weight=ft.FontWeight.BOLD)
    txt4 = ft.Text("", size=140, weight=ft.FontWeight.BOLD)
    txt5 = ft.Text("", size=140, weight=ft.FontWeight.BOLD)
    txt6 = ft.Text("", size=140, weight=ft.FontWeight.BOLD)
    txt7 = ft.Text("", size=140, weight=ft.FontWeight.BOLD)
    txt8 = ft.Text("", size=140, weight=ft.FontWeight.BOLD)
    txt9 = ft.Text("", size=140, weight=ft.FontWeight.BOLD)

    dlg_ganhador = ft.AlertDialog(
        modal=True,
        title=ft.Text("🎉Parabens!"),
        content=ft.Column([
            ft.Row([ft.Text(f"O Jogador Ganhou", weight=ft.FontWeight.BOLD, size=30)], alignment=ft. MainAxisAlignment.CENTER),
            ft.Row([ft.ElevatedButton("Jogar Novamente?", on_click=lambda e: page.close(dlg_ganhador))], alignment=ft. MainAxisAlignment.CENTER),
        ], height=70),
        alignment=ft.alignment.center,
        on_dismiss=lambda e: print("Dialog dismissed!"),)

    dlg_perdeu = ft.AlertDialog(
        modal=True,
        title=ft.Text("Que Pena!"),
        content=ft.Text(f"O BOT Ganhou"),
        alignment=ft.alignment.center,
        on_dismiss=lambda e: print("Dialog dismissed!"),
    )


    def verif_result():
        nonlocal plPlayer
        #------ VITORIAS DO PLAYER ------------------------
        if txt1.value == "X" and txt2.value  == "X" and txt3.value == "X":
            plPlayer =+ 1
            page.update()
            page.open(dlg_ganhador)

        elif txt4.value == "X" and txt5.value == "X" and txt6.value == "X":
            plPlayer =+ 1
            page.update()
            page.open(dlg_ganhador)

        elif txt7.value == "X" and txt8.value == "X" and txt9.value == "X":
            plPlayer =+ 1
            page.update()
            page.open(dlg_ganhador)

        # ---------------------------------------------------

        elif txt1.value == "X" and txt4.value == "X" and txt7.value == "X":
            plPlayer =+ 1
            page.update()
            page.open(dlg_ganhador)

        elif txt2.value == "X" and txt5.value == "X" and txt8.value == "X":
            plPlayer =+ 1
            page.update()
            page.open(dlg_ganhador)

        elif txt3.value == "X" and txt6.value == "X" and txt9.value == "X":
            plPlayer =+ 1
            page.update()
            page.open(dlg_ganhador)


        #---------------------------------------------------

        elif txt1.value == "X" and txt5.value == "X" and txt9.value == "X":
            plPlayer =+ 1
            page.update()
            page.open(dlg_ganhador)

        elif txt3.value == "X" and txt5.value == "X" and txt7.value == "X":
            plPlayer =+ 1
            page.update()
            page.open(dlg_ganhador)

        # ------ VITORIAS DO BOT ------------------------
        elif txt1.value == "O" and txt2.value == "O" and txt3.value == "O":
            plPlayer =+ 1
            page.update()
            page.open(dlg_perdeu)

        elif txt4.value == "O" and txt5.value == "O" and txt6.value == "0":
            plPlayer =+ 1
            page.update()
            page.open(dlg_perdeu)

        elif txt7.value == "O" and txt8.value == "O" and txt9.value == "0":
            plPlayer =+ 1
            page.update()
            page.open(dlg_perdeu)

        # ---------------------------------------------------

        elif txt1.value == "O" and txt4.value == "O" and txt7.value == "0":
            plPlayer = plPlayer + 1
            page.update()
            page.open(dlg_perdeu)

        elif txt2.value == "O" and txt5.value == "O" and txt8.value == "0":
            plPlayer = plPlayer + 1
            page.update()
            page.open(dlg_perdeu)

        elif txt3.value == "O" and txt6.value == "O" and txt9.value == "0":
            plPlayer = plPlayer + 1
            page.update()
            page.open(dlg_perdeu)

        # ---------------------------------------------------

        elif txt1.value == "O" and txt5.value == "O" and txt9.value == "0":
            plPlayer = plPlayer + 1
            page.update()
            page.open(dlg_perdeu)

        elif txt3.value == "O" and txt5.value == "O" and txt7.value == "0":
            plPlayer = plPlayer + 1
            page.update()
            page.open(dlg_perdeu)

        # ------------------------------------------------------

        else:
            print("Empate")

    pos = [txt1, txt2, txt3, txt4, txt5, txt6, txt7, txt8, txt9]

    def escolha(esc):
        if esc.value == "X":
            pass
        elif esc.value == "O":
            pass
        else:
            esc.value = "X"
            page.update()
            pos.remove(esc)

            escolhaBot = random.choice(pos)
            escolhaBot.value = "O"
            pos.remove(escolhaBot)
            page.update()
            #print(pos)
        verif_result()

    page.add(
        ft.Row([

            ft.Container(
                content=ft.Column([

                    ft.Row([ft.Text("Jogo da Velha", size=25, weight=ft.FontWeight.BOLD), ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Divider(),

                    #ft.Row([ft.Text(" "), ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([ft.Icon(name=ft.Icons.LEADERBOARD),ft.Text("Placar", size=20), ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([ft.Text(" "), ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([ft.Text(" "), ], alignment=ft.MainAxisAlignment.CENTER),

                    ft.Row([ft.Icon(name=ft.Icons.PERSON),ft.Text(f"Player: {plPlayer}", size=20), ]),
                    ft.Row([ft.Icon(name=ft.Icons.BLUR_CIRCULAR),ft.Text(f"BOT: {plBot}", size=20), ]),

                    ft.Row([ft.Text(" "), ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([ft.Text(" ") ], height=250, alignment=ft.MainAxisAlignment.CENTER),

                    ft.Row([ft.Image(src="https://www.se.senai.br/assets/img/logo.png", width=180)]),

                ]),
                width=200,
                # height = 200,
                #bgcolor="blue",
                border_radius=10,
                padding=10,

            ),

            ft.Column([
                ft.Container(
                    content=txt1,
                    width=200,
                    height=200,
                    bgcolor="red",
                    alignment=ft.alignment.center,
                    on_click=lambda e: escolha(txt1),
                ),
                ft.Container(
                    content=txt2,
                    width=200,
                    height=200,
                    bgcolor="red",
                    alignment=ft.alignment.center,
                    on_click=lambda e: escolha(txt2),
                ),
                ft.Container(
                    content=txt3,
                    width=200,
                    height=200,
                    bgcolor="red",
                    alignment=ft.alignment.center,
                    on_click=lambda e: escolha(txt3),
                ),
            ], expand=True),

            ft.Column([
                ft.Container(
                    content=txt4,
                    width=200,
                    height=200,
                    bgcolor="red",
                    alignment=ft.alignment.center,
                    on_click=lambda e: escolha(txt4),
                ),
                ft.Container(
                    content=txt5,
                    width=200,
                    height=200,
                    bgcolor="red",
                    alignment=ft.alignment.center,
                    on_click=lambda e: escolha(txt5),
                ),
                ft.Container(
                    content=txt6,
                    width=200,
                    height=200,
                    bgcolor="red",
                    alignment=ft.alignment.center,
                    on_click=lambda e: escolha(txt6),
                ),
            ], expand=True),

            ft.Column([
                ft.Container(
                    content=txt7,
                    width=200,
                    height=200,
                    bgcolor="red",
                    alignment=ft.alignment.center,
                    on_click=lambda e: escolha(txt7),
                ),
                ft.Container(
                    content=txt8,
                    width=200,
                    height=200,
                    bgcolor="red",
                    alignment=ft.alignment.center,
                    on_click=lambda e: escolha(txt8),
                ),
                ft.Container(
                    content=txt9,
                    width=200,
                    height=200,
                    bgcolor="red",
                    alignment=ft.alignment.center,
                    on_click=lambda e: escolha(txt9),
                ),
            ], expand=True),
        ], expand=True)

    )

ft.app(main)