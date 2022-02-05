from PIL import Image
import random as rn

img1 = Image.open("files/input.jpg")
img2 = img1.convert('L')



def threshold(img):
    pixelMap = img.load()
    width, height = img.size[0], img.size[1]

    for i in range(width):
        for j in range(height):
            value = int(pixelMap[i, j])
            if value > 127:
                pixelMap[i, j] = 255
            else:
                pixelMap[i, j] = 0

    print("..done")



def random(img):
    pixelMap = img.load()
    width, height = img.size[0], img.size[1]

    for i in range(width):
        for j in range(height):
            value = int(pixelMap[i, j])
            if value > rn.randint(0,255):
                pixelMap[i, j] = 255
            else:
                pixelMap[i, j] = 0

    print("..done")



def clustered_dot(img, mod=1):
    if mod == 1:
        dither_arr = Image.open("files/dither_arrays/8x8_vert.png")
        print("getting ready for clustered dot dithering (vertical/horizontal matrix)")
    if mod == 2:
        dither_arr = Image.open("files/dither_arrays/8x8_45deg.png")
        print("getting ready for clustered dot dithering (45 degree matrix)")
    if mod == 3:
        dither_arr = Image.open("files/dither_arrays/4x4_bayer.png")
        print("getting ready for clustered dot dithering (bayer matrix)")

    dither_arr = dither_arr.convert('L')
    arr_pixelMap = dither_arr.load()
    dith_arr_size = dither_arr.size[0]

    pixelMap = img.load()
    width, height = img.size[0], img.size[1]

    for i in range(width):
        for j in range(height):
            value = int(pixelMap[i, j]) + int(arr_pixelMap[i%dith_arr_size, j%dith_arr_size])
            if value > 255:
                pixelMap[i, j] = 255
            else:
                pixelMap[i, j] = 0

    dither_arr.close()
    print("..done")
    
    




def error_dif(img, mod=1):
    print("getting ready for error diffusion dithering")
    pixelMap = img.load()
    width, height = img.size[0], img.size[1]
    print(width, height)

    if mod==1:
        print("getting ready for floyd-steinberg error diffusion dithering")
        for j in range(height): 
            for i in range(width):
                value = pixelMap[i, j]
                if int(value) >= 127:
                    dif = value - 255
                    pixelMap[i, j] = 255
                else:
                    dif = value
                    pixelMap[i, j] = 0

                if i+1 < width:
                    pixelMap[i+1, j] += int((7/16)*dif)
                if i-1 > 0 and j+1 < height:
                    pixelMap[i-1, j+1] += int((3/16)*dif)
                if j+1 < height:
                    pixelMap[i, j+1] += int((5/16)*dif)
                if i+1 < width and j+1 < height:
                    pixelMap[i+1, j+1] += int((1/16)*dif)
    
    if mod==2:
        print("getting ready for sierra-lite error diffusion dithering")
        for j in range(height):
            for i in range(width):    
                value = pixelMap[i, j]
                if int(value) >= 127:
                    dif = value - 255
                    pixelMap[i, j] = 255
                else:
                    dif = value
                    pixelMap[i, j] = 0

                if i+1 < width:
                    pixelMap[i+1, j] += int((2/4)*dif)
                if j+1 < height:
                    pixelMap[i, j] += int((1/4)*dif)
                if i-1 > 0 and j+1 < height:
                    pixelMap[i-1, j+1] += int((1/4)*dif)

    print("..done")



error_dif(img2, 2)
#clustered_dot(img2, 3)
#threshold(img2)


img2.save("files/output13.png")
img2.show()

img1.close()
img2.close()