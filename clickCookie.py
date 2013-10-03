from pymouse import PyMouse
from time import sleep

if __name__ == '__main__':
	
	m = PyMouse()

	pos = m.position()
	xPos = pos[0]
	yPos = pos[1]

	while True:

		m.click(xPos, yPos, 3)
		sleep(0.02)


