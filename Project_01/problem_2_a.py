import math

start_radius = 0
end_radius = 100
dr = 10 ** -3

# According to: https://en.wikipedia.org/wiki/TNT_equivalent#:~:text=TNT%20equivalent%20is%20a%20convention,(1%2C000%20kilograms)%20of%20TNT.
joules_per_gram_tnt = 4184

rho = 1000
g = 10
h = 100
p_avg = rho * g * h

energy = 0
for r in range(round((end_radius-start_radius)/dr)):
    area = 4 * math.pi * r ** 2
    f = p_avg * area
    energy += f * dr
print("Energy:")
print(f"{energy} Joules")
print(f"{energy/joules_per_gram_tnt} Grams TNT Equivalent")