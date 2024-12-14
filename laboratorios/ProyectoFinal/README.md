<div align="center">
<table>
    <theader>
        <tr>
            <td style="width:25%;"><img src="https://github.com/rescobedoq/pw2/blob/main/epis.png?raw=true" alt="EPIS" style="width:80%; height:auto"/></td>
            <td>
                <span style="font-weight:bold;">UNIVERSIDAD NACIONAL DE SAN AGUSTIN</span><br />
                <span style="font-weight:bold;">FACULTAD DE INGENIERÍA DE PRODUCCIÓN Y SERVICIOS</span><br />
                <span style="font-weight:bold;">DEPARTAMENTO ACADÉMICO DE INGENIERÍA DE SISTEMAS E INFORMÁTICA</span><br />
                <span style="font-weight:bold;">ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS</span>
            </td>            
        </tr>
    </theader>
    <tbody>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Proyecto web</span>: Desarrollo de una aplicación web para una biblioteca virtual</td>
        </tr>
        <tr>
        <td colspan="2"><span style="font-weight:bold;">Fecha</span>:  2022/28/07</td>
        </tr>
    </tbody>
</table>
</div>

<div align="center">
<span style="font-weight:bold;">PROYECTO WEB: LIBON</span><br />
</div>


<table>
<theader>
<tr><th>INFORMACIÓN BÁSICA</th></tr>
</theader>
<tbody>
    <tr>
        <td>ASIGNATURA:</td><td>Programación Web 2</td>
    </tr>
    <tr>
        <td>SEMESTRE:</td><td>III</td>
    </tr>
    <tr>
        <td>FECHA INICIO:</td><td>18-Jul-2024</td><td>FECHA FIN:</td>
        <td>28-Jul-2024</td><td>DURACIÓN:</td><td>04 horas</td>
    </tr>
    <tr>
        <td colspan="3">DOCENTES:
        <ul>
        <li>Lino pinto</li>
        </ul>
        </td>
    </<tr>
      <tr>
        <td colspan="3">Alumno:
        <ul>
        <li>Mendoza Contreras Giovani Angel - gmendozaco@unsa.edu.pe</li>
        </ul>
        </td>
    </<tr>
</tdbody>
</table>

#   WebApp con Django

##  Tipo de Sistema
    Se trata de una aplicación web con un backend construido en el framework Django 4 y para el frontend usamos vue js 3 
    estas son las dos tecnologias que usamos en el proyecto, nuestro proyecto permite poder visualizar los diferentes ejemplares 
    con temas y categorias del interes del usuario en el cual el usuario podra reservar su ejemplar una ves ya haya creado 
    su cuenta pues este podra crear una cuenta y asi mismo logearse para poder hacer la reserva del ejemplar en el que este 
    interesado.

##  Requisitos del sistema
    El sistema debe satisfacer los siguientes requisitos funcionales y no funcionales:

    - RQ01 : El sistema esta disponible en Internet a traves de una URL.
    - RQ02 : El sistema debe permitir el inicio/cierre de sesión.
    - RQ03 : El sistema debe permitir poder visualizar los ejemplares antes de ser logeado con detalles como podria ser el autor 
             categoria, tema, precio.
    - RQ04 : El sistema brinda una busqueda por tema, nombre del ejemplar, categoria, autor.
    - RQ05 : Se podra hacer click socbre el ejemplar para ver mas detalles acerca de este, como tambien en los autores en los cuales 
             se puede ver acerca de este.
    - RQ06 : Una ves logeado el usuario podra visualizar botones con los cuales podra reservar su libro.
    - RQ07 : El sistema brindara seguridad al momento de manejar los datos usuario.

##  Modelo de datos
    El modelo de datos esta conformado por las siguientes entidades.

    -   Autor : En esta tabla tendremos el nombre del autor, su respectiva imagen, y detalles como su nacionalidad y 
    biografia ademas de los campos para hacer un seguimiento del objeto en cuestion.
    -   Boleta : En esta tabla podremos ver el cliente como tambien que tipo de accion como venta o prestamo, el pago 
    y los respectivos campos de seguimiento del objeto. 
    -   Carrito : En esta entidad tendremos al cliente, el ejemplar y los campos de seguimiento.
    -   Categoria : En esta tabla tendremos el nombre de la categoria con los campos de seguimiento.
    -   Ejemplar : En esta tabla tendremos el titulo, imagen del ejemplar, su categoria, tema, año, autor, sinopsis, 
    paginas, stock, 
    precio y los campos de seguimiento.
    -   Historial : Esta tabla contiene al cliente, si es duedor, los ejemplares que llevo, sus boletas y los campos de 
    seguimiento
    -   Prestamo : En esta tabla tenemos el ejemplar, cliente, fecha de devolucion y los campos de seguimiento. 
    -   Tema : Tenemos en esta tabla el nombre del tema y los campos de seguimiento.
    -   Usuario : En esta tabla tenemos al nombre de usuario, password, email, nombres, apellidos, dni, telefono, direccion 
    y los campos de seguimiento. 

##  Diccionario de datos

| Autor | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| id  | Numerico| No | Si | Ninguno | Código |
| nombre  | Cadena | No | No | Ninguno | Nombre |
| imagen  | Image | No | No | Ninguno | imagen |
| nacionalidad  | Cadena| No | No | Ninguno | Nacionalidad |
| biografia  | Cadena| No | No | Ninguno | Biografia |
| status  | Boolean | No | No | Ninguno | Estado |
| created  | Date | No | No | Ninguno | Fecha de creacion |
| modified  | Date | No | No | Ninguno | Fecha de modificacion |
| user_created  | Relacion | No | No | Ninguno | Creado por |
| user_modified  | Relacion | No | No | Ninguno | Modificado por |


| Boleta | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| id  | Numerico| No | Si | Ninguno | Código |
| cliente | Relacion | No | No | Ninguno | Nombre del cliente |
| ventas | Relacion | Si | No | Ninguno | Tipo de accion |
| prestamos | Relacion | Si | No | NULL | Tipo de accion |
| pago | double | Si | No | NULL | Tipo de accion |
| status  | Boolean | No | No | Ninguno | Estado |
| created  | Date | No | No | Ninguno | Fecha de creacion |
| modified  | Date | No | No | Ninguno | Fecha de modificacion |
| user_created  | Relacion | No | No | Ninguno | Creado por |
| user_modified  | Relacion | No | No | Ninguno | Modificado por |


| Carrito | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| id  | Numerico| No | Si | Ninguno | Código |
| cliente | Relacion | No | No | Ninguno | Nombre del cliente |
| ejemplar | Relacion | Si | No | Ninguno | Tipo de accion |
| status  | Boolean | No | No | Ninguno | Estado |
| created  | Date | No | No | Ninguno | Fecha de creacion |
| modified  | Date | No | No | Ninguno | Fecha de modificacion |
| user_created  | Relacion | No | No | Ninguno | Creado por |
| user_modified  | Relacion | No | No | Ninguno | Modificado por |


| Categoria | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| id  | Numerico| No | Si | Ninguno | Código |
| nombre | Cadena | No | No | Ninguno | Nombre de la categoria |
| status  | Boolean | No | No | Ninguno | Estado |
| created  | Date | No | No | Ninguno | Fecha de creacion |
| modified  | Date | No | No | Ninguno | Fecha de modificacion |
| user_created  | Relacion | No | No | Ninguno | Creado por |
| user_modified  | Relacion | No | No | Ninguno | Modificado por |


| Ejemplar | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| id  | Numerico| No | Si | Ninguno | Código |
| titulo  | Cadena | No | No | Ninguno | Nombre |
| imagen  | Image | No | No | Ninguno | imagen |
| categoria  | Cadena | No | No | Ninguno | Tipo de categoria |
| tema  | Cadena | No | No | Ninguno | Tipo de tema |
| año  | Cadena | No | No | Ninguno | año publicado |
| autor  | Relacion | No | No | Ninguno | Nombre del autor |
| sinopsis  | Cadena | No | No | Ninguno | Resumen |
| paginas  | Integer | No | No | Ninguno | Numero de paginas |
| stock  | Integer | No | No | Ninguno | Cantidad |
| precio  | Double | No | No | Ninguno | Costo |
| status  | Boolean | No | No | Ninguno | Estado |
| created  | Date | No | No | Ninguno | Fecha de creacion |
| modified  | Date | No | No | Ninguno | Fecha de modificacion |
| user_created  | Relacion | No | No | Ninguno | Creado por |
| user_modified  | Relacion | No | No | Ninguno | Modificado por |


| Historial | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| id  | Numerico| No | Si | Ninguno | Código |
| cliente | Relacion | No | No | Ninguno | Nombre del cliente |
| deudor | Boolean | Si | No | Ninguno | Penalidad |
| ejemplares | Relacion | Si | No | NULL | relacion de ejemplares |
| boletas | Relacion | Si | No | NULL | Relacion de boletas |
| status  | Boolean | No | No | Ninguno | Estado |
| created  | Date | No | No | Ninguno | Fecha de creacion |
| modified  | Date | No | No | Ninguno | Fecha de modificacion |
| user_created  | Relacion | No | No | Ninguno | Creado por |
| user_modified  | Relacion | No | No | Ninguno | Modificado por |


| Tema | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| id  | Numerico| No | Si | Ninguno | Código |
| nombre | Cadena | No | No | Ninguno | Nombre del tema |
| status  | Boolean | No | No | Ninguno | Estado |
| created  | Date | No | No | Ninguno | Fecha de creacion |
| modified  | Date | No | No | Ninguno | Fecha de modificacion |
| user_created  | Relacion | No | No | Ninguno | Creado por |
| user_modified  | Relacion | No | No | Ninguno | Modificado por |


| Ejemplar | | | | | |
| -- | -- | -- | -- | -- | -- |
| Atributo  | Tipo  | Nulo | Clave | Predeterminado | Descripción |
| id  | Numerico| No | Si | Ninguno | Código |
| username  | Cadena | No | No | Ninguno | Nombre de usuario |
| password  | password | No | No | Ninguno | Contraseña |
| email  | Email | No | No | Ninguno | Correo |
| first_name  | Cadena | No | No | Ninguno | Nombre |
| last_name  | Cadena | No | No | Ninguno | Apellidos |
| dni  | Cadena | No | No | Ninguno | Nro de identidad |
| telefono  | Cadena | No | No | Ninguno | Nro de telefono |
| direccion  | Cadena | No | No | Ninguno | Referencia |
| status  | Boolean | No | No | Ninguno | Estado |
| created  | Date | No | No | Ninguno | Fecha de creacion |
| modified  | Date | No | No | Ninguno | Fecha de modificacion |
| user_created  | Relacion | No | No | Ninguno | Creado por |
| user_modified  | Relacion | No | No | Ninguno | Modificado por |

##  Diagrama Entidad-Relación
    
    1. Autor: Esta tabla tiene relacion de muchos a uno con los campos user_created y user modified pues se relaciona 
    con los usuarios que los crean o los modifiquen.
    
    2. Boleta: Tiene relacion de muchos a muchos con ventas y prestamos, tiene relacion de muchos a uno con los campos 
    user_created y user modified pues se relaciona con los usuarios que los crean o los modifiquen.
    
    3. Carrito: Relacion de uno a uno con el usuario y de muchos a muchos con el ejemplar tiene relacion de muchos a 
    uno con los campos user_created y user modified pues se relaciona con los usuarios que los crean o los modifiquen.
    
    4. Categoria : tiene relacion de muchos a uno con los campos user_created y user modified pues se relaciona con los 
    usuarios que los crean o los modifiquen.
    
    5. Ejemplar : Se relaciona con categoria de muchos a uno, con tema de muchos a muchos, autor de muchos a muchos, 
    tiene relacion de muchos a uno con los campos user_created y user modified pues se relaciona con los usuarios que 
    los crean o los modifiquen.
    
    6. Historial : Se relaciona con cliente de uno a uno, ejemplares de muchos a muchos, boletas de muchos a muchos, 
    tiene relacion de muchos a uno con los campos user_created y user modified pues se relaciona con los usuarios que 
    los crean o los modifiquen.
    
    7. Prestamos : Se relaciona con ejemplares de muchos a uno, con cliente de muchos a uno, tiene relacion de muchos 
    a uno con los campos user_created y user modified pues se relaciona con los usuarios que los crean o los modifiquen.
    
    8. Tema : tiene relacion de muchos a uno con los campos user_created y user modified pues se relaciona con los usuarios 
    que los crean o los modifiquen.
    
    9. Usuario : Esta tabla se relaciona con todos los demas.
    
    10. Venta : Se relaciona con cliente de uno a uno, ejemplar de uno a uno, tiene relacion de muchos a uno con los campos 
    user_created y user modified pues se relaciona con los usuarios que los crean o los modifiquen.

