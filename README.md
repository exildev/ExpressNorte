#Domiciolios Express Del Norte

Plataforma de monitoreo de Domiciliospara al empresa ***Express Del Norte***

#Frameworks / API's
- Django 1.8.2
- [Django Suit](http://djangosuit.com/)

##Instalacion

1. Guardar el archivo [local_settings.py](https://gist.github.com/ivajo26/691a3da8d22fa341637c) dentro del directorio express/
2. Instalar virtualenv ```sudo pip install virtualenv```
3. En el repositorio realizar ```virtualenv env && source env/bin/activate```
4. Instalar todas las dependencias ```pip install -r requiremientos.txt```
5. Migrar la base de datos ```./manage.py migrate```
6. Sincronizar los modelos ```./manage.py syncdb```
7. Correr el servidor ```./manage.py runserver```

##Equipo de Desarrollo
- **Director de Proyecto:** Jose Luis Ahumada
- **Diseñador:** David Paredes
- **Pogramadores:**
  - Deyby Garcia
  - Iván Díaz
