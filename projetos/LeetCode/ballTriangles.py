

red: int = 2

blue: int = 4

color: bool = True

# red = 1, blue = 0

def generateTriangle(red: int, blue: int, startColor: bool) -> list:
	
	triangle: list = [startColor]
	loop: bool = True
	color: bool = startColor
	iterations: int = 0

	while loop:
		layerNumber = len(triangle)
		if color == True:
			if red - layerNumber >= 0:
				triangle.append(layerNumber)
				red -= layerNumber
				color = not color
				continue

		if color == False:
			if blue - layerNumber >= 0:
				triangle.append(layerNumber)
				blue -= layerNumber
				color = not color
				continue
		print(f"triangle = {triangle}, color = {color}, layerNumber = {layerNumber}, red = {red}, blue = {blue}")
		if (red - layerNumber or blue - layerNumber < 0):
			break
			

		


	if triangle[-1] < len(triangle) - 1:
		triangle.pop()

	return(triangle)		

redTriangle = generateTriangle(red = red, blue = blue, startColor = True)
blueTriangle = generateTriangle(red = red, blue = blue, startColor = False)


print(f"redTriangle = {redTriangle}, {len(redTriangle) - 1}; blueTriangle = {blueTriangle}, {len(blueTriangle) -1 }")

print("max length = " + str(max(len(redTriangle) - 1, len(blueTriangle) - 1)))





