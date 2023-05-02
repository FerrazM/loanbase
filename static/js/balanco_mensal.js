$(document).ready(function () {
    $("#form-periodo").submit(function (e) {
        e.preventDefault();
        var inicio = $("#inicio").val();
        var fim = $("#fim").val();
        $.ajax({
            type: "POST",
            url: "/balanco_mensal",
            data: { inicio: inicio, fim: fim },
            success: function (response) {
                // Atualizar a tabela com os novos valores
                $("#soma_pagamento").html(response.soma_pagamento);
                $("#soma_valor").html(response.soma_valor);
            }
        });
    });
});