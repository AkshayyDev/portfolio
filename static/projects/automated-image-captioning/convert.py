from PIL import Image

# Open the images
image1 = Image.open("img1.jpg")
image2 = Image.open("img2.jpg")
image3 = Image.open("img3.jpg")

# Resize the images
size = (580, 300)  # Specify the desired size
image1 = image1.resize(size)
image2 = image2.resize(size)
image3 = image3.resize(size)

# Save the resized images
image1.save("resized_image1.jpg")
image2.save("resized_image2.jpg")
image3.save("resized_image3.jpg")
