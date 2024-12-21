
function incrementarNumero()
{
    numeroEditar = document.getElementById('numeroEditar')
    nuevoNumero = String(Number(numeroEditar.innerHTML) + 1)
    numeroEditar.innerHTML = nuevoNumero
}

function disminuirNumero()
{
    numeroEditar = document.getElementById('numeroEditar')
    nuevoNumero = String(Number(numeroEditar.innerHTML) - 1)
    numeroEditar.innerHTML = nuevoNumero
}

function cargarNumero()
{
    valorNumero = document.getElementById('valorNumero')
    obj1 = document.getElementById('numSeleccionado')
    obj1.value = String(valorNumero.value)
}

function agregarNumero()
{
    obj1 = document.getElementById('valorNumero')
    listaNumeros = document.getElementById('listaNumeros')
    listaNumeros.innerHTML += `<li class='numInfo'>${obj1.value}</li>`
}

function actualizarSuma()
{
    arregloNumeros = document.querySelectorAll('.numInfo')
    sumaTotal = 0
    for(i = 0; i < arregloNumeros.length; i++)
    {
        numTemp = Number(arregloNumeros[i].innerHTML)
        sumaTotal = sumaTotal + numTemp
    }
    sumaFinal = document.getElementById('sumaFinal')
    sumaFinal.innerHTML = String(sumaTotal)
}