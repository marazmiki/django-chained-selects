(function($) {
  $(function(){
    function fillEmpty(target, label)
    {
      var options = '<option value="">' + label + '</option>';
      target.html(options);
      target.find('option:first').attr('selected', 'selected');
      target.trigger('change');
    }

    function fillField(target, label, url, pk, initialValue)
    {
      $.getJSON(url.replace('$pk$', pk), function(j) {
        var
          options = '<option value="">' + label + '</option>',
          width = target.outerWidth(),
          autoChoose = true
        ;

        $.each(j, function(i, v){
          options += '<option value="'+ v.value + '">' + v.display + '</option>';
        })

        target.html(options);

        if (navigator.appVersion.indexOf("MSIE") != -1){
          target.width(width + 'px');
        }

        target
          .find('option:first')
          .attr('selected', 'selected')
        ;

        if (initialValue){
          target
            .find('option[value="'+ initValue +'"]')
            .attr('selected', 'selected')
          ;
        }

        if (autoChoose && j.length == 1) {
          target
            .find('option[value="'+ j[0].value +'"]')
            .attr('selected', 'selected')
          ;
        }

        target.trigger('change');
      });
    }

    // find parent select and assign handlers
    $('select.chained').each(function() {
      var
        $parent = $('#' + $(this).data('parent-id')),
        $target = $(this),
        url = $(this).data('url'),
        emptyLabel = $(this).data('empty-label')
      ;
      $parent.on('change', function() {
        var
          pk = $(this).val()
        ;
        if (!pk || pk == ''){
          fillEmpty($target, emptyLabel);
        } else {
          fillField($target, emptyLabel, url, pk);
        }
      });
      fillEmpty($target, emptyLabel);
    });
  });
})(jQuery || django.jQuery);
