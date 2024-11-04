import openseespy.opensees as op
import numpy as np
import matplotlib.pyplot as plt

# Definir el modelo
op.wipe()
op.model('Basic', '-ndm', 2, '-ndf', 3)

# Definir nodos y apoyos
L = 5.0  # Longitud de la columna
op.node(1, 0.0, 0.0)
op.node(2, 0.0, L)
op.fix(1, 1, 1, 1)
op.fix(2, 0, 1, 0)

# Parámetros de la sección de la columna
fc = 30.0  # MPa
Ec = 5000 * np.sqrt(fc)  # MPa
G = 0.4 * Ec  # Módulo de corte
A = 0.3 * 0.3  # m^2, área de la sección
Iz = (0.3**4) / 12  # m^4, momento de inercia

# Definir material no lineal al cortante (Shear Hinge)
Fy = 0.6 * fc * A  # Capacidad de cortante (ejemplo simple)
K = G * A  # Rigidez al cortante

# Material no lineal para el cortante
op.uniaxialMaterial('Hysteretic', 1, K, Fy, 0.01, -K, -Fy, 0.01, 0.01, 0.01)

# Definir sección no lineal
op.section('Fiber', 1)
op.patch('rect', 1, 10, 1, -0.15, -0.15, 0.15, 0.15)

# Definir elementos con hinge de cortante en los extremos
op.geomTransf('Linear', 1)
op.element('forceBeamColumn', 1, 1, 2, 1, 1)

# Cargar el modelo
P = 500.0  # kN
op.timeSeries('Linear', 1)
op.pattern('Plain', 1, 1)
op.load(2, 0, -P, 0)

# Definir el análisis
op.system('BandGeneral')
op.numberer('Plain')
op.constraints('Plain')
op.integrator('LoadControl', 0.1)
op.algorithm('Newton')
op.analysis('Static')

# Ejecutar el análisis
op.analyze(10)

# Extraer los resultados
shear_force = op.eleResponse(1, 'force')  # Obtener fuerzas en el elemento

# Visualizar resultados (esfuerzo cortante)
print("Fuerza de Cortante: ", shear_force)

# Gráfica de cortante
plt.plot(shear_force, label='Fuerza de Cortante')
plt.xlabel('Paso')
plt.ylabel('Cortante (kN)')
plt.legend()
plt.show()

# Limpiar el modelo
op.wipe()
arreglar elerror en la linea 28
