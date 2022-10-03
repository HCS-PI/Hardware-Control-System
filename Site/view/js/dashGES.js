setInterval(() => {
    buscarMediaCPUCarros()
    buscarMediaRAMCarros()
}, 1000);


function buscarMediaCPUCarros() {

    vt_ModeloCarrosCPU = [];
    vt_MediasCPU = []

    fetch("/dashGestor/mediaCpuCarros", {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            idEmpresa: sessionStorage.ID_EMPRESA
        })
    }).then(function (resposta) {
        if (resposta.ok) {
            resposta.json().then(json => {

                for (let i = 0; i < json.length; i++) {
                    vt_ModeloCarrosCPU.push(json[i].ModeloCarro);
                    vt_MediasCPU.push(parseFloat((json[i].MediaConsumo)));
                }

                console.log(vt_ModeloCarrosCPU);
                console.log(vt_MediasCPU);

                var porcentagemCategeoriaGraficoCPU = 0
                var porcentagemBarraGraficoCPU =  0 
                if (vt_ModeloCarrosCPU.length < 2) {
                    porcentagemCategeoriaGraficoCPU = 0.2
                    porcentagemBarraGraficoCPU =  0.7
                }
                else {
                    porcentagemCategeoriaGraficoCPU = 0.6
                    porcentagemBarraGraficoCPU =  0.9
                }

                document.getElementById('grafico1').remove();
                novoGraficoCPU = document.createElement('canvas');
                novoGraficoCPU.setAttribute('id', 'grafico1');
                graficoBarraCPU.appendChild(novoGraficoCPU);


                const graficoUsoCPU = [
                    // Colocar aqui o tempo da coleta, estes são os títulos das barras
                    vt_ModeloCarrosCPU[0],
                    vt_ModeloCarrosCPU[1],
                    vt_ModeloCarrosCPU[2],
                    vt_ModeloCarrosCPU[3],
                    vt_ModeloCarrosCPU[4],
                ];


                // Dados do gráfico
                const dados1 = {
                    labels: graficoUsoCPU, // Nome da variável do gráfico
                    datasets: [{
                        label: 'Uso de CPU (%)', // Título
                        categoryPercentage: porcentagemCategeoriaGraficoCPU,
                        barPercentage: porcentagemBarraGraficoCPU, 
                        backgroundColor: '#49a7de', // cor de fundo
                        borderColor: 'black', // cor da borda
                        data: [vt_MediasCPU[0], vt_MediasCPU[1], vt_MediasCPU[2], vt_MediasCPU[3], vt_MediasCPU[4]], // Plot dos valores embaixo das barras
                    },
                    ]
                };

                // Configurações do gráfico
                const config1 = {
                    type: 'bar', // Define para o tipo barra
                    data: dados1, // Diz quais dados serão referentes àquele gráfico
                    options: {
                        scales: {
                            y: {
                                min: 0,
                                max: 100,
                                beginAtZero: true
                            }
                        },
                        animation: 0
                    }
                };

                //Diz qual é a div que receberá o gráfico pronto
                const grafico1 = new Chart(
                    document.getElementById('grafico1'),
                    config1
                );
            })
        }
    })
}


function buscarMediaRAMCarros() {


    vt_ModeloCarrosRAM = [];
    vt_MediasRAM = []

    fetch("/dashGestor/mediaRamCarros", {
        method: 'POST',
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            idEmpresa: sessionStorage.ID_EMPRESA
        })
    }).then(function (resposta) {
        if (resposta.ok) {
            
            resposta.json().then(json => {

                for (let i = 0; i < json.length; i++) {
                    vt_ModeloCarrosRAM.push(json[i].ModeloCarro);
                    vt_MediasRAM.push(parseFloat((json[i].MediaConsumo)));
                }
                var porcentagemCategeoriaGraficoRAM = 0
                var porcentagemBarraGraficoRAM =  0  

                if (vt_ModeloCarrosRAM.length < 2) {
                    porcentagemCategeoriaGraficoRAM = 0.2
                    porcentagemBarraGraficoRAM =  0.7
                }
                else {
                    porcentagemCategeoriaGraficoRAM = 0.6
                    porcentagemBarraGraficoRAM =  0.9
                }

                
                document.getElementById('grafico2').remove();
                novoGraficoRAM = document.createElement('canvas');
                novoGraficoRAM.setAttribute('id', 'grafico2');
                graficoBarraRAM.appendChild(novoGraficoRAM);

                
                const graficoUsoRAM = [
                    // Colocar aqui o tempo da coleta, estes são os títulos das barras
                    vt_ModeloCarrosRAM[0],
                    vt_ModeloCarrosRAM[1],
                    vt_ModeloCarrosRAM[2],
                    vt_ModeloCarrosRAM[3],
                    vt_ModeloCarrosRAM[4],
                ];

                // Dados do gráfico
                const dados2 = {
                    labels: graficoUsoRAM, // Nome da variável do gráfico
                    datasets: [{
                        label: 'Uso de RAM (%)',// Título
                        categoryPercentage: porcentagemCategeoriaGraficoRAM,
                        barPercentage: porcentagemBarraGraficoRAM, 
                        backgroundColor: '#b449de', // cor de fundo
                        borderColor: 'black', // cor da borda
                        data: [vt_MediasRAM[0], vt_MediasRAM[1], vt_MediasRAM[2], vt_MediasRAM[3], vt_MediasRAM[4]], // Plot dos valores embaixo das barras
                    },
                    ]
                };

                // Configurações do gráfico
                const config2 = {
                    type: 'bar', // Define para o tipo barra
                    data: dados2, // Diz quais dados serão referentes àquele gráfico
                    options: {
                        scales: {
                            y: {
                                min: 0,
                                max: 100,
                                beginAtZero: true
                            }
                        },
                        animation: 0
                    }
                };

                //Diz qual é a div que receberá o gráfico pronto
                const grafico2 = new Chart(
                    document.getElementById('grafico2'),
                    config2
                );
            })
        }
    })
}

const graficoUsoDisco = [
    'Livre',
    'Utilizado',
];

const dados3 = {
    labels: graficoUsoDisco,
    datasets: [{
        label: 'Uso de Disco',
        backgroundColor: ['#06D6A0', '#B84A62'],
        borderColor: 'none',
        data: [30, 70],
    },]
};

const config3 = {
    type: 'pie',
    data: dados3,
    options: {}
};

const grafico3 = new Chart(
    document.getElementById('grafico3'),
    config3
);

