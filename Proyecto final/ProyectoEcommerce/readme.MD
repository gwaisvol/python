# Proyecto Final Python - Entrega Final

Proyecto para el curso de Python de Coder House, Comisión 48600.
Hemos creado un ecommerce dedicado a la venta de productos para personas con Alzheimer.

## Para iniciarlo

Situarnos en la carpeta "ProyectoEcommerce", y ejectuar el comando - python manage.py runserver
Previamente nos aseguramos tener instalado django,y demas frameworks necesarios.


## Navegacion

Dentro del proyecto, nos dirijimos al "/home", desde donde podremos elegir por que lugares del sitio navegar!

Ejemplos de urls para navegar sin ir al home:
"Products/list-products/"
"Products/list-categories/"
"/nosotros"
"/cart/list-of-carts/"

## Rangos
No todos los usuarios van a tener los mismos accesos, ya que no es lo mismo la pagina para un usuario "admin", que para un cliente. En el caso de querer registrarnos como un cliente comun, vamos al signup, los hacemos normalmente y ya podemos inciar sesion!

Del lado de admin deberiamos crear un superuser utilizando los comandos en la consola de visual. (python manage.py createsuperuser). En donde tendremos un panel de adminsitracion (personalizado, y otro de django en la url /admin), que nos permitira editar, y eliminar cosas!


## Autores

- Germán Waisvol
- Silvina Noemí Cardoso.

## División de tareas
Silvina Cardoso se encargó de crear el proyecto en Django y subirlo a GitHub. Asi como también la parte fundamental de creación de las App del proyecto: Product, Cart y users, con sus respectivas vistas y paginas HTML. 

Germán Waisvol se encargó de los Unit Tests, armar los mensajes ,la sección Acerca de Nosotros, Bootstrap. También de la elección y la carga del Template base al proyecto. Se encargó de la parte de perfiles de usuario y permisos. Brindo soporte en el seguimiento de las tareas. Y estuvo a cargo del video de demostración.

En todo momento ambos estuvimos en coordinación y en pleno conocimiento de lo que cada uno realizaba, todas las decisiones fueron consensuadas y en cada una de las tareas ambos integrantes tuvieron algún tipo de participación.

## Video con el link explicativo

https://drive.google.com/file/d/1XKtuZd2oZtGygfYni0p_ixBX4692fsPI/view?usp=share_link


Esperamos que les guste.
