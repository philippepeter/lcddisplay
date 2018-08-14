# lcddisplay
Docker image to display a string on an LCD screen of an arduino using the serial port.

## Electronic wires:
[Arduino liquid crystal display](https://www.arduino.cc/en/Tutorial/LiquidCrystalDisplay)

## Arduino code
Created from the the Arduino example: LiquidDisplay->SerialDisplay

[The code](https://github.com/philippepeter/lcddisplay/blob/master/display.arduino)

## Command
`docker run --device=/dev/[USB_DEVICE] [DOCKER_IMAGE_NAME] "[STRING_TO_DISPLAY]"`

For example on a raspberrypi:
`docker run --device=/dev/ttyACM0 lcddisplay "Hello world!"`



