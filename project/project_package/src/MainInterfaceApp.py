from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition, CardTransition
from kivymd.app import MDApp
from kivy.properties import ObjectProperty, StringProperty, ListProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.list import OneLineIconListItem, MDList, TwoLineIconListItem, OneLineListItem, OneLineAvatarListItem
from kivymd.uix.picker import MDTimePicker
from project.project_package.src.package.User import User
from project.project_package.src.package.Species import Species

Window.size = (340, 630)


class MyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # tutaj mozna podpiąć baze
        self.species = None
        self.user = User("Ala")
        # rose = Species("rose", "rositina", 3, "Dużo wody, słońca i miłości <3",
        #                         "GUI/images/grootspecies.jpg", True)
        # tulip = Species("tulip", "tulipina", 7, "Dużo miłości <3",
        #                         "GUI/images/groot.jpg", True)
        # species = [tulip, rose]
        # for s in species:
        #     self.ids.species_catalog_screen.ids.species_list.add_widget(
        #         OneLineListItem(
        #             text=s.name,
        #         )
        #     )

        my_plants = ["stokrotka basia", "tulipan staszek", "róża rozalia", "kaktus kajtek"]

        for plant in my_plants:
            self.ids.my_plants_screen.ids.plants_list.add_widget(
                OneLineListItem(
                    text=plant,
                )
            )
        self.ids.user_screen.ids.user_photo.source = self.user.photo
        self.ids.user_screen.ids.user_name.text = self.user.nickname
        self.ids.user_screen.ids.lvl.text = "Your level:"+str(self.user.level.value)
        self.ids.user_screen.ids.plants_no.text = "You have: "+str(len(self.user.list_of_plants))+" plants"
        self.ids.user_screen.ids.time_from_kill.text = str(self.user.days_without_dead_plant)\
                                                       +" days without killing plants"


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DayScreen(Screen):
    pass


class SpeciesScreen(Screen):
    pass


class SpeciesCatalogScreen(Screen):
    pass


class PlantScreen(Screen):
    pass


class MyPlantsScreen(Screen):
    pass


class AddPlantScreen(Screen):
    pass


class MainScreen(Screen):
    pass


class UserScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class LoginDialog(FloatLayout):
    pass


class SignUpDialog(FloatLayout):
    pass

class PlantDialog(FloatLayout):
    pass


class MainApp(MDApp):
    dialog = None

    def __init__(self, **kwargs):
        super().__init__()
        self.user = User("Stokrotka")
        self.species = [Species("GROOT species", "NO SOY LATINA!", 3, "Dużo wody, słońca i miłości <3",
                                "GUI/images/grootspecies.jpg", True)]


    def build(self):
        self.theme_cls.primary_palette = 'LightGreen'
        Builder.load_file("KV/MainInterface.kv")

        return MyScreenManager()

    def on_start(self):
        for s in self.species:
            self.root.ids.species_catalog_screen.ids.species_list.add_widget(
                OneLineListItem(
                    text=s.name,
                    on_release=self.show_plant_dialog
                    # on_release=self.show_login_dialog()
                )
            )


    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    def get_time(self, instance, time):
        User.set_reminder_time(self.user, time)

    def show_alert_dialog(self, text_):
        if not self.dialog:
            self.dialog = MDDialog(
                text=text_
            )
            self.dialog.open()
            self.dialog = None

    def show_login_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=LoginDialog())
        self.dialog.open()
        self.dialog = None

    def show_sign_up_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=SignUpDialog())
        self.dialog.open()
        self.dialog = None

    def show_plant_dialog(self, onelinelistitem):
        if not self.dialog:
            self.dialog = MDDialog(
                type="custom",
                content_cls=PlantDialog())
        self.dialog.open()
        self.dialog = None


    def change_screen(self, screen_name, title, direction = 'None', mode=""):
        screen_manager = self.root.ids.screen_manager
        self.root.ids.toolbar.title = title

        if direction == 'None':
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return

        screen_manager.transition = CardTransition(direction=direction, mode=mode)
        screen_manager.current = screen_name


if __name__ == '__main__':
    MainApp().run()
