import colorgram

colors = colorgram.extract('painting.jpg', 10)
first_color = colors[0]
rgb = first_color.rgb # e.g. (255, 151, 210)
hsl = first_color.hsl # e.g. (230, 255, 203)
print(rgb)
print(hsl)