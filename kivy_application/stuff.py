for _ in range(7):
            self.add_widget(Label(text=f"{days[_]}", pos_hint={'x': x_var, 'y': 0.8}, size_hint=(0.14, 0.1)))  
            x_var += 0.14
        self.name = TextInput(pos_hint={'x': x_var, 'y': 0.8}, size_hint=(0.14, 0.1)))
        #self.add_widget(self.name)