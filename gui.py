import dearpygui.core as dgc
import dearpygui.simple as dgs
import main

def callLogic(sender, data):
    main.generateQRCodes(dgs.get_value("Input"))

dgc.set_main_window_size(330,250)

with dgs.window("QR Codes Generieren", width=300, height=200):
    print("GUI running")
    dgs.set_window_pos("QR Codes Generieren",0,0)
    dgc.set_theme("Blue")
    dgc.add_text("Sourcepath")
    dgc.add_spacing()
    dgc.add_input_text("Input", width=300)
    dgc.add_spacing()
    dgc.add_button("Generate",callback=callLogic)



dgc.start_dearpygui()