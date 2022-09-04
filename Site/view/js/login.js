modoG = fabricanteG = modeloG = tkAcessoG = tkAcessoVeiculo = '';

function verificaModo(modo){
    modoG = modo;

    if(modo == '0'){
        fieldFabricante.style.display = 'block';
        fieldTkAcesso.style.display = 'none';
        fieldModeloTesla.style.display = 'none';
        fieldModeloVolkswagen.style.display = 'none';
        fieldModeloHyundai.style.display = 'none';
        fieldModeloHonda.style.display = 'none';
        fieldTkVeiculo.style.display = 'none';
    }else if(modo == '1'){
        fieldTkAcesso.style.display = 'block';
        fieldFabricante.style.display = 'none';
        fieldModeloTesla.style.display = 'none';
        fieldModeloVolkswagen.style.display = 'none';
        fieldModeloHyundai.style.display = 'none';
        fieldModeloHonda.style.display = 'none';
        fieldTkVeiculo.style.display = 'none';
    }else{
        fieldTkAcesso.style.display = 'none';
        fieldFabricante.style.display = 'none';
        fieldModeloTesla.style.display = 'none';
        fieldModeloVolkswagen.style.display = 'none';
        fieldModeloHyundai.style.display = 'none';
        fieldModeloHonda.style.display = 'none';
        fieldTkVeiculo.style.display = 'none';
    }
}

function verificaFabricante(fab){
    fabricanteG = fab;

    if(fab == "0"){
        fieldModeloTesla.style.display = 'block';
        fieldModeloVolkswagen.style.display = 'none';
        fieldModeloHyundai.style.display = 'none';
        fieldModeloHonda.style.display = 'none';
    }else if(fab == "1"){
        fieldModeloVolkswagen.style.display = 'block';
        fieldModeloTesla.style.display = 'none';
        fieldModeloHyundai.style.display = 'none';
        fieldModeloHonda.style.display = 'none';
    }else if(fab == "2"){
        fieldModeloHyundai.style.display = 'block';
        fieldModeloTesla.style.display = 'none';
        fieldModeloVolkswagen.style.display = 'none';
        fieldModeloHonda.style.display = 'none';
    }else if(fab == "3"){
        fieldModeloHonda.style.display = 'block';
        fieldModeloTesla.style.display = 'none';
        fieldModeloVolkswagen.style.display = 'none';
        fieldModeloHyundai.style.display = 'none';
    }else{
        fieldModeloHonda.style.display = 'none';
        fieldModeloTesla.style.display = 'none';
        fieldModeloVolkswagen.style.display = 'none';
        fieldModeloHyundai.style.display = 'none';
        fieldTkVeiculo.style.display = 'none';
    }
}

function verificaModelo(modelo){
    modeloG = modelo;
    fieldTkVeiculo.style.display = 'block';
}

function login(){
    alert('Em desenvolvimento...')
}