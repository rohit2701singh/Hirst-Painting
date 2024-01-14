import colorgram

color_list = []
colors = colorgram.extract("image.jpg", 20)
# print(colors)

for i in range(len(colors)):
    rgb = colors[i].rgb
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    color_list.append((red, green, blue))
print(color_list)
