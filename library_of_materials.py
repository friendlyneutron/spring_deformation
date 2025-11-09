class Material:
    def __init__(name, stress_critical, c, T_max, C, alfa, p, G):
        name.stress_critical = stress_critical
        name.c = c
        name.T_max = T_max
        name.C = C
        name.alfa = alfa
        name.p = p
        name.G = G


steel = Material(
    stress_critical = 600e6,
    c = 0.15,
    T_max = 1700,
    C = 500,
    alfa = 12.5e-6,
    p = 7850,
    G = 80e9
    )

aluminum = Material(
    stress_critical = 270e6,
    c = 0.08,
    T_max = 930,
    C = 900,
    alfa = 23.1e-6,
    p = 2700,
    G = 26e9
    )

titanium = Material(
    stress_critical = 240e6,
    c = 725,
    T_max = 1941,
    C = 522,
    alfa = 8.6e-6,
    p = 4506,
    G = 45e9
    )

ferrum = Material(
    stress_critical = 540e6,
    c = 0.12,
    T_max = 1811,
    C = 450,
    alfa = 11.8e-6,
    p = 7870,
    G = 82e9
    )

argentum = Material(
    stress_critical = 125e6,
    c = 0.05,
    T_max = 1235,
    C = 235,
    alfa = 19.5e-6,
    p = 10490,
    G = 30e9
    )

cuprum = Material(
    stress_critical = 210e6,
    c = 0.09,
    T_max = 1357,
    C = 385,
    alfa = 16.5e-6,
    p = 8960,
    G = 48e9
    )

magnesium = Material(
    stress_critical = 160e6,
    c = 0.06,
    T_max = 923,
    C = 1020,
    alfa = 25.2e-6,
    p = 1738,
    G = 17e9
    )

kalium = Material(
    stress_critical = 15e6,
    c = 0.02,
    T_max = 336,
    C = 757,
    alfa = 83e-6,
    p = 862,
    G = 2.1e9
    )

calcium = Material(
    stress_critical = 110e6,
    c = 0.04,
    T_max = 1115,
    C = 647,
    alfa = 22.3e-6,
    p = 1550,
    G = 7.4e9
    )

chromium = Material(
    stress_critical = 689e6,
    c = 0.11,
    T_max = 2130,
    C = 449,
    alfa = 4.9e-6,
    p = 7190,
    G = 115e9
    )

cobaltum = Material(
    stress_critical = 760e6,
    c = 0.13,
    T_max = 1768,
    C = 421,
    alfa = 13e-6,
    p = 8900,
    G = 82e9
    )

niccolum = Material(
    stress_critical = 345e6,
    c = 0.1,
    T_max = 1728,
    C = 445,
    alfa = 13.4e-6,
    p = 8908,
    G = 76e9
    )

zincum = Material(
    stress_critical = 110e6,
    c = 0.04,
    T_max = 693,
    C = 390,
    alfa = 30.2e-6,
    p = 7140,
    G = 43e9
    )

manganum = Material(
    stress_critical = 250e6,
    c = 0.06,
    T_max = 1519,
    C = 479,
    alfa = 21.7e-6,
    p = 7470,
    G = 80e9
    )

niobium = Material(
    stress_critical = 275e6,
    c = 0.05,
    T_max = 2750,
    C = 265,
    alfa = 7.3e-6,
    p = 8570,
    G = 37e9
    )

molybdaenum = Material(
    stress_critical = 550e6,
    c = 0.08,
    T_max = 2896,
    C = 251,
    alfa = 4.8e-6,
    p = 10220,
    G = 126e9
    )

palladium = Material(
    stress_critical = 180e6,
    c = 0.05,
    T_max = 1828,
    C = 244,
    alfa = 11.8e-6,
    p = 12023,
    G = 44e9
    )

plumbum = Material(
    stress_critical = 18e6,
    c = 0.03,
    T_max = 600.6,
    C = 129,
    alfa = 28.9e-6,
    p = 11340,
    G = 5.6e9
    )

platinum = Material(
    stress_critical = 125e6,
    c = 0.06,
    T_max = 2041,
    C = 133,
    alfa = 8.8e-6,
    p = 21450,
    G = 61e9
    )

vanadium = Material(
    stress_critical = 450e6,
    c = 0.09,
    T_max = 1910,
    C = 490,
    alfa = 8.4e-6,
    p = 6110,
    G = 47e9
    )

scandium = Material(
    stress_critical = 220e6,
    c = 0.06,
    T_max = 1814,
    C = 568,
    alfa = 10.2e-6,
    p = 2985,
    G = 29e9
    )

germanium = Material(
    stress_critical = 150e6,
    c = 0.05,
    T_max = 1211,
    C = 320,
    alfa = 6e-6,
    p = 5323,
    G = 41e9
    )

yttrium = Material(
    stress_critical = 200e6,
    c = 0.07,
    T_max = 1799,
    C = 298,
    alfa = 10.6e-6,
    p = 4472,
    G = 26e9
    )

zirconium = Material(
    stress_critical = 330e6,
    c = 0.08,
    T_max = 2128,
    C = 278,
    alfa = 5.7e-6,
    p = 6506,
    G = 33e9
    )

kadmium = Material(
    stress_critical = 75e6,
    c = 0.04,
    T_max = 594,
    C = 231,
    alfa = 30.8e-6,
    p = 8650,
    G = 19e9
    )


materials ={
    "steel": steel,
    "aluminum": aluminum,
    "titanium": titanium,
    "ferrum": ferrum,
    "argentum": argentum,
    "cuprum": cuprum,
    "magnesium": magnesium,
    "kalium": kalium,
    "calcium": calcium,
    "chromium": chromium,
    "cobaltum": cobaltum,
    "niccolum": niccolum,
    "zincum": zincum,
    "manganum": manganum,
    "niobium": niobium,
    "molybdaenum": molybdaenum,
    "palladium": palladium,
    "plumbum": plumbum,
    "platinum": platinum,
    "vanadium": vanadium,
    "scandium": scandium,
    "germanium": germanium,
    "yttrium": yttrium,
    "zirconium": zirconium,
    "kadmium": kadmium
}