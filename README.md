<h1> Compilador HTMCode</h1>
<h2> Documentos Importantes </h2>
<h3> Propuesta </ h3>
Documento de la [propuesta](https://docs.google.com/document/d/1rsTjxqTfrrDu48KNuJDZXyhhyCyiaCX2iZMKbtrCpEA/edit?usp=sharing).
<h3> Demo </ h3>
[demo](https://youtu.be/g9JrWNcM5tA).
<h3> Documentacion </ h3>
[documentación](https://docs.google.com/document/d/e/2PACX-1vQwxL22XCo_WyjRrsN4OBeYc6BKY_IS_VUBE9iB2TabcEBEJxFah6xPtrELNbEEJT-JlafdrST6EoFS/pub).


<h2> Instalación </ h2>
Primero instalar los requerimientos de python con el comando: pip install -r requirements.txt
Luego ejecutar el archivo main.py con el comando: python main.py
En ese comando lo primero que se correra va a ser el manual de usuario, por lo que si se corre el documento website/Help/index.html en el buscador se podra ver el manual de usuario.

<h2> Manual de usuario </h2>
Para probar las distintas pruebas que se encuentran en el folder de pruebas se tiene que cambiar el valor de test en el main.py
Si se elimina el manual de usuario, solo basta con volver a correr el help.txt para poder volver a verlo

<h1> Avances </h1>


<h2> Avance 2 </h2>
Se tiene una gramatica, el scanner y el parse
Se tiene una clase de funciones, directorio de funciones, puntos neuralgicos, cubo semantico, variables y tabla de variables con sus respectivas funciones.
Se tiene un archivo de prueba con exito y un archivo de prueba con error.
Se genera un archivo de salida con el arbol de sintaxis.

<h2> Avance 3 </h2>
Se realizan los cuadruplos de las expresiones aritmeticas, logicas y relacionales.
Se realizan los cuadruplos del IF y de la declaracion de variables, lectura y asignacion de valores.

<h2> Avance 4 </h2>
Se realizan los cuadruplos del while y for

<h2> Avance 5 </h2>
Existen unos problemas en el momento de tener un for dentro de un if, no se rellenan los cuadruplos correctamente.
Existe un archivo de puntos neuralgicos y una copia de este mismo, ya que voy a refactorizar el codigo para que sea mas legible  y tenga una mejor documentacion para encontrar los problemas mas sencillo.

<h2> Avance 6 </h2>
Se refactorizo el codigo para que sea mas legible y simple. 
Se corrigieron los errores de los cuadruplos de los for dentro de un if.
Se añadio la maquina virtual, la memoria virtual y se escriben en un documento de texto las constantes creadas en compilacion, para tener acceso a ellas de manera global y asi evitar que se repitan.
La maquina virtual ya realiza las expresiones aritmeticas basicas
