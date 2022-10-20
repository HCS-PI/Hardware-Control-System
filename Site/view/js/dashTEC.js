function atualizar() {
    window.location = "/dashTEC.html";
}

function monitorados() {
    var idEmpresa = sessionStorage.ID_EMPRESA;

    fetch("/dashTecnico/carrosMonitorados", {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            idEmpresa: idEmpresa
        })
    }).then(function (resposta) {
        if (resposta.ok) {

            resposta.json().then(json => {

                for (var index = 0; index < json.length; index++) {
                    numCarros = json[index].qtdCarro
                    numCarrosSendoMonitorados.innerHTML = `${numCarros}`
                }
            })
        }
    })
}

function verCarros() {
    var idEmpresa = sessionStorage.ID_EMPRESA;

    fetch("/dashTecnico/verCarros", {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            idEmpresa: idEmpresa
        })
    }).then(function (resposta) {
        if (resposta.ok) {
            cardCarros.innerHTML = ''
            critico = 0
            resposta.json().then(json => {
                numDiv = 1
                for (var index = 0; index < json.length; index++) {
                    idCarro = json[index].IdCarro
                    modelo = json[index].Modelo
                    placa = json[index].Placa
                    problema = json[index].Componente
                    Valor = json[index].Valor


                    if (Valor >= 80 && Valor < 90) {
                        estadoRam = 'Alerta'
                    } else if (Valor > 90) {
                        estadoRam = 'Critico'
                        critico++
                    }

                    if (Valor >= 70 && Valor < 90) {
                        estadoCpu = 'Alerta'
                    } else if (Valor > 90) {
                        estadoCpu = 'Critico'
                        critico++
                    }

                    if (problema == "RAM" && Valor > 40.0) {
                        cardCarros.innerHTML +=
                            `<div class="carro carro${numDiv}">
                                <ul class="ulTitulo" >
                                <li>Placa</li>
                                <li>Modelo</li>
                                <li>Problema</li>
                                <li>Estado</li>
                            </ul>
                            <ul class="ulDescricao">
                                <div class="placaCarro">${placa}</div>
                                <div class="modeloCarro">${modelo}</div>
                                <div class="itemComProblema">${problema} -${Valor}%</div>
                                <div class="estadoCarro">${estadoRam}</div>
                            </ul>
                        </div>`
                    }
                    if (problema == "CPU" && Valor > 40.0) {
                        cardCarros.innerHTML +=
                            `<div class="carro carro${numDiv}">
                            <ul class="ulTitulo" >
                                <li>Placa</li>
                                <li>Modelo</li>
                                <li>Problema</li>
                                <li>Estado</li>
                            </ul>
                            <ul class="ulDescricao">
                            <div class="placaCarro">${placa}</div>
                            <div class="modeloCarro">${modelo}</div>
                            <div class="itemComProblema">${problema} - ${Valor}%</div>
                            <div class="estadoCarro">${estadoRam}</div>
                            </ul>
                        </div>`
                    }

                    if (numDiv == 1) {
                        numDiv = 2
                    } else {
                        numDiv = 1
                    }
                    carrosCriticos.innerHTML = critico
                }
            })

        }
    })

}
