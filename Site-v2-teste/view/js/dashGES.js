setInterval(() => {
  buscarMediaCPUCarros();
  buscarMediaRAMCarros();
}, 1000);

function buscarMediaCPUCarros() {
  vt_ModeloCarrosCPU = [];
  vt_MediasCPU = [];

  fetch("/dashGestor/mediaCpuCarros", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      idEmpresa: sessionStorage.ID_EMPRESA,
    }),
  }).then(function (resposta) {
    if (resposta.ok) {
      resposta.json().then((json) => {
        div_modelos_carros_CPU.innerHTML = "";
        for (let i = 0; i < json.length; i++) {
          vt_ModeloCarrosCPU.push(json[i].ModeloCarro);
          vt_MediasCPU.push(parseFloat(json[i].MediaConsumo));

          div_modelos_carros_CPU.innerHTML += `
                                            <div class="teste">
                                                <h3>Modelo: <span> ${json[i].ModeloCarro}  </span></h3>
                                                <h3>Consumo: <span> ${json[i].MediaConsumo} % </span></h3>
                                            </div>`;
        }

        console.log(vt_ModeloCarrosCPU);
        console.log(vt_MediasCPU);

        var porcentagemCategeoriaGraficoCPU = 0;
        var porcentagemBarraGraficoCPU = 0;
        if (vt_ModeloCarrosCPU.length < 2) {
          porcentagemCategeoriaGraficoCPU = 0.2;
          porcentagemBarraGraficoCPU = 0.7;
        } else {
          porcentagemCategeoriaGraficoCPU = 0.6;
          porcentagemBarraGraficoCPU = 0.9;
        }

        document.getElementById("graf_mediaCPU").remove();
        novoGraficoCPU = document.createElement("canvas");
        novoGraficoCPU.setAttribute("id", "graf_mediaCPU");
        div_graficoCPU.appendChild(novoGraficoCPU);

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
          datasets: [
            {
              label: "Uso de CPU (%)", // Título
              categoryPercentage: porcentagemCategeoriaGraficoCPU,
              barPercentage: porcentagemBarraGraficoCPU,
              backgroundColor: "#49a7de", // cor de fundo
              borderColor: "black", // cor da borda
              data: [
                vt_MediasCPU[0],
                vt_MediasCPU[1],
                vt_MediasCPU[2],
                vt_MediasCPU[3],
                vt_MediasCPU[4],
              ], // Plot dos valores embaixo das barras
            },
          ],
        };

        // Configurações do gráfico
        const config1 = {
          type: "bar", // Define para o tipo barra
          data: dados1, // Diz quais dados serão referentes àquele gráfico
          options: {
            scales: {
              y: {
                min: 0,
                max: 100,
                beginAtZero: true,
              },
            },
            animation: 0,
            responsive: false,
          },
        };

        //Diz qual é a div que receberá o gráfico pronto
        const grafico1 = new Chart(
          document.getElementById("graf_mediaCPU"),
          config1
        );
      });
    }
  });
}

function buscarMediaRAMCarros() {
  vt_ModeloCarrosRAM = [];
  vt_MediasRAM = [];

  fetch("/dashGestor/mediaRamCarros", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      idEmpresa: sessionStorage.ID_EMPRESA,
    }),
  }).then(function (resposta) {
    if (resposta.ok) {
      resposta.json().then((json) => {
        div_modelos_carros_RAM.innerHTML = "";

        for (let i = 0; i < json.length; i++) {
          vt_ModeloCarrosRAM.push(json[i].ModeloCarro);
          vt_MediasRAM.push(parseFloat(json[i].MediaConsumo));

          div_modelos_carros_RAM.innerHTML += `
                                            <div class="teste">
                                                <h3>Modelo: <span> ${json[i].ModeloCarro}  </span></h3>
                                                <h3>Consumo: <span> ${json[i].MediaConsumo} % </span></h3>
                                            </div>`;
        }
        var porcentagemCategeoriaGraficoRAM = 0;
        var porcentagemBarraGraficoRAM = 0;

        if (vt_ModeloCarrosRAM.length < 2) {
          porcentagemCategeoriaGraficoRAM = 0.2;
          porcentagemBarraGraficoRAM = 0.7;
        } else {
          porcentagemCategeoriaGraficoRAM = 0.6;
          porcentagemBarraGraficoRAM = 0.9;
        }

        document.getElementById("graf_mediaRAM").remove();
        novoGraficoRAM = document.createElement("canvas");
        novoGraficoRAM.setAttribute("id", "graf_mediaRAM");
        div_graficoRAM.appendChild(novoGraficoRAM);

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
          datasets: [
            {
              label: "Uso de RAM (%)", // Título
              categoryPercentage: porcentagemCategeoriaGraficoRAM,
              barPercentage: porcentagemBarraGraficoRAM,
              backgroundColor: "#b449de", // cor de fundo
              borderColor: "black", // cor da borda
              data: [
                vt_MediasRAM[0],
                vt_MediasRAM[1],
                vt_MediasRAM[2],
                vt_MediasRAM[3],
                vt_MediasRAM[4],
              ], // Plot dos valores embaixo das barras
            },
          ],
        };

        // Configurações do gráfico
        const config2 = {
          type: "bar", // Define para o tipo barra
          data: dados2, // Diz quais dados serão referentes àquele gráfico
          options: {
            scales: {
              y: {
                min: 0,
                max: 100,
                beginAtZero: true,
              },
            },
            animation: 0,
            responsive: false,
          },
        };

        //Diz qual é a div que receberá o gráfico pronto
        const grafico2 = new Chart(
          document.getElementById("graf_mediaRAM"),
          config2
        );
      });
    }
  });
}
/*
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
*/


function plotarTempCpuMaisRecente() {
  vt_ConsumoCPU = [];
  vt_Temperatura = [];

  fetch("/dashGestor/cpuTemperaturaServer", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        idEmpresa: sessionStorage.ID_EMPRESA,
      }),
    }).then(function (resposta) {
      if (resposta.ok) {
        resposta.json().then((json) => {
  
          for (let i = 0; i < json.length; i++) {
            if (json[i].dispositivo % 2 == 0) {
              vt_Temperatura.push(json[i].valor);
            } else if (json[i].dispositivo % 2 != 0) {
              vt_ConsumoCPU.push(json[i].valor);
            } else {
              console.log('Erro no IF Dispositivo');
            } 
          }
  
          const labels = ["10º Valor","9º Valor","8º Valor","7º Valor",
          "6º Valor","5º Valor","4º Valor","3º Valor","2º Valor",
          "Valor Mais Recente"];

          // Dados do gráfico
          const dados4 = {
              labels: labels, // Nome da variável do gráfico
                  datasets: [{
                      label: 'Uso de CPU (%)', // Título
                      categoryPercentage: 0.6,
                      barPercentage: 0.9, 
                      backgroundColor: '#49a7de', // cor de fundo
                      borderColor: '#257eb3', // cor da borda
                      data: vt_ConsumoCPU, // Plot dos valores embaixo das barras
                      yAxisID: 'y',
                  },
                  {
                      label: 'Temperatura CPU (ºC)',
                      data: vt_Temperatura,
                      borderColor: '#9c1010',
                      backgroundColor: '#d94343',
                      yAxisID: 'y',    
                  }
                  ]
              };
  
          // Configurações do gráfico
          const config4 = {
              type: 'line', // Define para o tipo barra
              data: dados4, // Diz quais dados serão referentes àquele gráfico
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
          grafico4 = new Chart(
              document.getElementById('graf_TempCPU'),
              config4,
          );
        });
      }
    });
}
plotarTempCpuMaisRecente();

setInterval(() => {
  updateGraph()
}, 1000);

const updateGraph = () => {
  var newTemp = null;
  var newCpu = null;

  fetch("/dashGestor/cpuTemperaturaServer", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        idEmpresa: sessionStorage.ID_EMPRESA,
      }),
    }).then(function (resposta) {
      if (resposta.ok) {
        resposta.json().then((json) => {

          for (let i = 0; i < json.length; i++) {
            if (json[i].dispositivo % 2 == 0) {
              newTemp = (json[i].valor);
            } else if (json[i].dispositivo % 2 != 0) {
              newCpu = (json[i].valor);
            } else {
              console.log('Erro no IF Dispositivo')
            } 
          }

          grafico4.data.datasets[0].data.push(newCpu);
          grafico4.data.datasets[1].data.push(newTemp);

          if (grafico4.data.datasets[0].data.length > 10) {
              grafico4.data.datasets[0].data.shift(1)
              grafico4.data.datasets[1].data.shift(1)
          }
        });
      }
    });
          grafico4.update();
}
