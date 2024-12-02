from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
Screen:

    MDCard:
        orientation: "vertical"
        size_hint: None, None
        size: "320dp", "120dp"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 4
        padding: "8dp"

        BoxLayout:
            orientation: "horizontal"
            spacing: "8dp"

            MDIcon:
                icon: "file-outline"
                size_hint: None, None
                size: "48dp", "48dp"
                theme_text_color: "Primary"

            BoxLayout:
                orientation: "vertical"
                spacing: "4dp"

                MDLabel:
                    text: "Physics Form 4 chanco.pdf"
                    theme_text_color: "Primary"
                    font_style: "H6"

                MDLabel:
                    text: "Size: 1.2 MB"
                    theme_text_color: "Secondary"
                    font_style: "Caption"

        MDSeparator:
            height: "1dp"

        MDBoxLayout:
            adaptive_height: True
            padding: "8dp"
            spacing: "8dp"

            MDRaisedButton:
                text: "Open"
                on_release: app.open_file()

            MDRaisedButton:
                text: "Delete"
                on_release: app.delete_file()
'''

class FileCardApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def open_file(self):
        print("Open file action triggered!")

    def delete_file(self):
        print("Delete file action triggered!")

if __name__ == "__main__":
    FileCardApp().run()