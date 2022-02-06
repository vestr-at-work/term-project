# Term project
Implementing different types of dithering algorithms for grayscale images. 

(Black and white) Dithering in esence converts grayscale images to only black and white with various levels of fidelity according to the algorithm used.

Dithering on wiki: https://en.wikipedia.org/wiki/Dither#Digital_photography_and_image_processing

In this project these algorithms are implemented:

1. Threshold dithering
2. Random dithering
3. Cluster dot dithering - 8x8px vertical/horizontal matrix
4. Cluster dot dithering - 8x8px diagonal matrix
5. Cluster dot dithering - 4x4px Bayer matrix
6. Error diffusion dithering - Floyd-Steinberg
7. Error diffusion dithering - Sierra-lite


User manual:

User needs to have installed the 'Pillow' library and 'random' library for the program to work.

For help on the installation of 'Pillow' click here: https://pillow.readthedocs.io/en/stable/installation.html

Library 'random' should be part of the standard Python installation, for more info look here: https://docs.python.org/3/library/random.html


Inputs:

User has to put the input images in the 'files/inputs' folder. (They don't need to be grayscale. If they have colour, they will be automaticaly converted to grayscale.)

All major file formats are supported. More info here: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html

Program run:

After running the program, user will be asked to enter the name of the image (even with suffix!) desired to be dithered.

After that, user will be shown the following algorithms and asked to choose one by entering the number of the chosen one.

1. Threshold dithering
2. Random dithering
3. Cluster dot dithering - 8x8px vertical/horizontal matrix
4. Cluster dot dithering - 8x8px diagonal matrix
5. Cluster dot dithering - 4x4px Bayer matrix
6. Error diffusion dithering - Floyd-Steinberg
7. Error diffusion dithering - Sierra-lite

If all done correctly (after a moment - the time depends on the algorithm chosen), user will be shown the dithered image and it will be saved in the 'files/outputs' folder as well. 




