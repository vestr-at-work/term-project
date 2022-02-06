from PIL import Image
import random as rn


def threshold(img): 
    pixelMap = img.load()
    width, height = img.size[0], img.size[1]
    print("\ngetting ready for threshold dithering...")

    for j in range(height):
        for i in range(width):
            value = int(pixelMap[i, j])
            if value > 127:
                pixelMap[i, j] = 255
            else:
                pixelMap[i, j] = 0

    print("..done")



def random(img):
    pixelMap = img.load()
    width, height = img.size[0], img.size[1]
    print("\ngetting ready for random dithering...")

    for j in range(height):
        for i in range(width):
            value = int(pixelMap[i, j])
            if value > rn.randint(0,255):
                pixelMap[i, j] = 255
            else:
                pixelMap[i, j] = 0

    print("..done")



def clustered_dot(img, mod=1):
    if mod == 1:
        dither_arr = Image.open("files/dither_arrays/8x8_vert.png")
        print("\ngetting ready for clustered dot dithering (vertical/horizontal matrix)...")
    if mod == 2:
        dither_arr = Image.open("files/dither_arrays/8x8_45deg.png")
        print("\ngetting ready for clustered dot dithering (diagonal matrix)...")
    if mod == 3:
        dither_arr = Image.open("files/dither_arrays/4x4_bayer.png")
        print("\ngetting ready for clustered dot dithering (bayer matrix)...")

    dither_arr = dither_arr.convert('L')
    arr_pixelMap = dither_arr.load()
    dith_arr_size = dither_arr.size[0]

    pixelMap = img.load()
    width, height = img.size[0], img.size[1]

    for j in range(height):
        for i in range(width):
            value = int(pixelMap[i, j]) + int(arr_pixelMap[i%dith_arr_size, j%dith_arr_size])
            if value > 255:
                pixelMap[i, j] = 255
            else:
                pixelMap[i, j] = 0

    dither_arr.close()
    print("..done")
    
    

def error_dif(img, mod=1):
    pixelMap = img.load()
    width, height = img.size[0], img.size[1]

    if mod==1:
        print("\ngetting ready for floyd-steinberg error diffusion dithering...")
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
        print("\ngetting ready for sierra-lite error diffusion dithering...")
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


#--------------------------start of the main program-------------------------------

print("program for image dithering.\n")

file = input("enter the file name (with suffix): ")
file = file.strip()     #striping the input of unwanted leading and trailing space characters 

try:
    img = Image.open(f"files/{file}")
    img_gray = img.convert('L')     #converting the input image to grayscale
    img.close()

    print("\nwhat type of dithering do you want?\n")

    print("1. threshold dithering")
    print("2. random dithering")
    print("3. cluster dot dithering - 8x8px vertical/horizontal matrix")
    print("4. cluster dot dithering - 8x8px diagonal matrix")
    print("5. cluster dot dithering - 4x4px bayer matrix")
    print("6. error diffusion dithering - floyd-steinberg")
    print("7. error diffusion dithering - sierra-lite")

    dith_type = input("\nenter the number: ")
    input_error = False     #setting default value for input error handling to False

    dith_type = dith_type.strip()
    dith_type = dith_type.strip(".")

    if dith_type == '1':
        threshold(img_gray)
    elif dith_type == '2':
        random(img_gray)
    elif dith_type == '3':
        clustered_dot(img_gray, 1)
    elif dith_type == '4':
        clustered_dot(img_gray, 2)
    elif dith_type == '5':
        clustered_dot(img_gray, 3)
    elif dith_type == '6':
        error_dif(img_gray, 1)
    elif dith_type == '7':
        error_dif(img_gray, 2)
    else:       #if wrong value has been entered
        print("\nwrong input")
        input_error = True      
    
    if input_error is not True:
        img_gray.save("files/output.png")
        img_gray.show()     #showing the final image to the user

    img_gray.close()

except:
    print("wrong file name entered")
