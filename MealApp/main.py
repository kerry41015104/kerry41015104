from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
import requests
from kivy.properties import StringProperty
import webbrowser
from kivymd.uix.snackbar import Snackbar
from kivy.uix.label import Label


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
        ingredient_list = self.root.ids['home'].ids['ingredient_list']
        url = 'https://www.themealdb.com/api/json/v1/1/random.php'
        recipe = requests.get(url=url).json()
        print(recipe)
        self.name = recipe['meals'][0]['strMeal']
        self.category = recipe['meals'][0]['strCategory']
        self.area = recipe['meals'][0]['strArea']
        self.image = recipe['meals'][0]['strMealThumb']
        self.url = recipe['meals'][0]['strSource']
        for i in range(1,21):
            if recipe['meals'][0][f'strIngredient{i}'] != '':
                l = Label(text=recipe['meals'][0][f'strIngredient{i}'],color=(0,0,0,1))
                ingredient_list.add_widget(l)


    def view(self):
        if self.url != '':
            webbrowser.open(self.url)
        else:
            Snackbar(text='Url is not available').show()



MainApp().run()