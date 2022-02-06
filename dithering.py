"""
dithering
david petera, 1. year of studies
winter term 2021/22
NPRG030 – programming 1
"""

#importing necessary libraries
from PIL import Image     #image handeling
import random as rn     #generation of pseudo-random values 


def threshold(img): 
    #loading pixels of the image and size
    pixelMap = img.load()
    width, height = img.size[0], img.size[1]
    print("\ngetting ready for threshold dithering...")

    #going through every pixel and changing its value according to the set threshold
    threshold = 127
    for j in range(height):
        for i in range(width):
            value = int(pixelMap[i, j])
            if value > threshold:
                pixelMap[i, j] = 255
            else:
                pixelMap[i, j] = 0

    print("..done")



def random(img):
    #loading pixels of the image and size
    pixelMap = img.load()
    width, height = img.size[0], img.size[1]
    print("\ngetting ready for random dithering...")

    #going through every pixel and changing its value according to the random threshold
    for j in range(height):
        for i in range(width):
            value = int(pixelMap[i, j])
            if value > rn.randint(0,255):
                pixelMap[i, j] = 255
            else:
                pixelMap[i, j] = 0

    print("..done")



def clustered_dot(img, mod=1):
    #loading the right dithering matrix (according to the input) from the image files 
    if mod == 1:
        dither_matrix = Image.open("files/dither_matricies/8x8_vert.png")
        print("\ngetting ready for clustered dot dithering (vertical/horizontal matrix)...")
    if mod == 2:
        dither_matrix = Image.open("files/dither_matricies/8x8_45deg.png")
        print("\ngetting ready for clustered dot dithering (diagonal matrix)...")
    if mod == 3:
        dither_matrix = Image.open("files/dither_matricies/4x4_bayer.png")
        print("\ngetting ready for clustered dot dithering (bayer matrix)...")

    dither_matrix = dither_matrix.convert('L')
    matrix_pixelMap = dither_matrix.load()
    dith_matrix_size = dither_matrix.size[0]

    #loading pixels of the image and size
    pixelMap = img.load()
    width, height = img.size[0], img.size[1]

    #going through every pixel and adding its value with the value in the dither matrix and changing its value according to the threshold
    threshold = 255
    for j in range(height):
        for i in range(width):
            value = int(pixelMap[i, j]) + int(matrix_pixelMap[i%dith_matrix_size, j%dith_matrix_size])
            if value > threshold:
                pixelMap[i, j] = 255
            else:
                pixelMap[i, j] = 0

    dither_matrix.close()
    print("..done")
    
    

def error_dif(img, mod=1):
    #loading pixels of the image and size
    pixelMap = img.load()
    width, height = img.size[0], img.size[1]

    if mod==1:      #if floyd-steinberg selected

        print("\ngetting ready for floyd-steinberg error diffusion dithering...")

        #going through every pixel, changing its value according to the threshold and distributing the difference (error) to the neighbouring pixels
        threshold = 127
        for j in range(height): 
            for i in range(width):
                value = pixelMap[i, j]
                if int(value) >= threshold:
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
    
    if mod==2:      #if sierra-lite selected

        print("\ngetting ready for sierra-lite error diffusion dithering...")

        #going through every pixel, changing its value according to the threshold and distributing the difference (error) to the neighbouring pixels
        threshold = 127
        for j in range(height):
            for i in range(width):    
                value = pixelMap[i, j]
                if int(value) >= threshold:
                    dif = value - 255
                    pixelMap[i, j] = 255
                else:
                    dif = value
                    pixelMap[i, j] = 0

                if i+1 < width:
                    pixelMap[i+1, j] += int((2/4)*dif)
                if j+1 < height:
                    pixelMap[i, j+1] += int((1/4)*dif)
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

    dith_type = dith_type.strip()       #striping the input of unwanted leading and trailing space characters
    dith_type = dith_type.strip(".")    #striping the input of unwanted leading and trailing dot characters

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
        img_gray.save("files/outputs/output.png")       #saving the image
        img_gray.show()     #showing the final image to the user

    img_gray.close()

except:
    print("wrong file name entered")
