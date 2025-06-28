# TuPrimeraPaginaQuintero

Este es un proyecto web desarrollado con **Django** como parte de la entrega final del curso. La aplicación es un blog funcional donde los usuarios pueden registrarse, crear publicaciones con imágenes, enviar mensajes, editar su perfil, y navegar por distintas páginas como "Acerca de mí" o un listado filtrado de publicaciones.

## 🚀 Funcionalidades principales

- Registro, login y logout de usuarios
- Vista de perfil y edición de datos personales (incluye avatar)
- Crear, editar y eliminar publicaciones (con imágenes y categorías)
- Vista de detalle de cada publicación
- Búsqueda por título y filtrado por categoría
- Vista “Acerca de mí”
- Mensajería entre usuarios
- Uso de `CKEditor` para contenido enriquecido
- Sistema de navegación con `base.html` y Bootstrap 5
- Seguridad con decoradores y mixins en vistas protegidas

## 🛠️ Tecnologías utilizadas

- Python 3.13
- Django 5.2
- SQLite3
- Bootstrap 5
- CKEditor
- HTML + CSS
- Git & GitHub


## 📁 Estructura del proyecto

- `Miapp/` → Modelo principal (Post), categorías, vistas generales
- `accounts/` → Registro, login, perfil
- `messaging/` → Mensajes entre usuarios
- `media/` → Imágenes subidas por los usuarios (no incluida en el repo)
- `static/` → Archivos estáticos (Bootstrap, CSS)
- `templates/` → Herencia con `base.html`, páginas específicas

---

## 🧾 Notas

- El archivo `db.sqlite3` y la carpeta `media/` están excluidos del repositorio con `.gitignore`
- Compatible con desarrollo local. Para producción se requiere configuración adicional.


---

## 👨‍💻 Autor

**Gabriel Quintero**  
[GitHub](https://github.com/G4briel4224)
