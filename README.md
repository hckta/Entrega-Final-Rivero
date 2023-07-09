# Entrega-Final-Rivero

- En este proyecto se propone una pagina web que le permite al usuario acceder a la publicación de 3 tipos de productos, pantalones, remeras y calzados.
- Para ejecutar este proyecto es necesario instalar en su entorno local la configuracion del especificada en el archivo 'requirements.txt'.
Para su instalacion puede ejecutarse el comando 'pip install Django'

- Para la utilizacion de este proyecto debe utilizarse el comando 'python manage.py runserver' de forma que se levante el proyecto en django, luego podran acceder a la web de inicio. 

- Lo primero que debemos realizar en nuestra pantalla de inicio sera el registro de una cuenta ingresando nuestros datos basicos solicitados, luego de eso tendremos acceso nuevamente al inicio, pero esta vez con la posibilidad de editar datos extra de nuestra cuenta como agregar descripcion, un link o un avatar o editar nuestra contraseña. 

- Una vez registrados se nos permitira el acceso para interactuar con 3 modelos; pantalones, remeras y calzados. Se puede acceder a cada uno de estos que nos llevara a su propia vista y template determinado, en donde se podra elegir si se desea publicar un articulo o buscar un articulo especifico mediante un buscador que filtra por el atributo 'color'. Cada uno de estos modelos contara con sus propios atributos color, marca, talle y fecha de publicacion(opcional). Tambien contaran con la posibilidad de eliminar, modificar y ver mas informacion sobre cada uno de los objetos especificos publicados (pantalones;remeras;calzados). El atributo imagen se encuentra en revision


- El proyecto esta abierto a contribuciones en otras branch que no sean main.

- Este es un proyecto basico con estructura MVT que se encuentra en desarrollo. El mismo fue desarrollado por Octavio Nahuel Rivero, principiante en programacion, estudiante de coderhouse en el curso de python comision 43855.