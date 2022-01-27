import PySimpleGUI as sg

import time
import threading


class Gui:
    window = None

    def ShowHide(self):
        isActive = False
        centerTextKey = "center-text"

        while True:
            self.window["far-right"].Update(visible=True if isActive else False)

            isActive = not isActive

            self.window["center-text"].update(
                "Inactive right panel" if isActive else "Active right panel"
            )

            time.sleep(5)

    def __init__(self):
        sg.theme("Topanga")  # Add a touch of color

        centered = [
            [sg.Text("Center text", key="center-text")],
        ]

        layout = [
            [
                sg.Text(key="-EXPAND-", font="ANY 1", pad=(0, 0))
            ],  # the thing that expands from top
            [
                sg.Text(
                    "", pad=(0, 0), key="-EXPAND2-"
                ),  # the thing that expands from left
                sg.Column(
                    centered,
                    vertical_alignment="center",
                    justification="center",
                    k="-C-",
                ),
                sg.Text(key="-EXPAND3-", font="ANY 2", pad=(0, 0)),
                sg.Column(
                    [
                        [
                            sg.Text("I am at the far right"),
                        ]
                    ],
                    vertical_alignment="center",
                    justification="right",
                    k="far-right",
                ),
            ],
        ]

        self.window = sg.Window(
            "Climate Controller",
            layout,
            element_justification="center",
            no_titlebar=True,
            location=(0, 0),
            size=(800, 450),
            # keep_on_top=True,
            finalize=True,
        )

        self.window["-C-"].expand(True, True, True)

        self.window["-EXPAND-"].expand(True, True, True)

        self.window["-EXPAND2-"].expand(True, False, True)

        self.window["-EXPAND3-"].expand(False, False, False)

        self.window["far-right"].Update(visible=False)

        self.window.Maximize()

        showHideThread = threading.Thread(target=self.ShowHide, name="Show Hide Thread")
        showHideThread.setDaemon(True)
        showHideThread.start()

        while True:

            event, values = self.window.read()

            if event == sg.WIN_CLOSED or event == "Exit":

                break

        self.window.close()
