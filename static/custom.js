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

        on_pjax_complete();
    }
);

function on_pjax_complete() {
    highlight_selected_list_item();
    $('#nav_title').html($('#article').data('title'));
}


function highlight_selected_list_item() {
    $('#sidebar a').removeClass('active');
    $('.item[data-id="' + $("#article").data("id") + '"]').addClass('active');
}