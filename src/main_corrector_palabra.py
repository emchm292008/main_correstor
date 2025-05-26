import re
from spellchecker import SpellChecker
import pyttsx3

class CorrectorOrtografico:
    def _init_(self):
        self.spell = SpellChecker(language='es')
        self.engine = pyttsx3.init()
        self.errores_corregidos = 0
        
        # Configuración de voz
        try:
            voices = self.engine.getProperty('voices')
            self.engine.setProperty('voice', voices[0].id)
            self.engine.setProperty('rate', 150)
        except:
            print("(Advertencia: No se pudo configurar la voz)")

    def verificar_palabra(self, palabra):
        """
        Verifica si una palabra está bien escrita y ofrece sugerencias si es necesario
        """
        # Limpiar la palabra de caracteres especiales (excepto tildes y ñ)
        palabra_limpia = re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑ]', '', palabra)
        
        if not palabra_limpia:
            return {"correcta": True, "original": palabra, "sugerencias": []}
        
        # Verificar si la palabra es correcta
        palabra_correcta = self.spell.correction(palabra_limpia) == palabra_limpia
        
        if palabra_correcta:
            return {"correcta": True, "original": palabra, "sugerencias": []}
        else:
            # Obtener sugerencias
            sugerencias = self.spell.candidates(palabra_limpia)
            
            # Si no hay sugerencias, usar la corrección automática
            if not sugerencias:
                correccion = self.spell.correction(palabra_limpia)
                sugerencias = {correccion} if correccion else set()
            
            # Ordenar sugerencias por frecuencia de uso
            try:
                sugerencias_ordenadas = sorted(sugerencias, 
                                           key=lambda x: self.spell.word_usage_frequency(x), 
                                           reverse=True)
            except:
                # Si falla el ordenamiento, usar orden arbitrario
                sugerencias_ordenadas = list(sugerencias)
            
            # Limitar a 5 sugerencias
            sugerencias_ordenadas = sugerencias_ordenadas[:5]
            
            return {
                "correcta": False,
                "original": palabra,
                "sugerencias": sugerencias_ordenadas
            }

    def pronunciar_palabra(self, palabra):
        """Función opcional para pronunciar palabras"""
        try:
            self.engine.say(palabra)
            self.engine.runAndWait()
        except:
            print("(No se pudo pronunciar la palabra)")

def mostrar_menu():
    print("\n=== CORRECTOR ORTOGRÁFICO ===")
    print("1. Verificar una palabra")
    print("2. Salir")
    return input("Seleccione una opción: ")

def main():
    corrector = CorrectorOrtografico()
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            palabra = input("\nIngrese una palabra: ")
            resultado = corrector.verificar_palabra(palabra)
            
            if resultado["correcta"]:
                print(f"✓ La palabra '{palabra}' está correctamente escrita.")
                corrector.pronunciar_palabra(palabra)
            else:
                print(f"✗ La palabra '{palabra}' contiene errores.")
                print("Sugerencias:")
                for i, sug in enumerate(resultado["sugerencias"], 1):
                    print(f"{i}. {sug}")
                
                if resultado["sugerencias"]:
                    corrector.pronunciar_palabra(resultado["sugerencias"][0])
                
        elif opcion == "3":
            texto = input("\nIngrese el texto a corregir: ")
            texto_corregido = corrector.corregir_texto(texto)
            print("\nTexto corregido:")
            print(texto_corregido)
            print(f"\nTotal errores corregidos: {corrector.errores_corregidos}")
            
        elif opcion == "2":
            print("Gracias por usar el corrector ortográfico. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor intente nuevamente.")

if __name__ == "__main__":
    main()
