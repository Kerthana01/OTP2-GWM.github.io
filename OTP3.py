from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import random

class OTPApp(App):
    def build(self):
        self.phone_number_input = TextInput(hint_text="Enter your phone number")
        self.otp_label = Label(text="")
        self.verify_input = TextInput(hint_text="Enter the OTP")
        self.result_label = Label(text="")

        generate_button = Button(text="Generate OTP", on_release=self.generate_otp)
        verify_button = Button(text="Verify OTP", on_release=self.verify_otp)

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(self.phone_number_input)
        layout.add_widget(generate_button)
        layout.add_widget(self.otp_label)
        layout.add_widget(self.verify_input)
        layout.add_widget(verify_button)
        layout.add_widget(self.result_label)

        return layout

    def generate_otp(self, instance):
        otp = ''.join(random.choice('0123456789') for _ in range(4))
        self.otp_label.text = f"Generated OTP: {otp}"
        self.generated_otp = otp

    def verify_otp(self, instance):
        user_input = self.verify_input.text
        if user_input == self.generated_otp:
            self.result_label.text = "Valid OTP"
        else:
            self.result_label.text = "Invalid OTP"

if __name__ == "__main__":
    OTPApp().run()
