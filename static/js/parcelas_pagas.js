// selecione a checkbox1 e adicione um ouvinte de evento de clique
const checkbox1 = document.getElementById('id_checkbox1');
checkbox1.addEventListener('click', function () {
    const parcelasPagasElement = document.getElementById('id_parcelas_pagas');
    const parcelasAtrasadasElement = document.getElementById('id_parcelas_atrasadas');

    if (checkbox1.checked) {
        // se a checkbox1 estiver marcada, atualize a quantidade de parcelas_pagas
        parcelasPagasElement.value = parseInt(parcelasPagasElement.value) + 1;
        if (parseInt(parcelasAtrasadasElement.value) > 0) {
            parcelasAtrasadasElement.value = parseInt(parcelasAtrasadasElement.value) - 1;
        }
    }
});
