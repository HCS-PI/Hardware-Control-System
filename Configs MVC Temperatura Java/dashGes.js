setInterval(() => {
    buscarMediaCPUCarros();
    buscarMediaRAMCarros();
  }, 1000);
  
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
              if (json[i].Dispositivo % 2 == 0) {
                vt_Temperatura.push(json[i].Valor);
              } else if (json[i].Dispositivo % 2 != 0) {
                vt_ConsumoCPU.push(json[i].Valor);
              } else {
                console.log('Erro no IF Dispositivo')
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
                        data: [], // Plot dos valores embaixo das barras
                        yAxisID: 'y',
                    },
                    {
                        label: 'Temperatura CPU (ºC)',
                        data: [],
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
                document.getElementById('grafico4'),
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
              if (json[i].Dispositivo % 2 == 0) {
                newTemp = (json[i].Valor);
              } else if (json[i].Dispositivo % 2 != 0) {
                newCpu = (json[i].Valor);
              } else {
                console.log('Erro no IF Dispositivo')
              } 
            }
  
            grafico4.data.datasets[0].data.push(newCPU);
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