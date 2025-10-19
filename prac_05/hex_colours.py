COLOUR_TO_CODE = {"blue1": "#0000ff", "cyan1": "#00ffff", "gold1": "#ffd700", "green1": "#00ff00",
                "red1": "#ff0000", "purple": "#a020f0", "black": "#000000", "white": "#ffffff", "yellow": "#ffff00", "orange1": "#ffa500"}
print(COLOUR_TO_CODE)

colour_input = input("Enter colour: ").lower()
while colour_input != "":
    try:
        print(colour_input, "is", COLOUR_TO_CODE[colour_input])
    except KeyError:
        print("Invalid colour")
    colour_input = input("Enter colour: ").lower()
