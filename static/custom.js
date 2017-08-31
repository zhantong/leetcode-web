$(document).ready(
    function () {
        $('#sidebar').sidebar('setting', 'transition', 'overlay');
        $('#sidebar').sidebar('attach events', '.launch.item');
        $(document).pjax('a[data-pjax]', '#pjax-container');
        $(document).on('pjax:timeout', function () {
            return false;
        });
        $(document).on('pjax:start', function () {
            $('#sidebar').sidebar('hide');
        });
        $(document).on('pjax:complete', function () {
            on_pjax_complete();
        });
        $('#prev').click(function () {
            $('#sidebar > a.item.active').prev().click();
        });
        $('#next').click(function () {
            $('#sidebar > a.item.active').next().click();
        });
        $('div.input > i.link').click(function () {
            $('.item[data-id="' + $("#problem_id").val() + '"]').click();
            $("#problem_id").blur();
        });
        $("#problem_id").keypress(function (e) {
            if (e.keyCode == '13') {
                $('div.input > i.link').click();
            }
        });

        on_pjax_complete();
    }
);

function on_pjax_complete() {
    highlight_selected_list_item();
    $('#nav_title').html($('#article').data('title'));

    $("#problem_id").val('');
}


function highlight_selected_list_item() {
    $('#sidebar a').removeClass('active');
    $('.item[data-id="' + $("#article").data("id") + '"]').addClass('active');
}