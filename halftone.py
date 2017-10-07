from PIL import Image, ImageDraw
"""
Floyd-Steinberg 

	X 7
  3 5 1   (1/16)
  
  
grayscale 

x = (0.299 * R + 0.587 * G + 0.114 * B)
"""


orig_img = Image.open("image.jpg")
size = orig_img.size
#new_img = Image.new("RGB", size, color=(255,255,255))

new_img = orig_img.copy()
draw = ImageDraw.Draw(new_img)



#orig_px = orig_img.load()
#new_px = new_img.load()

width = size[0]
height = size[1]
print(width, height)

def makeGreyscale() :
	for x in range(0, width):
		for y in range(0, height):
			current_px = orig_img.getpixel( (x, y) )
			#right_px = orig_img.getpixel( (x + 1, y) )
			#below_px = orig_img.getpixel( (x, y + 1) )
			#left_below_px = orig_img.getpixel( (x - 1, y + 1) )
			#right_below_px = orig_img.getpixel( (x + 1, y + 1) )
		

			grayscale = (0.299 * current_px[0]) + (0.587 * current_px[1]) + (0.114 * current_px[2])
		
			new_img.putpixel( (x, y), (int(grayscale), int(grayscale), int(grayscale)))
		

"""
def halftone():
	for x in range(1, width-1, 2):
		for y in range(0, height-1, 1):
			print(x,y)
			current_px = new_img.getpixel( (x, y) )
			right_px = new_img.getpixel( (x + 1, y) )
			below_px = new_img.getpixel( (x, y + 1) )
			left_below_px = new_img.getpixel( (x - 1, y + 1) )
			right_below_px = new_img.getpixel( (x + 1, y + 1) )

			grayscale = (0.299 * current_px[0]) + (0.587 * current_px[1]) + (0.114 * current_px[2])
			
			if grayscale > (255/2):
				#white
				error = 255.0 - grayscale
				error_one = error/16
				new_img.putpixel( (x, y), (255,255,255))
			else:
				#black
				error = grayscale
				error_one = error/16
				new_img.putpixel( (x, y), (0,0,0))
	
			right_px_error = error_one * 7
			new_img.putpixel((x + 1, y), (int(right_px[0] * right_px_error), int(right_px[1] * right_px_error), int(right_px[2] * right_px_error)))
			
			below_px_error = error_one * 5
			new_img.putpixel((x + 1, y), (int(below_px[0] * below_px_error), int(below_px[1] * below_px_error), int(below_px[2] * below_px_error)))				

			left_below_px_error = error_one * 3
			new_img.putpixel((x + 1, y), (int(left_below_px[0] * left_below_px_error), int(left_below_px[1] * left_below_px_error), int(left_below_px[2] * left_below_px_error)))
			
			right_below_px_error = error_one * 1
			new_img.putpixel((x + 1, y), (int(right_below_px[0] * right_below_px_error), int(right_below_px[1] * right_below_px_error), int(right_below_px[2] * right_below_px_error)))		
			
			#new_img.putpixel( (x, y), (int(grayscale), int(grayscale), int(grayscale)))
"""

size_circle = 4

def halftone():
	for x in range(0, width-1, size_circle):
		for y in range(0, height-1, size_circle):
			print(x,y)
			
			position = [(x,y), (x+(size_circle/2), y+(size_circle/2))]
			pixels = []
			
			for i in range(0, int(size_circle/2)):
				for j in range(0, int(size_circle/2)):
					print(i,j)
					try:
						pixels[i+j] = new_img.getpixel( (x+i, y+j) )
						new_img.putpixel( (x+i, y+j), (255,255,255) )
					except:
						pixels[i+j] = (0,0,0)
			
			average_red = 0;
			average_green = 0
			average_blue = 0
			for pixel in pixels:
				average_red += pixel[0]
				average_green += pixel[1]
				average_blue += pixel[2]
			
			average_red = average_red / pixels.length()
			average_green = average_green / pixels.length()
			average_blue = average_blue / pixels.length()
			
			grayscale = (0.299 * average_red) + (0.587 * average_green) + (0.114 * average_blue)	
			
			draw.ellipse(position, fill=(int(grayscale), int(grayscale), int(grayscale)))							
				
			"""	
			current_px = new_img.getpixel( (x, y) )
			new_img.putpixel( (x,y), (255,255,255) )
			
			try:
				right_px = new_img.getpixel( (x+1, y) )
				new_img.putpixel( (x+1,y), (255,255,255) )
			except:
				right_px = (0,0,0)
			
			try:
				below_px = new_img.getpixel( (x, y+1) )
				new_img.putpixel( (x,y+1), (255,255,255) )
			except:
				below_px = (0,0,0)
			
			try:
				right_below_px = new_img.getpixel( (x+1, y+1) )
				new_img.putpixel( (x+1,y+1), (255,255,255) )
			except:
				right_below_px = (0,0,0)
				
			position = [(x,y), (x+1, y+1)]
			
			average_red = (current_px[0] + right_px[0] + below_px[0] + right_below_px[0]) / 4
			average_green = (current_px[1] + right_px[1] + below_px[1] + right_below_px[1]) / 4
			average_blue = (current_px[2] + right_px[2] + below_px[2] + right_below_px[2]) / 4
			
			grayscale = (0.299 * average_red) + (0.587 * average_green) + (0.114 * average_blue)	
			
			draw.ellipse(position, fill=(int(grayscale), int(grayscale), int(grayscale)))
			"""
						
			
halftone()

new_img.save("halftone.jpg", "JPEG")



