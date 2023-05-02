window.addEventListener("load", function () {
    document.getElementById("id_valor").addEventListener("input", updatePayment);
    document.getElementById("id_juros").addEventListener("input", updatePayment);

});

function customRound(num, decimalPlaces) {
    return +(Math.round(num + "e+" + decimalPlaces) + "e-" + decimalPlaces);
}

function updatePayment() {
    let valor = parseFloat(document.getElementById("id_valor").value.replace(",", "."));
    let juros = document.getElementById("id_juros").value;

    if (valor && juros) {
        let jurosDecimal = juros.replace("%", "");
        jurosDecimal = jurosDecimal.replace(",", ".");
        jurosDecimal = math.eval(jurosDecimal / 100);
        let juros_mes = math.eval(valor * jurosDecimal);
        document.getElementById("id_juros_mes").value = juros_mes.toFixed(2);
    }
}
