from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
import requests
from kivy.properties import StringProperty
import webbrowser
from kivymd.uix.snackbar import Snackbar
from kivy.uix.label import Label
from kivy.network.urlrequest import UrlRequest
import certifi



class HomeScreen(Screen):
    pass


class MainApp(MDApp):
    name = StringProperty()
    category = StringProperty()
    area = StringProperty()
    image = StringProperty()
    url = StringProperty()

    def __init__(self,**kwargs):
        Window.size = (400,600)
        super().__init__(**kwargs)

    def on_start(self):
        url = 'https://www.themealdb.com/api/json/v1/1/random.php'
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error, ca_file=certifi.where())



    def success(self, UrlRequest, recipe):
        ingredient_list = self.root.ids['home'].ids['ingredient_list']


        self.name = recipe['meals'][0]['strMeal']
        self.category = recipe['meals'][0]['strCategory']
        self.area = recipe['meals'][0]['strArea']
        self.image = recipe['meals'][0]['strMealThumb']
        self.url = recipe['meals'][0]['strSource']
        for i in range(1,21):
            if recipe['meals'][0][f'strIngredient{i}'] != '':
                l = Label(text=recipe['meals'][0][f'strIngredient{i}'],color=(0,0,0,1))
                ingredient_list.add_widget(l)



    def error(self, urlrequest):
        print("error")
        Snackbar(text='Url is not available').show()
    def failure(self, urlrequest):
        print("failure")
        Snackbar(text='Url is not available').show()

    def view(self):
        if self.url != '':
            Snackbar(
                text=self.url,
                size_hint_x=2
            ).show()
        else:
            Snackbar(text='Url is not available').show()

MainApp().run()