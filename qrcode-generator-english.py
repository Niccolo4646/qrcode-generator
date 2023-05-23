#Github | Niccolo4646

import qrcode

link = input("Write an URL ")
namefile1 = input("Write the name you want to give to the file without the extension ")
namefile2 = ".png"
namefile3 = namefile1 + namefile2

obj_qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 10, border = 4)

obj_qr.add_data(link)

obj_qr.make(fit = True)

qr_img = obj_qr.make_image(fill_color = "black")

qr_img.save(namefile3)

print("Done!")
print("I created the qrcode for", link)