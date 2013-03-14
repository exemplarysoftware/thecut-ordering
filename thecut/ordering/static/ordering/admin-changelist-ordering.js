ordering.jQuery(document).ready(function($) {

    $.ajaxSetup({traditional: true});
    $('body').addClass('js-enabled').ajaxStart(function() {
        $(this).addClass('ajax-loading');
    }).ajaxStop(function() {
        $(this).removeClass('ajax-loading');
    });

    $('body.change-list table#result_list tbody tr').each(function(index) {
        var href = $(this).find('a').attr('href');
        var pk = parseInt(href.match(/(\d+)\//)[1]);
        $(this).attr('data-pk', 'pk_' + pk);
    });

    $('body.change-list table#result_list tbody').sortable({
        cursor: 'move',
        opacity: 0.6,
        axis: 'y',
        update: function(event, ui) {
            $(this).children('tr').removeClass('row1 row2');
            $(this).children('tr:nth-child(odd)').addClass('row1');
            $(this).children('tr:nth-child(even)').addClass('row2');

            $.ajax({
                data: $(this).sortable('serialize', {'key': 'pk', 'attribute': 'data-pk'}),
                error: function(XMLHttpRequest, textStatus, errorThrown) {
                    alert('An error occured whilst processing this request.');
                },
                type: 'POST',
                url: 'reorder'
            });
        }
    });

    $('body.change-list p.paginator').append('(drag to change ordering).');

});
