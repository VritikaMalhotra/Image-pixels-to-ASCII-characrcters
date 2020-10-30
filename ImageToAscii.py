from PIL import Image #Using pillow libaray

#Making a list of Ascii characters we want in our image and reversing it. 
ASCII_CHARS = ['.',',',':','a','^','%',';','v','*',';',':']
ASCII_CHARS =ASCII_CHARS[::-1]

#Function to resize the image.
def resize(image,new_width):
    
    (old_width,old_height) = image.size

    #Finding the aspect ratio.
    aspect_ratio = float(old_height)/float(old_width)

    #Multiplying aspect ratio with new width to genarate new height with same ratio.
    new_height = int(aspect_ratio*new_width)
    new_dim = (new_width,new_height)

    #Genarting new image with new dimesnsions.
    new_image = image.resize(new_dim)
    return new_image


#This fucntion will return photograph in grayscale.
def grayscale(image):
    return image.convert('L')

#Function used to map pixels from image to ascii charcaters.
def modify(image,buckets=25):
    #Getting all the pixels of image.
    initial_pixels = list(image.getdata())

    #Mapping all the pixesls to ascii charcaters in the list.
    new_pixels = [ASCII_CHARS[pixels//buckets]for pixels in initial_pixels]

    #Returning a string of all pixels joint.
    return ''.join(new_pixels)

#Calling all functions
def do(image,new_width=100):

    #Calling ewsize fucntion
    image = resize(image,new_width)

    #Calling grayscale fucntion
    image = grayscale(image)

    #Calling modify fucntion
    pixels = modify(image)
    len_pixels = len(pixels)

    new_image = [pixels[index:index+new_width]for index in range(0,len_pixels,new_width)]
    return '\n'.join(new_image)

#Opening image
def start(path):
    image = None
    try:
        image = Image.open(path)
    except:
        print('UNABLE TO FIND IMAGE...')
        return

    #Calling do fucntion to call all the other fucntions.
    image = do(image)

    #Creating a text file and opening it in write mode , writing image pixels and closing the file.
    f = open('image.txt','w')
    f.write(image)
    f.close()

if __name__  ==  "__main__":
    import sys
    import urllib.request 

    #When we rund the code using command prompt argv[1] gives us the path of the image
    #or name of the file which we want to convert.
    #Here this fucntion checks if the second argument is a link, it sends request to the server
    #the second argument is the default argument. If the system is unable to get its url request fullfilled,
    #the hacker.jpg is the default image.
    if(sys.argv[1].startswith('http://') or sys.argv[1].startswith('https://')):
        urllib.request.urlretrieve(sys.argv[1],"hacker.jpg")
        path = "hacker.jpg"

    else:
        path = sys.argv[1]

    #Calling the start fucntion.which calles the do ducntion, which will call all the other fucntions.
    start(path)