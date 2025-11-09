from math import pi
import matplotlib.pyplot as plt
from library_of_materials import materials
#Рассматриваем падение пружины с прикреплённым к ней сверху грузом с определённой небольшой высоты. Система расположена вертикально.

def spring_deformation (V, g, legs, M, l, y, d, D, N, stress_critical, c_spring, T_max, T, C, alfa, p, G, dt, max_oscillation):
    # g - ускорение свободного падения на космическом теле, м/с^2.
    # legs - количество ног у аппарата.
    # M - масса аппарата, кг.
    # l - длина пружины, м.
    # y - высота от поверхности до точки крепления пружины, м.
    # d - диаметр проволоки пружины, м.
    # D - диаметр пружины, м.
    # N - количество витков пружины.
    # stress_critical - максимальное напряжение, которое выдерживает материал пружины, Па.
    # c_spring - коэффициент вязкого трения внутри пружины, кг/м.
    # T_max - температура плавления материала пружины, К.
    # T - температура пружины в данный момент, К.
    # C - удельная теплоёмкость материала пружины, Дж/(кг*К).
    # alfa - коэффициент теплового расширения материала пружины, К^-1.
    # p - плотность материала пружины, кг/м^3.
    # G - коэффициент сдвига пружины, Па.
    # dt - интегрируемый промежуток времени, с.
    # max_oscillation - максимальное количество колебаний.

    n = 10 #Количество сегментов пружины.
    break_number = False
    M /= legs
    the_oscillation = 1 #Номер колебания, происходящего в данный момент.
    y_start = y #Начальная высота крепления пружины.
    t = 0
    l_number = [] #Длина пружины.
    time_of_oscillation = [] #Значения времени колебаний.
    V_spring = [] #Значения скорости пружины.
    stress_spring = [] #Значения механического напряжения.
    delta_spring = [] #Значения относительного сжатия пружины.
    coordinate = [] #Значения расстояния крепления пружины от поверхности.
    x_spring = [] #Значения сжатия пружины.
    F_spring = [] #Значения силы Гука пружины.
    E_spring = [] #Значения потенциальной энергии пружины.
    down_acceleration = [] #Значения максимального ускорения при сжатии пружины.
    d_1 = d #Всё это - диаметры сегментов пружины, отсчёт начинается с поверхности.
    d_2 = d
    d_3 = d
    d_4 = d
    d_5 = d
    d_6 = d
    d_7 = d
    d_8 = d
    d_9 = d
    d_10 = d
    T_spring_1 = [] #Всё это - значения температуры сегментов пружины, отсчёт начинается с поверхности.
    T_spring_2 = []
    T_spring_3 = []
    T_spring_4 = []
    T_spring_5 = []
    T_spring_6 = []
    T_spring_7 = []
    T_spring_8 = []
    T_spring_9 = []
    T_spring_10 = []
    T_1 = T #Всё это - температуры сегментов, отсчёт начинается с поверхности.
    T_2 = T
    T_3 = T
    T_4 = T
    T_5 = T
    T_6 = T
    T_7 = T
    T_8 = T
    T_9 = T
    T_10 = T
    k_1_spring = []
    k_2_spring = []
    k_3_spring = []
    k_4_spring = []
    k_5_spring = []
    k_6_spring = []
    k_7_spring = []
    k_8_spring = []
    k_9_spring = []
    k_10_spring = []
    k = (G * d**4) / (8 * N * D**3) #Расчёт коэффициента жёсткости цилиндрической пружины.
    k_1 = k * n
    k_2 = k * n
    k_3 = k * n
    k_4 = k * n
    k_5 = k * n
    k_6 = k * n
    k_7 = k * n
    k_8 = k * n
    k_9 = k * n
    k_10 = k * n
    m = (N * pi**2 * p * d**2 * D) / 4 #Расчёт массы пружины.
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
            stress_spring.append(4 * m * g / (pi * d**2))
            delta_spring.append(0)
            k_1_spring.append(k_1)
            k_2_spring.append(k_2)
            k_3_spring.append(k_3)
            k_4_spring.append(k_4)
            k_5_spring.append(k_5)
            k_6_spring.append(k_6)
            k_7_spring.append(k_7)
            k_8_spring.append(k_8)
            k_9_spring.append(k_9)
            k_10_spring.append(k_10)
            T_spring_1.append(T_1)
            T_spring_2.append(T_2)
            T_spring_3.append(T_3)
            T_spring_4.append(T_4)
            T_spring_5.append(T_5)
            T_spring_6.append(T_6)
            T_spring_7.append(T_7)
            T_spring_8.append(T_8)
            T_spring_9.append(T_9)
            T_spring_10.append(T_10)
        while V < 0: #Пока пружина сжимается.
            if y > N / n * (d_1 + d_2 + d_3 + d_4 + d_5 + d_6 + d_7 + d_8 + d_9) + d_10 * (N / n + 1):
                l_number.append(l)
                coordinate.append(y)
                t += dt
                time_of_oscillation.append(t)
                y += V * dt
                T_1 += (1 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_2 += (8 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_3 += (27 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_4 += (64 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_5 += (125 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_6 += (216 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_7 += (343 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_8 += (512 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_9 += (729 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_10 += (10 * c_spring * abs(V**3) * dt) / (m * C)
                d_1 *= (1 + alfa * (1 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_2 *= (1 + alfa * (8 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_3 *= (1 + alfa * (27 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_4 *= (1 + alfa * (64 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_5 *= (1 + alfa * (125 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_6 *= (1 + alfa * (216 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_7 *= (1 + alfa * (343 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_8 *= (1 + alfa * (512 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_9 *= (1 + alfa * (729 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_10 *= (1 + alfa * (10 * c_spring * abs(V**3) * dt) / (m * C))
                k_1 = (n * G * d_1**4) / (8 * N * D**3) #Расчёт коэффициента жёсткости для каждого сегмента пружины.
                k_2 = (n * G * d_2**4) / (8 * N * D**3)
                k_3 = (n * G * d_3**4) / (8 * N * D**3)
                k_4 = (n * G * d_4**4) / (8 * N * D**3)
                k_5 = (n * G * d_5**4) / (8 * N * D**3)
                k_6 = (n * G * d_6**4) / (8 * N * D**3)
                k_7 = (n * G * d_7**4) / (8 * N * D**3)
                k_8 = (n * G * d_8**4) / (8 * N * D**3)
                k_9 = (n * G * d_9**4) / (8 * N * D**3)
                k_10 = (n * G * d_10**4) / (8 * N * D**3)
                k = (k_1 * k_2 * k_3 * k_4 * k_5 * k_6 * k_7 * k_8 * k_9 * k_10) / (k_2 * k_3 * k_4 * k_5 * k_6 * k_7 * k_8 * k_9 * k_10 + k_1 * k_3 * k_4 * k_5 * k_6 * k_7 * k_8 * k_9 * k_10 + k_1 * k_2 * k_4 * k_5 * k_6 * k_7 * k_8 * k_9 * k_10 + k_1 * k_2 * k_3 * k_5 * k_6 * k_7 * k_8 * k_9 * k_10 + k_1 * k_2 * k_3 * k_4 * k_6 * k_7 * k_8 * k_9 * k_10 + k_1 * k_2 * k_3 * k_4 * k_5 * k_7 * k_8 * k_9 * k_10 + k_1 * k_2 * k_3 * k_4 * k_5 * k_6 * k_8 * k_9 * k_10 + k_1 * k_2 * k_3 * k_4 * k_5 * k_6 * k_7 * k_9 * k_10 + k_1 * k_2 * k_3 * k_4 * k_5 * k_6 * k_7 * k_8 * k_10 + k_1 * k_2 * k_3 * k_4 * k_5 * k_6 * k_7 * k_8 * k_9)
                V += ((k * (l - y) + c_spring * V**2) / M - g) * dt
                V_spring.append(V)
                F_spring.append(k * (l - y))
                E_spring.append((k * (l - y)**2) / 2)
                x_spring.append(l - y)
                N_ground = abs(m * (k * (l - y) + c_spring * V**2) / (2 * M) + m * g / 2 + k * (l - y) + c_spring * V**2)
                stress_spring.append(4 * max(m * g, k * (l - y), c_spring * V**2, N_ground) / (pi * d**2))
                delta_spring.append((l - y) / l)
                k_1_spring.append(k_1)
                k_2_spring.append(k_2)
                k_3_spring.append(k_3)
                k_4_spring.append(k_4)
                k_5_spring.append(k_5)
                k_6_spring.append(k_6)
                k_7_spring.append(k_7)
                k_8_spring.append(k_8)
                k_9_spring.append(k_9)
                k_10_spring.append(k_10)
                T_spring_1.append(T_1)
                T_spring_2.append(T_2)
                T_spring_3.append(T_3)
                T_spring_4.append(T_4)
                T_spring_5.append(T_5)
                T_spring_6.append(T_6)
                T_spring_7.append(T_7)
                T_spring_8.append(T_8)
                T_spring_9.append(T_9)
                T_spring_10.append(T_10)
                down_acceleration.append((k * (l - y) + c_spring * V**2) / M - g)
            elif y <= N / n * (d_1 + d_2 + d_3 + d_4 + d_5 + d_6 + d_7 + d_8 + d_9) + d_10 * (N / n + 1):
                break_number = True
                break
        if break_number == True:
            break
        while V >= 0 and y < l: #Пока система взлетает, пружина касается поверхности.
            if y > N / n * (d_1 + d_2 + d_3 + d_4 + d_5 + d_6 + d_7 + d_8 + d_9) + d_10 * (N / n + 1):
                l_number.append(l)
                coordinate.append(y)
                t += dt
                time_of_oscillation.append(t)
                y += V * dt
                T_1 += (1 * c_spring * V**3 * dt) / (n**2 * m * C)
                T_2 += (8 * c_spring * V**3 * dt) / (n**2 * m * C)
                T_3 += (27 * c_spring * V**3 * dt) / (n**2 * m * C)
                T_4 += (64 * c_spring * V**3 * dt) / (n**2 * m * C)
                T_5 += (125 * c_spring * V**3 * dt) / (n**2 * m * C)
                T_6 += (216 * c_spring * V**3 * dt) / (n**2 * m * C)
                T_7 += (343 * c_spring * V**3 * dt) / (n**2 * m * C)
                T_8 += (512 * c_spring * V**3 * dt) / (n**2 * m * C)
                T_9 += (729 * c_spring * V**3 * dt) / (n**2 * m * C)
                T_10 += (10 * c_spring * V**3 * dt) / (m * C)
                d_1 *= (1 + alfa * (1 * c_spring * V**3 * dt) / (n**2 * m * C))
                d_2 *= (1 + alfa * (8 * c_spring * V**3 * dt) / (n**2 * m * C))
                d_3 *= (1 + alfa * (27 * c_spring * V**3 * dt) / (n**2 * m * C))
                d_4 *= (1 + alfa * (64 * c_spring * V**3 * dt) / (n**2 * m * C))
                d_5 *= (1 + alfa * (125 * c_spring * V**3 * dt) / (n**2 * m * C))
                d_6 *= (1 + alfa * (216 * c_spring * V**3 * dt) / (n**2 * m * C))
                d_7 *= (1 + alfa * (343 * c_spring * V**3 * dt) / (n**2 * m * C))
                d_8 *= (1 + alfa * (512 * c_spring * V**3 * dt) / (n**2 * m * C))
                d_9 *= (1 + alfa * (729 * c_spring * V**3 * dt) / (n**2 * m * C))
                d_10 *= (1 + alfa * (10 * c_spring * V**3 * dt) / (m * C))
                k_1 = (n * G * d_1**4) / (8 * N * D**3)
                k_2 = (n * G * d_2**4) / (8 * N * D**3)
                k_3 = (n * G * d_3**4) / (8 * N * D**3)
                k_4 = (n * G * d_4**4) / (8 * N * D**3)
                k_5 = (n * G * d_5**4) / (8 * N * D**3)
                k_6 = (n * G * d_6**4) / (8 * N * D**3)
                k_7 = (n * G * d_7**4) / (8 * N * D**3)
                k_8 = (n * G * d_8**4) / (8 * N * D**3)
                k_9 = (n * G * d_9**4) / (8 * N * D**3)
                k_10 = (n * G * d_10**4) / (8 * N * D**3)
                k = (k_1 * k_2 * k_3 * k_4 * k_5 * k_6 * k_7 * k_8 * k_9 * k_10) / (k_2 * k_3 * k_4 * k_5 * k_6 * k_7 * k_8 * k_9 * k_10 + k_1 * k_3 * k_4 * k_5 * k_6 * k_7 * k_8 * k_9 * k_10 + k_1 * k_2 * k_4 * k_5 * k_6 * k_7 * k_8 * k_9 * k_10 + k_1 * k_2 * k_3 * k_5 * k_6 * k_7 * k_8 * k_9 * k_10 + k_1 * k_2 * k_3 * k_4 * k_6 * k_7 * k_8 * k_9 * k_10 + k_1 * k_2 * k_3 * k_4 * k_5 * k_7 * k_8 * k_9 * k_10 + k_1 * k_2 * k_3 * k_4 * k_5 * k_6 * k_8 * k_9 * k_10 + k_1 * k_2 * k_3 * k_4 * k_5 * k_6 * k_7 * k_9 * k_10 + k_1 * k_2 * k_3 * k_4 * k_5 * k_6 * k_7 * k_8 * k_10 + k_1 * k_2 * k_3 * k_4 * k_5 * k_6 * k_7 * k_8 * k_9)
                V += ((k * (l - y) - c_spring * V**2) / M - g) * dt
                V_spring.append(V)
                F_spring.append(k * (l - y))
                E_spring.append((k * (l - y)**2) / 2)
                x_spring.append(l - y)
                N_ground = abs(m * (k * (l - y) + c_spring * V**2) / (2 * M) + m * g / 2 + k * (l - y) - c_spring * V**2)
                stress_spring.append(4 * max(m * g, k * (l - y), c_spring * V**2, N_ground) / (pi * d**2))
                delta_spring.append((l - y) / l)
                k_1_spring.append(k_1)
                k_2_spring.append(k_2)
                k_3_spring.append(k_3)
                k_4_spring.append(k_4)
                k_5_spring.append(k_5)
                k_6_spring.append(k_6)
                k_7_spring.append(k_7)
                k_8_spring.append(k_8)
                k_9_spring.append(k_9)
                k_10_spring.append(k_10)
                T_spring_1.append(T_1)
                T_spring_2.append(T_2)
                T_spring_3.append(T_3)
                T_spring_4.append(T_4)
                T_spring_5.append(T_5)
                T_spring_6.append(T_6)
                T_spring_7.append(T_7)
                T_spring_8.append(T_8)
                T_spring_9.append(T_9)
                T_spring_10.append(T_10)
                down_acceleration.append((k * (l - y) - c_spring * V**2) / M - g)
            elif y <= N / n * (d_1 + d_2 + d_3 + d_4 + d_5 + d_6 + d_7 + d_8 + d_9) + d_10 * (N / n + 1):
                break_number = True
                break
        if break_number == True:
            break
        while V < 0 and y < l:
            if y > N / n * (d_1 + d_2 + d_3 + d_4 + d_5 + d_6 + d_7 + d_8 + d_9) + d_10 * (N / n + 1):
                l_number.append(l)
                coordinate.append(y)
                t += dt
                time_of_oscillation.append(t)
                y += V * dt
                T_1 += (1 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_2 += (8 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_3 += (27 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_4 += (64 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_5 += (125 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_6 += (216 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_7 += (343 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_8 += (512 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_9 += (729 * c_spring * abs(V**3) * dt) / (n**2 * m * C)
                T_10 += (10 * c_spring * abs(V**3) * dt) / (m * C)
                d_1 *= (1 + alfa * (1 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_2 *= (1 + alfa * (8 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_3 *= (1 + alfa * (27 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_4 *= (1 + alfa * (64 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_5 *= (1 + alfa * (125 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_6 *= (1 + alfa * (216 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_7 *= (1 + alfa * (343 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_8 *= (1 + alfa * (512 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_9 *= (1 + alfa * (729 * c_spring * abs(V**3) * dt) / (n**2 * m * C))
                d_10 *= (1 + alfa * (10 * c_spring * abs(V**3) * dt) / (m * C))
                k_1 = (n * G * d_1**4) / (8 * N * D**3)
                k_2 = (n * G * d_2**4) / (8 * N * D**3)
                k_3 = (n * G * d_3**4) / (8 * N * D**3)
                k_4 = (n * G * d_4**4) / (8 * N * D**3)
                k_5 = (n * G * d_5**4) / (8 * N * D**3)
                k_6 = (n * G * d_6**4) / (8 * N * D**3)
                k_7 = (n * G * d_7**4) / (8 * N * D**3)
                k_8 = (n * G * d_8**4) / (8 * N * D**3)
                k_9 = (n * G * d_9**4) / (8 * N * D**3)
                k_10 = (n * G * d_10**4) / (8 * N * D**3)
                k = (k_1 * k_2 * k_3 * k_4 * k_5 * k_6 * k_7 * k_8 * k_9 * k_10) / (k_2 * k_3 * k_4 * k_5 * k_6 * k_7 * k_8 * k_9 * k_10 + k_1 * k_3 * k_4 * k_5 * k_6 * k_7 * k_8 * k_9 * k_10 + k_1 * k_2 * k_4 * k_5 * k_6 * k_7 * k_8 * k_9 * k_10 + k_1 * k_2 * k_3 * k_5 * k_6 * k_7 * k_8 * k_9 * k_10 + k_1 * k_2 * k_3 * k_4 * k_6 * k_7 * k_8 * k_9 * k_10 + k_1 * k_2 * k_3 * k_4 * k_5 * k_7 * k_8 * k_9 * k_10 + k_1 * k_2 * k_3 * k_4 * k_5 * k_6 * k_8 * k_9 * k_10 + k_1 * k_2 * k_3 * k_4 * k_5 * k_6 * k_7 * k_9 * k_10 + k_1 * k_2 * k_3 * k_4 * k_5 * k_6 * k_7 * k_8 * k_10 + k_1 * k_2 * k_3 * k_4 * k_5 * k_6 * k_7 * k_8 * k_9)
                V += ((k * (l - y) + c_spring * V**2) / M - g) * dt
                V_spring.append(V)
                F_spring.append(k * (l - y))
                E_spring.append((k * (l - y)**2) / 2)
                x_spring.append(l - y)
                N_ground = abs(m * (k * (l - y) + c_spring * V**2) / (2 * M) + m * g / 2 + k * (l - y) + c_spring * V**2)
                stress_spring.append(4 * max(m * g, k * (l - y), c_spring * V**2, N_ground) / (pi * d**2))
                delta_spring.append((l - y) / l)
                k_1_spring.append(k_1)
                k_2_spring.append(k_2)
                k_3_spring.append(k_3)
                k_4_spring.append(k_4)
                k_5_spring.append(k_5)
                k_6_spring.append(k_6)
                k_7_spring.append(k_7)
                k_8_spring.append(k_8)
                k_9_spring.append(k_9)
                k_10_spring.append(k_10)
                T_spring_1.append(T_1)
                T_spring_2.append(T_2)
                T_spring_3.append(T_3)
                T_spring_4.append(T_4)
                T_spring_5.append(T_5)
                T_spring_6.append(T_6)
                T_spring_7.append(T_7)
                T_spring_8.append(T_8)
                T_spring_9.append(T_9)
                T_spring_10.append(T_10)
                down_acceleration.append((k * (l - y) + c_spring * V**2) / M - g)
            elif y <= N / n * (d_1 + d_2 + d_3 + d_4 + d_5 + d_6 + d_7 + d_8 + d_9) + d_10 * (N / n + 1):
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
            stress_spring.append(4 * m * g / (pi * d**2))
            delta_spring.append(0)
            k_1_spring.append(k_1)
            k_2_spring.append(k_2)
            k_3_spring.append(k_3)
            k_4_spring.append(k_4)
            k_5_spring.append(k_5)
            k_6_spring.append(k_6)
            k_7_spring.append(k_7)
            k_8_spring.append(k_8)
            k_9_spring.append(k_9)
            k_10_spring.append(k_10)
            T_spring_1.append(T_1)
            T_spring_2.append(T_2)
            T_spring_3.append(T_3)
            T_spring_4.append(T_4)
            T_spring_5.append(T_5)
            T_spring_6.append(T_6)
            T_spring_7.append(T_7)
            T_spring_8.append(T_8)
            T_spring_9.append(T_9)
            T_spring_10.append(T_10)
        the_oscillation += 1
    if break_number == False:
        if max(stress_spring) < stress_critical:
            if max(T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9, T_10) < T_max:
                print(f"Max down acceleration is {round(max(down_acceleration), 4)} m/s^2.")
                print(f"Max relative shortening of spring is {round(max(delta_spring), 4)}.")
                print(f"The ration of max stress of spring to critical stress of spring is {round(max(stress_spring) / stress_critical * 100, 4)} %.")
                print(f"Maximum temperature of the spring's segment is {round(max(T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9, T_10), 4)} K, while max temperature is {T_max} K.")
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
                plt.plot(time_of_oscillation, T_spring_1, 'g')
                plt.plot(time_of_oscillation, T_spring_2, 'g')
                plt.plot(time_of_oscillation, T_spring_3, 'g')
                plt.plot(time_of_oscillation, T_spring_4, 'g')
                plt.plot(time_of_oscillation, T_spring_5, 'g')
                plt.plot(time_of_oscillation, T_spring_6, 'g')
                plt.plot(time_of_oscillation, T_spring_7, 'g')
                plt.plot(time_of_oscillation, T_spring_8, 'g')
                plt.plot(time_of_oscillation, T_spring_9, 'g')
                plt.plot(time_of_oscillation, T_spring_10, 'g')
                plt.xlabel("с")
                plt.ylabel("К")
                plt.grid()
                plt.title("Зависимость температуры от времени.")
                plt.subplot(3, 2, 5)
                plt.plot(time_of_oscillation, k_1_spring, 'b')
                plt.plot(time_of_oscillation, k_2_spring, 'b')
                plt.plot(time_of_oscillation, k_3_spring, 'b')
                plt.plot(time_of_oscillation, k_4_spring, 'b')
                plt.plot(time_of_oscillation, k_5_spring, 'b')
                plt.plot(time_of_oscillation, k_6_spring, 'b')
                plt.plot(time_of_oscillation, k_7_spring, 'b')
                plt.plot(time_of_oscillation, k_8_spring, 'b')
                plt.plot(time_of_oscillation, k_9_spring, 'b')
                plt.plot(time_of_oscillation, k_10_spring, 'b')
                plt.xlabel("с")
                plt.ylabel("Н/м")
                plt.grid()
                plt.title("Зависимость жёсткости сегментов от времени.")
                plt.subplot(3, 2, 6)
                plt.plot(time_of_oscillation, stress_spring, 'r')
                plt.xlabel("с")
                plt.ylabel("Па")
                plt.grid()
                plt.title('Зависимость механического напряжения от времени.')
                plt.show()
            elif max(T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9, T_10) >= T_max:
                print(f"The spring will melt. Maximum temperature of sprint is {round(max(T_1, T_2, T_3, T_4, T_5, T_6, T_7, T_8, T_9, T_10), 4)} K, while critical temperature is {T_max}, K.")
        elif max(stress_spring) >= stress_critical:
            print(f"The spring will break. The ration of max stress of spring to critical stress of spring is {round(max(stress_spring) / stress_critical * 100, 4)} %.")
    elif break_number == True:
        print(f"The spring is too weak. The critical hight is bigger then minimum hight on {round(((N / n * (d_1 + d_2 + d_3 + d_4 + d_5 + d_6 + d_7 + d_8 + d_9) + d_10 * (N / n + 1)) / (l - max(x_spring)) - 1) * 100, 4)} %.")

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
        c_spring = material.c,
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
        c_spring = float(input("Choose coefficient of ")),
        T_max = float(input("Choose temperature of melting of the material.")),
        T = float(input("Choose temperature of the material.")),
        C = float(input("Choose coefficient of viscous friction of the material.")),
        alfa = float(input("Choose coefficient of thermal expansion of the material.")),
        p = float(input("Choose density of the material.")),
        G = float(input("Choose shear modulus of the material.")),
        dt = float(input("Choose time interval.")),
        max_oscillation = int(input("Choose number of oscillation."))
    )