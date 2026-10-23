import os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.text import LabelBase

# IMPORTANT: Apni app me Hindi sahi se dikhane ke liye koi bhi Hindi font (jaise 'NotoSansDevanagari-Regular.ttf') 
# download karke isi folder me rakhein aur niche register karein.
FONT_PATH = "NotoSansDevanagari-Regular.ttf"
if os.path.exists(FONT_PATH):
    LabelBase.register(name="Hindi", fn_regular=FONT_PATH)
    FONT_NAME = "Hindi"
else:
    FONT_NAME = "Roboto" # Default fallback

class MainApp(App):
    def build(self):
        self.title = "Hindi Data Processor"
        
        # Main Layout (Vertical)
        layout = BoxLayout(orientation='vertical', padding=15, spacing=10)
        
        # Title Label
        title_label = Label(
            text="डेटा प्रोसेसिंग एप्लिकेशन", 
            font_name=FONT_NAME, 
            font_size='22sp', 
            size_hint_y=None, 
            height=40,
            bold=True
        )
        layout.add_widget(title_label)
        
        # Input Section Label
        input_label = Label(
            text="नीचे अपना टेक्स्ट या डेटा दर्ज करें:", 
            font_name=FONT_NAME, 
            font_size='16sp', 
            size_hint_y=None, 
            height=30,
            halign='left',
            valign='middle'
        )
        input_label.bind(size=input_label.setter('text_size'))
        layout.add_widget(input_label)
        
        # Text Input Box
        self.user_input = TextInput(
            hint_text="यहाँ लिखें...", 
            font_name=FONT_NAME,
            font_size='16sp',
            multiline=True,
            size_hint_y=0.3
        )
        layout.add_widget(self.user_input)
        
        # Process Button
        process_btn = Button(
            text="डेटा प्रोसेस करें", 
            font_name=FONT_NAME,
            font_size='18sp',
            background_color=(0.1, 0.6, 0.4, 1),
            size_hint_y=None, 
            height=50
        )
        process_btn.bind(on_press=self.process_data)
        layout.add_widget(process_btn)
        
        # Output Section Label
        output_label = Label(
            text="प्रोसेस्ड आउटपुट:", 
            font_name=FONT_NAME, 
            font_size='16sp', 
            size_hint_y=None, 
            height=30,
            halign='left',
            valign='middle'
        )
        output_label.bind(size=output_label.setter('text_size'))
        layout.add_widget(output_label)
        
        # Scrollable Output Area
        scroll = ScrollView(size_hint_y=0.5)
        self.output_text = Label(
            text="यहाँ आपका रिजल्ट दिखेगा।", 
            font_name=FONT_NAME,
            font_size='16sp',
            size_hint_y=None,
            halign='left',
            valign='top'
        )
        self.output_text.bind(size=self.output_text.setter('text_size'))
        self.output_text.bind(texture_size=lambda instance, value: setattr(instance, 'height', value))
        
        scroll.add_widget(self.output_text)
        layout.add_widget(scroll)
        
        return layout

    def process_data(self, instance):
        text_to_process = self.user_input.text
        
        if not text_to_process.strip():
            self.output_text.text = "कृपया प्रोसेसिंग के लिए कुछ टेक्स्ट दर्ज करें!"
            return
            
        try:
            result = f"सफलतापूर्वक प्रोसेस किया गया!\n\nमूल टेक्स्ट: {text_to_process}\nकैरेक्टर काउंट: {len(text_to_process)}"
            self.output_text.text = result
            
        except Exception as e:
            self.output_text.text = f"त्रुटि (Error): {str(e)}"

if __name__ == "__main__":
    MainApp().run()
  
