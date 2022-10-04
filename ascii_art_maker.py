from PIL import Image, ImageOps
import random


def get_brightness(pixel):
    brightness = pixel[0] + pixel[1] + pixel[2]
    brightness = brightness/3
    return brightness
###Convert the input image to grayscale.
###Split the image into M×N tiles.
###Correct M (the number of rows) to match the image and font aspect ratio.
###Compute the average brightness for each image tile and then look up a suitable ASCII character for each.
###Assemble rows of ASCII character strings and print them to a file to form the final image

def find_ascii(brightness):

    #simgle sorting algorithm to find the darkest pixel ie: r + g + b 
    #returns pixel index
    #can take current_min_index as an argument if it is desired to run the sorting again multiple times on a single row
    character = ""
    scale = " .:-=+*#%@"

    if (brightness < 25):
        character = "@"
    elif (brightness >= 25 and brightness < 50):
        character = "%"
    elif (brightness >= 50 and brightness < 75):
        character = "#"
    elif (brightness >= 75 and brightness < 100):
        character = "*"
    elif (brightness >= 100 and brightness < 125):
        character = "+"
    elif (brightness >= 125 and brightness < 150):
        
        character = "="
    elif  (brightness >= 150 and brightness < 175):
        
        character = "-"
    elif (brightness >= 175 and brightness < 200):
        
        character = ":"
    elif (brightness >=200 and brightness < 225):
        
        character = "."
    elif (brightness >= 225 and brightness <= 255):
        
        character = " "

    
    return character


def main():
    basewidth = int(input("resolution (single int): "))
    img_input = input("input image file: ")
    img = Image.open(img_input)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    img.save('thumbnail.jpg')

    
    
    new_img = Image.open('thumbnail.jpg')
    #img = ImageOps.grayscale(img)
    pixels = new_img.load()
    width, height = img.size
    string = ""

    #print(pixels[0,0])
    
    for y in range(height):
        row = []
        #column = []
        for x in range(width):
            row.append(pixels[x,y])
            #print(row[x])
            brightness = get_brightness(row[x])
            string += find_ascii(brightness)
            string += find_ascii(brightness)
            if (x == width-1):
                string += "\n"
    
            
    with open('output.txt', 'w') as f:
        f.write(string)
        print(string)

    

if __name__ == "__main__":
    main()