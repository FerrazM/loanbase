$(document).ready(function () {
    var savedDate = $('input[name="vencimento_mensal"]').val();
    var savedDay = savedDate.split('/')[0];
    var savedMonth = savedDate.split('/')[1];
    var savedYear = savedDate.split('/')[2];

    $('input[name="vencimento_mensal"]').change(function () {
        var enteredDate = $(this).val();
        var enteredDay = enteredDate.split('/')[0];
        var enteredMonth = enteredDate.split('/')[1];
        var enteredYear = enteredDate.split('/')[2];

        if (enteredDay == savedDay && enteredMonth == savedMonth && enteredYear == savedYear) {
            $('input[name="checkbox1"]').prop('checked', false);

            var nextMonth = parseInt(savedMonth) + 1;
            var nextMonthYear = savedYear;
            if (nextMonth == 13) {
                nextMonth = 1;
                nextMonthYear = parseInt(savedYear) + 1;
            }

            var nextMonthDD = savedDay;
            var nextMonthMM = nextMonth;
            var nextMonthYYYY = nextMonthYear;

            if (nextMonthMM < 10) {
                nextMonthMM = '0' + nextMonthMM;
            }

            var nextMonthDate = nextMonthDD + '/' + nextMonthMM + '/' + nextMonthYYYY;
            $('input[name="vencimento_mensal"]').val(nextMonthDate);

            savedMonth = nextMonth;
            savedYear = nextMonthYear;
        } else {
            savedDay = enteredDay;
            savedMonth = enteredMonth;
            savedYear = enteredYear;
        }
    });

    $('input[name="checkbox1"]').change(function () {
        if ($(this).is(':checked')) {
            var nextMonth = parseInt(savedMonth) + 1;
            var nextMonthYear = savedYear;
            if (nextMonth == 13) {
                nextMonth = 1;
                nextMonthYear = parseInt(savedYear) + 1;
            }

            var nextMonthDD = savedDay;
            var nextMonthMM = nextMonth;
            var nextMonthYYYY = nextMonthYear;

            if (nextMonthMM < 10) {
                nextMonthMM = '0' + nextMonthMM;
            }

            var nextMonthDate = nextMonthDD + '/' + nextMonthMM + '/' + nextMonthYYYY;
            $('input[name="vencimento_mensal"]').val(nextMonthDate);

            savedMonth = nextMonth;
            savedYear = nextMonthYear;
        }
    });
});

