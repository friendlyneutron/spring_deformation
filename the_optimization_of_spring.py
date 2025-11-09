from math import pi
from library_of_materials import materials

def the_optimization_of_spring (n, legs, g, M, V_0, k, G, p, l):
    # n - кратность перегрузки (n > 1).
    # legs - количество ног у аппарата.
    # g - ускорение свободного падения на поверхности космического тела, м/с^2.
    # M - масса аппарата, кг.
    # k - коэффициент жёсткости пружины, Н/м.
    # G - модуль сдвига материала пружины, Па.
    # p - плотность материала пружины, кг/м^3.
    # l - длина пружины, м.

    M /= legs
    y_max = l + (M * g * (n**2 - 1)) / (2 * k) - V_0**2 / (2 * g)
    print("Your hight must be less, then", y_max, "meters.")
    y = float(input("Choose hight, that you want."))
    if y < y_max:
        beta = float(input("Choose the ratio of the diameter of the spring to the diameter of the wire of the spring."))
        d_max = 2 * ((2 * beta**2 * k * M * (M * g**2 * (n**2 - 1) + k * (2 * g * (l - y) - V_0**2))) / (pi**2 * p * G * (M * g**2 * (n + 1) + k * (2 * g * y + V_0**2))))**0.25
        print("Your diameter should be less, then", d_max, "meters.")
        d = float(input("Choose diameter, that you want"))
        if d <= d_max:
            print("Your spring will have", round((pi**2 * G * p * d**4) / (32 * beta**2 * k), 4), "kilogram.")
            print("Your spring will have", beta * d, "meters of diameter of it.")
            print("Your spring will have", round((G * d) / (8 * beta**3 * k), 4), "rounds.")
        else:
            print("Your diameter is too big.")
    else:
        print("Your hight is too high.")

material_name = input("Choose material that you want. If you don't want any, choose '-'.")
if material_name != "-" and material_name not in materials:
    print("The library doesn't have that material.")
elif material_name != "-" and material_name in materials:
    material = materials[material_name]
    the_optimization_of_spring(
        n = float(input("Choose the coefficient of overload.")),
        legs = int(input("Choose a number of legs on the machine.")),
        g = float(input("Choose acceleration on space object.")),
        M = float(input("Choose mass of the machine.")),
        V_0 = float(input("Choose speed of start.")),
        k = float(input("Choose the stiffness coefficient of the spring.")),
        G = material.G,
        p = material.p,
        l = float(input("Choose length of spring."))
    )
elif material_name == "-":
    the_optimization_of_spring(
    n = float(input("Choose the coefficient of overload.")),
    legs = int(input("Choose a number of legs on the machine.")),
    g = float(input("Choose acceleration on space object.")),
    M = float(input("Choose mass of the machine.")),
    V_0 = float(input("Choose speed of start.")),
    k = float(input("Choose the stiffness coefficient of the spring.")),
    G = float(input("Choose shear modulus of the material.")),
    p = float(input("Choose density of the material.")),
    l = float(input("Choose length of spring."))
)