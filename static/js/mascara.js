var SPMaskBehavior = function (val) {
    return val.replace(/\D/g, '').length === 11 ? '(00) 00000-0000' : '(00) 0000-00009';
},
    spOptions = {
        onKeyPress: function (val, e, field, options) {
            field.mask(SPMaskBehavior.apply({}, arguments), options);
        }
    };

$(document).ready(function () {
    $('.mask-cpf').mask('000.000.000-00', { reverse: true });
    $('.mask-telefone').mask(SPMaskBehavior, spOptions);
    $('.mask-data-emprestimo').mask('00/00/0000');
    $('.mask-data').mask('00/00/0000');
    $('.mask-vencimento').mask('00/00/0000');
    $('.mask-valor').mask("###0.00", { reverse: true });
    $('.mask-juros').mask('##0.00%', { reverse: true });
    
});

