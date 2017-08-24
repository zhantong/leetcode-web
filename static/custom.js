$(document).ready(
    function () {
        $(document).pjax('a[data-pjax]', '#pjax-container');
        $(document).on('pjax:timeout', function () {
            return false;
        });

        $(document).on('pjax:complete', function () {
            highlight_selected_list_item()
        });
        highlight_selected_list_item();
    }
);

function highlight_selected_list_item() {
    $('#problem_list li').removeClass('selected');
    $('.pure-menu-item[data-id="' + $("#content_title").data("id") + '"]').addClass('selected');
}