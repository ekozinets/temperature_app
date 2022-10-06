$(document).ready(function () {
    var temperature_chart;

    function create_chart(labels, data) {
        var ctx = $("#temperature-chart");
        temperature_chart = new Chart(ctx, {
            type: 'line',
            data: {
                datasets: [{
                    label: 'Temperature',
                    backgroundColor: '#0d6efd',
                    data : data,
                    cubicInterpolationMode: 'monotone',
                    tension: 0
                }],
                labels: labels,

            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    title: {
                        display: false,
                    }
                  }
            }
        });
    }

    function show_chart(labels, data) {
        if (temperature_chart != undefined) {
            temperature_chart.destroy();
        }
        if (labels.length == 0 || data.length == 0) {
            $('#empty-data').fadeIn(500);
            return;
        }
        create_chart(labels, data);
    }

    function show_error_message(message) {
        $('.error-msg').find('ul').html('');
        $('.error-msg').css('display','block');
        $.each(message, function( key, value ) {
            $(".error-msg").find("ul").append('<li>' + value + '</li>');
        });
    }

    $('#main-form').submit(function () {
        $('#empty-data').css('display','none');
        $.ajax({
            data: $(this).serialize(),
            type: 'post',
            url: "/",
            success: function (response) {
                if ($.isEmptyObject(response.error)) {
                    show_chart(response.labels, response.data);
                } else {
                    show_error_message(response.error);
                }
            },
            error: function (response) {
                alert('Sorry. Some error.');
            }
        });
        return false;
    });
})
