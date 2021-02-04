# INFO_SOCIAL
Proyecto de informática Social.


## Instrucciones de instalación:

En primera instancia se requiere tener un IDE para ejecutar y manipular el proyecto, el cual está desarrollado en el framework Django, escrito bajo Python. Para este proyecto se recomienda utilizar <strong>PyCharm</strong> de Jetbrains y en adición se necesita tener instalado Anaconda en el sistema para el control y manejo de recursos y herramientas de Python, incluyendo el entorno virtual que se requiere parasu ejecución local.

Los pasos de instalación y ejecución son los siguientes:

<ul>
<li> Ejecutar PyCharm y usar la opción de abrir proyecto desde control de versiones (<i>Version control</i> o <i>VCS</i>).</li>
<li> Dentro del panel <i>VCS</i> colocar la url del repositorio GIT del proyecto para comenzar su clonado, posterior a esto PyCharm abrirá el editor con el proeycto y todos sus recursos.</li>
<li> Agregar un interprete al proyecto, esto se hace desde la opción en la esquina inferior derecha y se requiere agregar un interprete Anaconda que posea python 3.8 o superior.</li>
<li> Luego en el apartado de terminal instalar los recursos del proyecto, esto se hace con el siguiente comando:</li><br>
   
     pip install -r requirements.txt
  
<li> Luego de instalar los recursos, el proyecto puede ejecutarse con el siguiente comando: </li><br>
    
    python manage.py runserver

<li> Posterior a ello el portal ya quedaría en ejecución localmente.
</ul>

Nota: la ejecución no es requerida si solo se quiere hacer revisión del código, además estas instrucciones solo son para la instalación y uso con PyCharm y Anaconda, si se desea, se puede usar otro IDE e inclusive otro administrador de entornos virtuales (como Virtualenv) 🤷‍♂️.
