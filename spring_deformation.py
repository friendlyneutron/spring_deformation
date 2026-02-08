from math import pi
import matplotlib.pyplot as plt
from library_of_materials import materials
#Рассматриваем падение пружины с прикреплённым к ней сверху грузом с определённой небольшой высоты. Система расположена вертикально.

def spring_deformation (V, g, legs, M, l, y, d, D, N, stress_critical, c, T_max, T, C, alfa, p, G, dt, max_oscillation):
    # g - ускорение свободного падения на космическом теле, м/с^2.
    # legs - количество ног у аппарата.
    # M - масса аппарата, кг.
    # l - длина пружины, м.
    # y - высота от поверхности до точки крепления пружины, м.
    # d - диаметр проволоки пружины, м.
    # D - диаметр пружины, м.
    # N - количество витков пружины.
    # stress_critical - максимальное напряжение, которое выдерживает материал пружины, Па.
    # c - коэффициент вязкого трения внутри пружины, кг/м.
    # T_max - температура плавления материала пружины, К.
    # T - температура пружины в данный момент, К.
    # C - удельная теплоёмкость материала пружины, Дж/(кг*К).
    # alfa - коэффициент теплового расширения материала пружины, К^-1.
    # p - плотность материала пружины, кг/м^3.
    # G - коэффициент сдвига пружины, Па.
    # dt - интегрируемый промежуток времени, с.
    # max_oscillation - максимальное количество колебаний.

    break_number = False
    M /= legs
    the_oscillation = 1 #Номер колебания, происходящего в данный момент.
    y_start = y #Начальная высота крепления пружины.
    t = 0
    l_number = [] #Длина пружины.
    time_of_oscillation = [] #Значения времени колебаний.
    V_spring = [] #Значения скорости пружины.
    stress_spring_1 = [] #Значения механического напряжения.
    stress_spring_2 = []
    stress_spring_3 = []
    stress_spring_4 = []
    delta_spring = [] #Значения относительного сжатия пружины.
    coordinate = [] #Значения расстояния крепления пружины от поверхности.
    x_spring = [] #Значения сжатия пружины.
    F_spring = [] #Значения силы Гука пружины.
    E_spring = [] #Значения потенциальной энергии пружины.
    down_acceleration = [] #Значения максимального ускорения при сжатии пружины.
    T_spring_1 = [] #Всё это - значения температуры сегментов пружины, отсчёт начинается с поверхности.
    T_spring_2 = []
    T_spring_3 = []
    T_spring_4 = []
    T_1 = T #Всё это - температуры сегментов, отсчёт начинается с поверхности.
    T_2 = T
    T_3 = T
    T_4 = T
    d_1 = d
    d_2 = d
    d_3 = d
    d_4 = d
    k_1_spring = []
    k_2_spring = []
    k_3_spring = []
    k_4_spring = []
    k = G * d**4 / (8 * N * D**3)
    k_1 = k
    k_2 = k
    k_3 = k
    k_4 = k
    m = (N * pi**2 * p * d**2 * D) / 4
    m_1 = m / 4
    m_2 = m / 4
    m_3 = m / 4
    m_4 = m / 4
    while the_oscillation <= max_oscillation:
        while y >= l: #Пока система опускается, пружина не касается поверхности.
            l_number.append(l)
            coordinate.append(y)
            t += dt
            time_of_oscillation.append(t)
            y += V * dt
            V -= g * dt
            V_spring.append(V)
            F_spring.append(0)
            E_spring.append(0)
            x_spring.append(0)
            stress_spring_1.append(4 * m_1 * g / (pi * d_1**2))
            stress_spring_2.append(4 * m_2 * g / (pi * d_2**2))
            stress_spring_3.append(4 * m_3 * g / (pi * d_3**2))
            stress_spring_4.append(4 * m_4 * g / (pi * d_4**2))
            delta_spring.append(0)
            k_1_spring.append(k_1)
            k_2_spring.append(k_2)
            k_3_spring.append(k_3)
            k_4_spring.append(k_4)
            T_spring_1.append(T_1)
            T_spring_2.append(T_2)
            T_spring_3.append(T_3)
            T_spring_4.append(T_4)
        while V < 0: #Пока пружина сжимается.
            if y > (d_1 * N + d_2 * N + d_3 * N + d_4 * (N + 1)) / 4:
                l_number.append(l)
                coordinate.append(y)
                t += dt
                time_of_oscillation.append(t)
                y += V * dt
                T_1 += (c * V**2 * abs(V) * dt) / (64 * m_1 * C)
                T_2 += (c * V**2 * abs(V) * dt) / (8 * m_2 * C)
                T_3 += (27 * c * V**2 * abs(V) * dt) / (64 * m_3 * C)
                T_4 += (c * V**2 * abs(V) * dt) / (m_4 * C)
                d_1 *= (1 + alfa * (c * V**2 * abs(V) * dt) / (64 * m_1 * C))
                d_2 *= (1 + alfa * (c * V**2 * abs(V) * dt) / (8 * m_2 * C))
                d_3 *= (1 + alfa * (27 * c * V**2 * abs(V) * dt) / (64 * m_3 * C))
                d_4 *= (1 + alfa * (c * V**2 * abs(V) * dt) / (m_4 * C))
                k_1 = (G * d_1**4) / (4 * N * D**3) #Расчёт коэффициента жёсткости для каждого сегмента пружины.
                k_2 = (G * d_2**4) / (4 * N * D**3)
                k_3 = (G * d_3**4) / (4 * N * D**3)
                k_4 = (G * d_4**4) / (4 * N * D**3)
                k = k_1 * k_2 * k_3 * k_4 / (k_2 * k_3 * k_4 + k_1 * k_3 * k_4 + k_1 * k_2 * k_4 + k_1 * k_2 * k_3)
                V += ((k * (l - y) + c * V**2) / M - g) * dt
                V_spring.append(V)
                F_spring.append(k * (l - y))
                E_spring.append((k * (l - y)**2) / 2)
                x_spring.append(l - y)
                N_ground = (1 + m / (2 * M)) * (k * (l - y) + c * V**2)
                stress_spring_1.append(4 * max(m_1 * g, k_1 * (l - y), c * V**2 * 0.25**2, N_ground) / (pi * d_1**2))
                stress_spring_2.append(4 * max(m_2 * g, k_2 * (l - y), k_1 * (l - y), c * V**2 * 0.25**2, c * V**2 * 0.25) / (pi * d_2**2))
                stress_spring_3.append(4 * max(m_3 * g, k_3 * (l - y), k_2 * (l - y), c * V**2 * 0.25, c * V**2 * 9 * 0.25**2) / (pi * d_3**2))
                stress_spring_4.append(4 * max(m_4 * g, k_4 * (l - y), k_3 * (l - y), c * V**2 * 9 * 0.25**2, c * V**2) / (pi * d_4**2))
                delta_spring.append((l - y) / l)
                k_1_spring.append(k_1)
                k_2_spring.append(k_2)
                k_3_spring.append(k_3)
                k_4_spring.append(k_4)
                T_spring_1.append(T_1)
                T_spring_2.append(T_2)
                T_spring_3.append(T_3)
                T_spring_4.append(T_4)
                down_acceleration.append((k * (l - y) + c * V**2) / M - g)
            elif y <= (d_1 * N + d_2 * N + d_3 * N + d_4 * (N + 1)) / 4:
                break_number = True
                break
        if break_number == True:
            break
        while V >= 0 and y < l: #Пока система взлетает, пружина касается поверхности.
            if y > (d_1 * N + d_2 * N + d_3 * N + d_4 * (N + 1)) / 4:
                l_number.append(l)
                coordinate.append(y)
                t += dt
                time_of_oscillation.append(t)
                y += V * dt
                T_1 += (c * V**3 * dt) / (64 * m_1 * C)
                T_2 += (c * V**3 * dt) / (8 * m_2 * C)
                T_3 += (27 * c * V**3 * dt) / (64 * m_3 * C)
                T_4 += (c * V**3 * dt) / (m_4 * C)
                d_1 *= (1 + alfa * (c * V**3 * dt) / (64 * m_1 * C))
                d_2 *= (1 + alfa * (c * V**3 * dt) / (8 * m_2 * C))
                d_3 *= (1 + alfa * (27 * c * V**3 * dt) / (64 * m_3 * C))
                d_4 *= (1 + alfa * (c * V**3 * dt) / (m_4 * C))
                k_1 = (G * d_1**4) / (4 * N * D**3)
                k_2 = (G * d_2**4) / (4 * N * D**3)
                k_3 = (G * d_3**4) / (4 * N * D**3)
                k_4 = (G * d_4**4) / (4 * N * D**3)
                k = k_1 * k_2 * k_3 * k_4 / (k_2 * k_3 * k_4 + k_1 * k_3 * k_4 + k_1 * k_2 * k_4 + k_1 * k_2 * k_3)
                V += ((k * (l - y) - c * V**2) / M - g) * dt
                V_spring.append(V)
                F_spring.append(k * (l - y))
                E_spring.append((k * (l - y)**2) / 2)
                x_spring.append(l - y)
                N_ground = (1 + m / (2 * M)) * (k * (l - y) - c * V**2)
                stress_spring_1.append(4 * max(m_1 * g, k_1 * (l - y), c * V**2 * 0.25**2, N_ground) / (pi * d_1**2))
                stress_spring_2.append(4 * max(m_2 * g, k_2 * (l - y), k_1 * (l - y), c * V**2 * 0.25**2, c * V**2 * 0.25) / (pi * d_2**2))
                stress_spring_3.append(4 * max(m_3 * g, k_3 * (l - y), k_2 * (l - y), c * V**2 * 0.25, c * V**2 * 9 * 0.25**2) / (pi * d_3**2))
                stress_spring_4.append(4 * max(m_4 * g, k_4 * (l - y), k_3 * (l - y), c * V**2 * 9 * 0.25**2, c * V**2) / (pi * d_4**2))
                delta_spring.append((l - y) / l)
                k_1_spring.append(k_1)
                k_2_spring.append(k_2)
                k_3_spring.append(k_3)
                k_4_spring.append(k_4)
                T_spring_1.append(T_1)
                T_spring_2.append(T_2)
                T_spring_3.append(T_3)
                T_spring_4.append(T_4)
                down_acceleration.append((k * (l - y) - c * V**2) / M - g)
            elif y <= (d_1 * N + d_2 * N + d_3 * N + d_4 * (N + 1)) / 4:
                break_number = True
                break
        if break_number == True:
            break
        while V < 0 and y < l:
            if y > (d_1 * N + d_2 * N + d_3 * N + d_4 * (N + 1)) / 4:
                l_number.append(l)
                coordinate.append(y)
                t += dt
                time_of_oscillation.append(t)
                y += V * dt
                T_1 += (c * V**2 * abs(V) * dt) / (64 * m_1 * C)
                T_2 += (c * V**2 * abs(V) * dt) / (8 * m_2 * C)
                T_3 += (27 * c * V**2 * abs(V) * dt) / (64 * m_3 * C)
                T_4 += (c * V**2 * abs(V) * dt) / (m_4 * C)
                d_1 *= (1 + alfa * (c * V**2 * abs(V) * dt) / (64 * m_1 * C))
                d_2 *= (1 + alfa * (c * V**2 * abs(V) * dt) / (8 * m_2 * C))
                d_3 *= (1 + alfa * (27 * c * V**2 * abs(V) * dt) / (64 * m_3 * C))
                d_4 *= (1 + alfa * (c * V**2 * abs(V) * dt) / (m_4 * C))
                k_1 = (G * d_1**4) / (4 * N * D**3)
                k_2 = (G * d_2**4) / (4 * N * D**3)
                k_3 = (G * d_3**4) / (4 * N * D**3)
                k_4 = (G * d_4**4) / (4 * N * D**3)
                k = k_1 * k_2 * k_3 * k_4 / (k_2 * k_3 * k_4 + k_1 * k_3 * k_4 + k_1 * k_2 * k_4 + k_1 * k_2 * k_3)
                V += ((k * (l - y) + c * V**2) / M - g) * dt
                V_spring.append(V)
                F_spring.append(k * (l - y))
                E_spring.append((k * (l - y)**2) / 2)
                x_spring.append(l - y)
                N_ground = (1 + m / (2 * M)) * (k * (l - y) + c * V**2)
                stress_spring_1.append(4 * max(m_1 * g, k_1 * (l - y), c * V**2 * 0.25**2, N_ground) / (pi * d_1**2))
                stress_spring_2.append(4 * max(m_2 * g, k_2 * (l - y), k_1 * (l - y), c * V**2 * 0.25**2, c * V**2 * 0.25) / (pi * d_2**2))
                stress_spring_3.append(4 * max(m_3 * g, k_3 * (l - y), k_2 * (l - y), c * V**2 * 0.25, c * V**2 * 9 * 0.25**2) / (pi * d_3**2))
                stress_spring_4.append(4 * max(m_4 * g, k_4 * (l - y), k_3 * (l - y), c * V**2 * 9 * 0.25**2, c * V**2) / (pi * d_4**2))
                delta_spring.append((l - y) / l)
                k_1_spring.append(k_1)
                k_2_spring.append(k_2)
                k_3_spring.append(k_3)
                k_4_spring.append(k_4)
                T_spring_1.append(T_1)
                T_spring_2.append(T_2)
                T_spring_3.append(T_3)
                T_spring_4.append(T_4)
                down_acceleration.append((k * (l - y) + c * V**2) / M - g)
            elif y <= (d_1 * N + d_2 * N + d_3 * N + d_4 * (N + 1)) / 4:
                break_number = True
                break
        if break_number == True:
            break
        while V > 0 and y >= l: #Пока система взлетает, пружина не касается поверхности.
            l_number.append(l)
            coordinate.append(y)
            t += dt
            time_of_oscillation.append(t)
            y += V * dt
            V -= g * dt
            V_spring.append(V)
            F_spring.append(0)
            E_spring.append(0)
            x_spring.append(0)
            stress_spring_1.append(4 * m_1 * g / (pi * d_1**2))
            stress_spring_2.append(4 * m_2 * g / (pi * d_2**2))
            stress_spring_3.append(4 * m_3 * g / (pi * d_3**2))
            stress_spring_4.append(4 * m_4 * g / (pi * d_4**2))
            delta_spring.append(0)
            k_1_spring.append(k_1)
            k_2_spring.append(k_2)
            k_3_spring.append(k_3)
            k_4_spring.append(k_4)
            T_spring_1.append(T_1)
            T_spring_2.append(T_2)
            T_spring_3.append(T_3)
            T_spring_4.append(T_4)
        the_oscillation += 1
    if break_number == False:
        if max(max(stress_spring_1), max(stress_spring_2), max(stress_spring_3), max(stress_spring_4)) < stress_critical:
            if max(T_1, T_2, T_3, T_4) < T_max:
                print(f"Maximum down acceleration is {round(max(down_acceleration), 4)} m/s^2.")
                print(f"Maximum relative shortening of spring is {round(max(delta_spring), 4)}.")
                print(f"The rations of maximum stress of springs every segment to critical stress of springs segments are {round(max(stress_spring_1) / stress_critical * 100, 4)} %, {round(max(stress_spring_2) / stress_critical * 100, 4)} %, {round(max(stress_spring_3) / stress_critical * 100, 4)} %, {round(max(stress_spring_4) / stress_critical * 100, 4)} %.")
                print(f"The rations of maximum temperature of springs every segment to its critical temperature are {round(max(T_spring_1) / T_max * 100, 4)} %, {round(max(T_spring_2) / T_max * 100, 4)} %, {round(max(T_spring_3) / T_max * 100, 4)} %, {round(max(T_spring_4) / T_max * 100, 4)} %.")
                if y_start >= l:
                    print("Time of oscillation is", round(t / (max_oscillation + 0.5) * max_oscillation, 4), "s.")
                if y_start < l:
                    print("Time of oscillation is", round(t, 4), "s.")
                if the_oscillation == max_oscillation + 1:
                    print("True")
                elif the_oscillation < max_oscillation + 1:
                    print("False")
                plt.subplot(3, 2, 1)
                plt.plot(time_of_oscillation, coordinate, 'black')
                plt.plot(time_of_oscillation, l_number, 'purple')
                plt.legend(["coordinate", "lenght of the spring"])
                plt.xlabel("с")
                plt.ylabel("м")
                plt.grid()
                plt.title('Зависимость координаты крепления пружины от времени.')
                plt.subplot(3, 2, 2)
                plt.plot(time_of_oscillation, E_spring, 'g')
                plt.xlabel("с")
                plt.ylabel("Дж")
                plt.grid()
                plt.title('Зависимость потенциальной энергии от времени.')
                plt.subplot(3, 2, 3)
                plt.plot(time_of_oscillation, V_spring, 'gray')
                plt.xlabel("с")
                plt.ylabel("м/с")
                plt.grid()
                plt.title("Зависимость скорости от времени.")
                plt.subplot(3, 2, 4)
                plt.plot(time_of_oscillation, T_spring_1, 'r')
                plt.plot(time_of_oscillation, T_spring_2, 'orange')
                plt.plot(time_of_oscillation, T_spring_3, 'yellow')
                plt.plot(time_of_oscillation, T_spring_4, 'g')
                plt.legend(["first", "second", "third", "fourth"])
                plt.xlabel("с")
                plt.ylabel("К")
                plt.grid()
                plt.title("Зависимость температуры от времени.")
                plt.subplot(3, 2, 5)
                plt.plot(time_of_oscillation, k_1_spring, 'b')
                plt.plot(time_of_oscillation, k_2_spring, 'brown')
                plt.plot(time_of_oscillation, k_3_spring, 'black')
                plt.plot(time_of_oscillation, k_4_spring, 'purple')
                plt.legend(["first", "second", "third", "fourth"])
                plt.xlabel("с")
                plt.ylabel("Н/м")
                plt.grid()
                plt.title("Зависимость жёсткости сегментов от времени.")
                plt.subplot(3, 2, 6)
                plt.plot(time_of_oscillation, stress_spring_1, 'r')
                plt.plot(time_of_oscillation, stress_spring_2, 'orange')
                plt.plot(time_of_oscillation, stress_spring_3, 'yellow')
                plt.plot(time_of_oscillation, stress_spring_4, 'green')
                plt.legend(["first", "second", "third", "fourth"])
                plt.xlabel("с")
                plt.ylabel("Па")
                plt.grid()
                plt.title('Зависимость механического напряжения от времени.')
                plt.show()
            else:
                print("The spring will melt.")
                if T_1 >= T_max:
                    print(f"The first segment will melt. Tempretature of it is more then its maximum temperature on {round((T_1 - T_max) / T_max * 100, 4)} %.")
                if T_2 >= T_max:
                    print(f"The second segment will melt. Tempretature of it is more then its maximum temperature on {round((T_2 - T_max) / T_max * 100, 4)} %.")
                if T_3 >= T_max:
                    print(f"The third segment will melt. Tempretature of it is more then its maximum temperature on {round((T_3 - T_max) / T_max * 100, 4)} %.")
                if T_4 >= T_max:
                    print(f"The fourth segment will melt. Tempretature of it is more then its maximum temperature on {round((T_4 - T_max) / T_max * 100, 4)} %.")
        else:
            print("The spring will break.")
            if max(stress_spring_1) >= stress_critical:
                print(f"The first segment will break. Maximum stress in it is more then critical stress of its material on {round((max(stress_spring_1) - stress_critical) / stress_critical * 100, 4)} %.")
            if max(stress_spring_2) >= stress_critical:
                print(f"The second segment will break. Maximum stress in it is more then critical stress of its material on {round((max(stress_spring_2) - stress_critical) / stress_critical * 100, 4)} %.")
            if max(stress_spring_3) >= stress_critical:
                print(f"The third segment will break. Maximum stress in it is more then critical stress of its material on {round((max(stress_spring_3) - stress_critical) / stress_critical * 100, 4)} %.")
            if max(stress_spring_4) >= stress_critical:
                print(f"The fourth segment will break. Maximum stress in it is more then critical stress of its material on {round((max(stress_spring_4) - stress_critical) / stress_critical * 100, 4)} %.")
    elif break_number == True:
        print(f"The spring is too weak. The critical hight is bigger then minimum hight on {round((((d_1 * N + d_2 * N + d_3 * N + d_4 * (N + 1)) / 4) / (l - max(x_spring)) - 1) * 100, 4)} %.")

material_name = input("Choose material that you want. If you don't want any, choose '-'.")
if material_name != "-" and material_name not in materials:
    print("The library doesn't have that material.")
elif material_name != "-" and material_name in materials:
    material = materials[material_name]
    spring_deformation(
        V = float(input("Choose speed of starting.")),
        g = float(input("Choose acceleration on space object.")),
        legs = int(input("Choose a number of legs on the machine.")),
        M = float(input("Choose mass of machine.")),
        l = float(input("Choose length of spring.")),
        y = float(input("Choose height.")),
        d = float(input("Choose diameter of wire.")),
        D = float(input("Choose diameter of spring.")),
        N = float(input("Choose number of rounds.")),
        stress_critical = material.stress_critical,
        c = material.c,
        T_max = material.T_max,
        T = float(input("Choose temperature of material.")),
        C = material.C,
        alfa = material.alfa,
        p = material.p,
        G = material.G,
        dt = float(input("Choose time interval.")),
        max_oscillation = int(input("Choose number of oscillation."))
    )
elif material_name == "-":
    spring_deformation(
        V = float(input("Choose speed of starting.")),
        g = float(input("Choose acceleration on space object.")),
        legs = int(input("Choose a number of legs on the machine.")),
        M = float(input("Choose mass of machine.")),
        l = float(input("Choose length of spring.")),
        y = float(input("Choose height.")),
        d = float(input("Choose diameter of wire.")),
        D = float(input("Choose diameter of spring.")),
        N = float(input("Choose number of rounds.")),
        stress_critical = float(input("Choose critical stress of material.")),
        c = float(input("Choose coefficient of ")),
        T_max = float(input("Choose temperature of melting of material.")),
        T = float(input("Choose temperature of material.")),
        C = float(input("Choose coefficient of viscous friction of material.")),
        alfa = float(input("Choose coefficient of thermal expansion of material.")),
        p = float(input("Choose density of material.")),
        G = float(input("Choose shear modulus of material.")),
        dt = float(input("Choose time interval.")),
        max_oscillation = int(input("Choose number of oscillation."))
    )