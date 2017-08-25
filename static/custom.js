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
            highlight_selected_list_item();
        });
        highlight_selected_list_item();
    }
);


function highlight_selected_list_item() {
    $('#sidebar a').removeClass('active');
    $('.item[data-id="' + $("#content_title").data("id") + '"]').addClass('active');
}