import FreeSimpleGUI as sg

compress_label = sg.Text("Select a file to compress: ")
compress_input = sg.InputText()
choose_button1 = sg.FilesBrowse("Choose")

destination_label = sg.Text("Select a destination folder: ")
destination_input = sg.InputText()
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[[compress_label, compress_input, choose_button1],
                                                   [destination_label, destination_input, choose_button2],
                                                   [compress_button]])

window.read()
window.close()