from PIL import Image
import PIL

img1 = Image.open("files/input6.png")
img2 = img1.convert('L')



def clustered_dot(img, mod=1):
    if mod == 1:
        dither_arr = Image.open("files/dither_arrays/8x8_vert.png")
        print(f"getting ready for clustered dot dithering (vertical/horizontal matrix)\nwith the image size of{img.size[0]}x{img.size[1]}px")
    if mod == 2:
        dither_arr = Image.open("files/dither_arrays/8x8_45deg.png")
        print(f"getting ready for clustered dot dithering (45 degree matrix)\nwith the image size of{img.size[0]}x{img.size[1]}px")
    if mod == 3:
        dither_arr = Image.open("files/dither_arrays/4x4_bayer.png")
        print(f"getting ready for clustered dot dithering (bayer matrix)\nwith the image size of{img.size[0]}x{img.size[1]}px")
    dither_arr = dither_arr.convert('L')
    arr_pixelMap = dither_arr.load()
    pixelMap = img.load()

    arr_size = dither_arr.size[0]

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            value = int(pixelMap[i, j]) + int(arr_pixelMap[i%arr_size, j%arr_size])
            if value > 255:
                pixelMap[i, j] = 255
            else:
                pixelMap[i, j] = 0

        if i % 50 == 0 : print(f"{i}, {j}")

    print("..done")
    dither_arr.close()
    




def error_dif(img):
    print(f"getting ready for error difusion dithering with the image size of{img.size[0]}x{img.size[1]}px")
    pixelMap = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):    
            value = pixelMap[i, j]
            if int(value) >= 127:
                dif = value - 255
                pixelMap[i, j] = 255
            else:
                dif = value
                pixelMap[i, j] = 0

            if j+1 < img.size[1]:
                pixelMap[i, j+1] += int((7/16)*dif)
            if i+1 < img.size[0]:
                pixelMap[i+1, j-1] += int((3/16)*dif)
            if i+1 < img.size[0]:
                pixelMap[i+1, j] += int((5/16)*dif)
            if i+1 < img.size[0] and j+1 < img2.size[1]:
                pixelMap[i+1, j+1] += int((1/16)*dif)
        if i % 50 == 0 : print(f"{i}, {j}")
    print("..done")


#error_dif(img2)
clustered_dot(img2, 3)

img2.save("files/output13.png")
img2.show()

img1.close()
img2.close()