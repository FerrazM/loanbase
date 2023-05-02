$(document).ready(function calculatePayment() {
    var valor = document.getElementById("valor").value;
    var juros = document.getElementById("juros").value;
    var juros_mes = (valor * (juros / 100)).toFixed(2);
    document.getElementById("juros_mes").value = juros_mes;
});