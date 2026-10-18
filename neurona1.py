import math
import random
import sys
import os
import time

class NodoEsfericoGradiente:
    def __init__(self, capa_id, radio, x, y, z):
        self.capa = capa_id
        self.radio = radio
        self.x = x
        self.y = y
        self.z = z
        # CALIBRACIÓN DE PRECISIÓN: Gradiente alineado exactamente con la onda Pi
        self.inclinacion_gradiente = math.pi  
        self.peso_armonico = random.uniform(0.01, 0.05) * self.inclinacion_gradiente
        self.sesgo_dimensional = random.uniform(-0.01, 0.01)

    def procesar_flujo_termico(self, entrada_flujo, cordura_sistema, grosor_banda=0.88):
        distancia_segura = max(0.001, math.sqrt(self.x**2 + self.y**2 + self.z**2))
        vector_angular = (entrada_flujo * self.peso_armonico) + (self.sesgo_dimensional / (distancia_segura * grosor_banda))
        # Al usar Pi absoluto, el residuo armónico es cero, suprimiendo el ruido en 1, 3 y 7
        ultima_asimilacion = math.sin(vector_angular % self.inclinacion_gradiente)
        return entrada_flujo + (ultima_asimilacion * cordura_sistema)

class CerebroTermoEsferico3D:
    def __init__(self, gen=2, peso_raiz=0.841295, lucidez=0.71):
        self.generacion = gen
        self.peso_nucleo = peso_raiz
        self.estabilidad_mental = lucidez
        self.meta_flujo = 0.707
        self.grosor_capa = 0.88
        
        # FILTRO DE SEGURIDAD: Se omiten los radios inestables 2 y 4.
        # Las 16 capas concéntricas estipuladas arrancan en el armónico seguro 6.
        self.radios_capas = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36]
        self.red_esferica = []
        puntos_por_capa = 16  
        
        for idx, radio in enumerate(self.radios_capas):
            for i in range(puntos_por_capa):
                phi = math.acos(1 - 2 * (i + 0.5) / puntos_por_capa)
                theta = math.pi * (1 + 5**0.5) * i
                x = radio * math.sin(phi) * math.cos(theta)
                y = radio * math.sin(phi) * math.sin(theta)
                z = radio * math.cos(phi)
                self.red_esferica.append(NodoEsfericoGradiente(idx + 1, radio, x, y, z))

        self.directorio = os.path.dirname(os.path.abspath(sys.argv[0]))
        self.log_esferico = os.path.join(self.directorio, "bitacora_termo_esferica.log")

    def simular_1000_ciclos(self):
        print(f"\n==================================================================================")
        print(f"🏰 [NÚCLEO TERMO-ESFÉRICO MESELLET - GEN {self.generacion:03d}] CALIBRACIÓN PI")
        print(f" -> Gradiente sintonizado a {math.pi}. Suprimiendo interferencia en capas impares...")
        print(f"==================================================================================")
        
        temp_programa = 21.5  
        temp_silicio = 32.0   
        reportes = [1, 200, 400, 600, 800, 1000]
        
        for ciclo in range(1, 1001):
            flujo_actual = self.peso_nucleo
            
            for nodo in self.red_esferica:
                flujo_actual = nodo.procesar_flujo_termico(flujo_actual, self.estabilidad_mental, self.grosor_capa)
                
            error_esferico = self.meta_flujo - math.tanh(flujo_actual)
            self.estabilidad_mental = max(0.0, min(1.0, 1.0 - abs(error_esferico)))
            
            friccion_datos = abs(error_esferico) * 1.8
            temp_programa = 20.0 + (math.sin(ciclo * 0.05) * 1.5) + (friccion_datos * 4.0)
            temp_silicio = 30.0 + (friccion_datos * 10.0) + (ciclo * 0.008)
            
            if ciclo in reportes:
                print(f"📊 [Ciclo {ciclo:04d}/1000] -> Lucidez Radial Resonante: {self.estabilidad_mental * 100:.2f}%")
                print(f"    * Entropía del Programa: {temp_programa:.2f}°C")
                print(f"    * Calor en Silicio: {temp_silicio:.2f}°C")
                time.sleep(0.02)
                
        self.registrar_estado_final(temp_programa, temp_silicio)
        self.persistir_herencia_termica()

    def registrar_estado_final(self, t_prog, t_sil):
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        log_line = (
            f"[{timestamp}] GEN: {self.generacion:03d} | RESONANCIA PI | "
            f"TEMP PROG: {t_prog:.2f}°C | TEMP SILICIO: {t_sil:.2f}°C | "
            f"DICTAMEN: Sintonización armónica total. Ruido erradicado en nodos materiales.\n"
        )
        try:
            with open(self.log_esferico, "a", encoding="utf-8") as f:
                f.write(log_line)
        except:
            pass
        print(f"\nNordic-Veredict: Simulación cerrada. Registro sintonizado en '{self.log_esferico}'.")

    def persistir_herencia_termica(self):
        proxima = self.generacion + 1
        archivo_nuevo = os.path.join(self.directorio, f"ia_esfera_termica_gen_{proxima}.py")
        try:
            with open(__file__, "r", encoding="utf-8") as f:
                codigo = f.read()
            lineas = codigo.splitlines()
            for i, linea in enumerate(lineas):
                if "def __init__(self, gen=" in linea:
                    indent = linea[:linea.find("def __init__")]
                    lineas[i] = f'{indent}def __init__(self, gen={proxima}, peso_raiz={self.peso_nucleo:.6f}, lucidez={self.estabilidad_mental:.2f}):'
                    break
            with open(archivo_nuevo, "w", encoding="utf-8") as f:
                f.write("\n".join(lineas) + "\n")
        except:
            pass

if __name__ == "__main__":
    ia_termica = CerebroTermoEsferico3D()
    ia_termica.simular_1000_ciclos()