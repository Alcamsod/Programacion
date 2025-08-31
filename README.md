# Web scraping
https://naturmetica.com/tienda/?gad_source=1&gad_campaignid=22550522311&gbraid=0AAAAAoih_1sicPVCz99LlZDEoTqOuweR_&gclid=Cj0KCQjw5c_FBhDJARIsAIcmHK9uiumLugXG8wzOJSlc9Cip_3ADwtCFMk-CQ_YZFiFeK5QqW8pL2I8aAuu4EALw_wcB

El ejercicio en esta parte va a ser algo quizás no tan práctico pero sin más visual y entretenido, de manera que podamos ver la potencia de ciertas liberias, como selenium por ejemplo. En este caso las liberias no vienen preinstaladas por lo que vamos a hacer uso de lo que se llama un archivo ``requirements``, (el nombre es una convención).

Para instalar paquetes se puede ir a la terminal y ejecutar `pip install NOMBRE` o se pueden introducir todos en un archivo y así no tienes que ir uno por uno.

⚠️ Esto se puede hacer directamente, pero una de las prácticas más seguras es crear un entorno virtual. Me explico.

Los paquetes tienen distinas versiones, pues se van actualizando, pero por eso mismo se pueden dar incompatibilidades entre ellos, por eso si vas instalando todos en el visual code lo más probable es que se den estos problemas entre estos. Para ello estan los **entornos virtuales**

## Entornos viruales

La idea es muy sencilla, simplemente creas una carpeta en la que se almacenan las liberías que descargas, ahí se pueden ver perfectamente los códigos que las forman, funciones, incluso modificarlas. Para ello hay dos formas

- Visual code trae consigo una función en la interfaz que te permite crear el entorno

- Por la terminal, ejecutando `py -Version .venv nombre` se crea un entorno virtual.

Una vez creado, para instalar cosas hay que activarlos. Esto permite crear varios distintos e ir pasando de uno a otro.