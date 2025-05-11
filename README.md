
# 👾 Alien Invasion

Este es un juego arcade desarrollado en Python usando la biblioteca **PyGame**. El jugador controla una nave espacial que debe disparar a múltiples tipos de naves enemigas, ganar puntos y evitar colisiones. El proyecto fue desarrollado como parte de una prueba práctica para la plataforma **Kodland**.

---

## 🧠 Objetivos del Proyecto

- Desarrollar un videojuego básico en PyGame.
- Aplicar conceptos de programación estructurada y orientada a objetos.
- Crear interfaces con menús interactivos.
- Contar score, disparos y enemigos eliminados.
- Implementar múltiples tipos de enemigos.

---

## 📂 Estructura del Proyecto

```
alien_invasion/
├── main.py                # Punto de entrada principal del juego
├── jugador.py             # Clase del jugador (Player)
├── enemigo.py             # Clase base y subclases de enemigos
├── bala.py                # Clase de disparos
├── utils.py               # Funciones auxiliares (mostrar texto, menús)
├── imagenes/
│   ├── nave.png           # Imagen de la nave del jugador
│   ├── enemigo1.png       # Tipo de enemigo 1
│   ├── enemigo2.png       # Tipo de enemigo 2
│   ├── disparo.png        # Imagen del disparo
│   └── fondo.jpg          # Imagen de fondo del juego
```

---

## 🎮 Controles

| Tecla         | Acción                          |
|--------------|----------------------------------|
| ← / →        | Mover la nave                    |
| Barra espaciadora | Disparar                    |
| ESC          | Mostrar menú de pausa/salida     |
| ENTER        | Reanudar el juego desde el menú  |

---

## 🧩 Características

- 🛸 Dos tipos de naves enemigas
- 🔫 Disparos controlados por el jugador
- 🧮 Conteo de score, disparos realizados y enemigos destruidos
- 📜 Menú de inicio y menú de pausa
- 🌌 Imagen de fondo espacial

---

## 📦 Requisitos

- Python 3.10+
- PyGame 2.6+

Instalación de PyGame:

```bash
pip install pygame
```

---

## ▶️ Cómo ejecutar el juego

Ubicado en la carpeta raíz del proyecto, ejecuta:

```bash
python main.py
```

---

## ✍️ Comentarios adicionales

Este proyecto fue desarrollado como parte de una prueba práctica para tutor de Python en **Kodland**. Se implementó una versión sin clases y otra versión con clases separadas para fomentar la comprensión de estructuras más robustas.

---

## 📸 Capturas

![Captura del juego](imagenes/fondo.jpg)

---

## ⚖️ Licencia

Este proyecto es de uso educativo. Puedes modificarlo y reutilizarlo con fines no comerciales.
