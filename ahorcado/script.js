// ==========================================
// VARIABLES DEL JUEGO
// ==========================================

let palabra = "";

let letrasAdivinadas = [];

let intentos = 6;


// ==========================================
// ELEMENTOS DEL HTML
// ==========================================

// Configuración

const palabraSecreta =
    document.getElementById("palabraSecreta");

const comenzar =
    document.getElementById("comenzar");

const configuracion =
    document.getElementById("configuracion");

const errorConfiguracion =
    document.getElementById("errorConfiguracion");


// Juego

const juegoContainer =
    document.getElementById("juegoContainer");

const palabraHTML =
    document.getElementById("palabra");

const intentosHTML =
    document.getElementById("intentos");

const letraInput =
    document.getElementById("letra");

const botonAdivinar =
    document.getElementById("adivinar");

const mensajeHTML =
    document.getElementById("mensaje");

const letrasHTML =
    document.getElementById("letras");

const botonReiniciar =
    document.getElementById("reiniciar");

const dibujoHTML =
    document.getElementById("dibujo");


// ==========================================
// DIBUJOS DEL AHORCADO
// ==========================================

const dibujos = [

`
  +---+
  |   |
      |
      |
      |
      |
=========
`,

`
  +---+
  |   |
  O   |
      |
      |
      |
=========
`,

`
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
`,

`
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
`,

`
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
`,

`
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
`,

`
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
`

];


// ==========================================
// COMENZAR EL JUEGO
// ==========================================

function comenzarJuego() {

    let palabraIngresada =
        palabraSecreta.value.trim().toLowerCase();


    // Comprobar que se haya escrito algo

    if (palabraIngresada === "") {

        errorConfiguracion.textContent =
            "Debes introducir una palabra.";

        return;
    }


    // Comprobar que solamente contenga letras

    if (!/^[a-záéíóúñ]+$/i.test(palabraIngresada)) {

        errorConfiguracion.textContent =
            "La palabra solamente puede contener letras.";

        return;
    }


    // Guardar la palabra

    palabra = palabraIngresada;


    // Reiniciar variables

    letrasAdivinadas = [];

    intentos = 6;


    // Limpiar mensajes

    errorConfiguracion.textContent = "";

    mensajeHTML.textContent = "";


    // Ocultar configuración

    configuracion.classList.add("oculto");


    // Mostrar juego

    juegoContainer.classList.remove("oculto");


    // Activar botón

    botonAdivinar.disabled = false;


    // Limpiar input

    letraInput.value = "";


    // Actualizar pantalla

    mostrarPalabra();

    actualizarInterfaz();

}


// ==========================================
// MOSTRAR PALABRA
// ==========================================

function mostrarPalabra() {

    let resultado = "";


    for (let letra of palabra) {

        if (letrasAdivinadas.includes(letra)) {

            resultado += letra + " ";

        } else {

            resultado += "_ ";

        }

    }


    palabraHTML.textContent = resultado;

}


// ==========================================
// ACTUALIZAR INTERFAZ
// ==========================================

function actualizarInterfaz() {

    intentosHTML.textContent = intentos;


    letrasHTML.textContent =
        letrasAdivinadas.join(", ");


    dibujoHTML.textContent =
        dibujos[6 - intentos];

}


// ==========================================
// ADIVINAR LETRA
// ==========================================

function adivinarLetra() {

    const letra =
        letraInput.value.trim().toLowerCase();


    // Validar que haya una letra

    if (letra.length !== 1) {

        mensajeHTML.textContent =
            "Introduce solamente una letra.";

        return;
    }


    // Validar que sea una letra

    if (!/^[a-záéíóúñ]$/i.test(letra)) {

        mensajeHTML.textContent =
            "Introduce solamente letras.";

        return;
    }


    // Comprobar si ya fue utilizada

    if (letrasAdivinadas.includes(letra)) {

        mensajeHTML.textContent =
            "Ya utilizaste esa letra.";

        letraInput.value = "";

        return;
    }


    // Guardar la letra

    letrasAdivinadas.push(letra);


    // Comprobar si la letra está en la palabra

    if (palabra.includes(letra)) {

        mensajeHTML.textContent =
            "¡Correcto! La letra está en la palabra.";

    } else {

        intentos--;

        mensajeHTML.textContent =
            "Incorrecto. Esa letra no está en la palabra.";

    }


    // Actualizar interfaz

    mostrarPalabra();

    actualizarInterfaz();


    // Comprobar resultado

    comprobarResultado();


    // Limpiar input

    letraInput.value = "";

}


// ==========================================
// COMPROBAR SI GANÓ O PERDIÓ
// ==========================================

function comprobarResultado() {

    let gano = true;


    // Revisar todas las letras de la palabra

    for (let letra of palabra) {

        if (!letrasAdivinadas.includes(letra)) {

            gano = false;

            break;

        }

    }


    // Si ganó

    if (gano) {

        mensajeHTML.textContent =
            "🎉 ¡Ganaste! Adivinaste la palabra.";

        botonAdivinar.disabled = true;

        return;

    }


    // Si perdió

    if (intentos === 0) {

        mensajeHTML.textContent =
            "💀 ¡Perdiste! La palabra era: " + palabra;

        botonAdivinar.disabled = true;

    }

}


// ==========================================
// NUEVA PARTIDA
// ==========================================

function nuevaPartida() {

    // Ocultar juego

    juegoContainer.classList.add("oculto");


    // Mostrar configuración

    configuracion.classList.remove("oculto");


    // Limpiar palabra

    palabraSecreta.value = "";

    errorConfiguracion.textContent = "";


    // Limpiar variables

    palabra = "";

    letrasAdivinadas = [];

    intentos = 6;

}


// ==========================================
// EVENTOS
// ==========================================


// Botón "Comenzar juego"

comenzar.addEventListener(
    "click",
    comenzarJuego
);


// Botón "Adivinar"

botonAdivinar.addEventListener(
    "click",
    adivinarLetra
);


// Botón "Nueva partida"

botonReiniciar.addEventListener(
    "click",
    nuevaPartida
);


// Permitir presionar Enter para adivinar

letraInput.addEventListener(
    "keydown",
    function(event) {

        if (event.key === "Enter") {

            adivinarLetra();

        }

    }
);