# **Corrector Ortográfico en Python**

## **Integrantes**
- Emanuel Chavarría  
- Santiago Estrada  
- Curso: Fundamentos de Programación  
- Fecha: 28 de mayo de 2025  

---

## **Introducción**

Este proyecto consiste en un corrector ortográfico para palabras en español que permite verificar si una palabra está escrita correctamente y ofrece sugerencias para corregir errores ortográficos. Además, incluye una función opcional para pronunciar la palabra ingresada o la sugerida, usando síntesis de voz. El objetivo es reforzar el uso de librerías externas, procesamiento de texto y manejo de interfaces básicas en consola.

---

## **Diseño y Arquitectura**

El programa está compuesto por:

- **Clase `CorrectorOrtografico`:**
  - Inicializa el corrector de palabras usando la librería `spellchecker` con soporte para español.
  - Configura un motor de síntesis de voz (`pyttsx3`) para pronunciar palabras.
  - Métodos principales:
    - `verificar_palabra(palabra)`: Evalúa si la palabra está escrita correctamente, limpiándola de caracteres especiales y comparándola con el diccionario. Si la palabra es incorrecta, genera hasta 5 sugerencias de corrección ordenadas por frecuencia de uso.
    - `pronunciar_palabra(palabra)`: Pronuncia la palabra usando el motor de síntesis de voz.

- **Funciones auxiliares:**
  - `mostrar_menu()`: Presenta un menú simple en consola para verificar palabras o salir.
  - `main()`: Controla el flujo principal de la aplicación, interactuando con el usuario.

**Dependencias:**  
- `pyspellchecker` para corrección ortográfica.  
- `pyttsx3` para síntesis de voz.  

---

## **Manual de Usuario**

### **Requisitos**

- Python 3.x instalado.
- Instalar dependencias con:

### **Ejecución**

1. Abrir una terminal o consola.
2. Navegar al directorio donde está el archivo `.py`.
3. Ejecutar el programa con:


### **Uso**

- Al ejecutar, se muestra un menú con dos opciones:
- `1`: Ingresar una palabra para verificar su ortografía.
- `2`: Salir del programa.
- Si la palabra está correcta, se informa y se pronuncia.
- Si la palabra tiene errores, se muestran hasta 5 sugerencias y se pronuncia la primera.

---

## **Desafíos y Lecciones Aprendidas**

- Integrar y configurar librerías externas para corrección ortográfica y síntesis de voz.
- Manejo de caracteres especiales y normalización de texto para evitar falsos positivos en la corrección.
- Implementar un menú sencillo para mejorar la interacción en consola.
- Aprender a manejar excepciones para evitar fallos en la pronunciación o configuración del motor de voz.

---

## **Conclusiones**

El proyecto es un ejemplo funcional de un corrector ortográfico básico que combina procesamiento de texto con salida de voz, ofreciendo una experiencia interactiva. Se logró integrar herramientas útiles para el análisis de texto en español y se mejoró el manejo de interfaces de usuario en la consola. Como futuras mejoras, se podrían incluir corrección gramatical, análisis de oraciones completas y una interfaz gráfica.