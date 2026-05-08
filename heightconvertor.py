import functions

import FreeSimpleGUI as sg

feet_label = sg.Text("Feet: ")
feet_input = sg.InputText(tooltip="Enter feet")

inches_label = sg.Text("Inches:")
inches_input = sg.InputText(tooltip="Enter inches")

convert_button = sg.Button("Convert")

window = sg.Window("Height Converter", layout=[[feet_label, feet_input], [inches_label, inches_input], [convert_button]])
window.read()
window.close()