/*global showAddAnotherPopup, showRelatedObjectLookupPopup showRelatedObjectPopup updateRelatedObjectLinks*/

function compressArray(original) {

	var compressed = [];
	// make a copy of the input array
	var copy = original.slice(0);

	// first loop goes over every element
	for (var i = 0; i < original.length; i++) {

		var myCount = 0;
		// loop over every element in the copy and see if it's the same
		for (var w = 0; w < copy.length; w++) {
			if (original[i] == copy[w]) {
				// increase amount of times duplicate is found
				myCount++;
				// sets item to undefined
				delete copy[w];
			}
		}

		if (myCount > 0) {
			var a = new Object();
			a.value = original[i];
			a.count = myCount;
			compressed.push(a);
		}
	}

	return compressed;
};

(function($) {
    'use strict';
    $(document).ready(function() {
        var modelName = $('#django-admin-form-add-constants').data('modelName');

        $('body').on('click', '.add-another', function(e) {
            e.preventDefault();
            var event = $.Event('django:add-another-related');
            $(this).trigger(event);
            if (!event.isDefaultPrevented()) {
                showAddAnotherPopup(this);
            }
        });

        $( "#bank_form" ).submit(function( event ) {

          var days = django.jQuery('select').map(function(){
              if (this.value.length>0){return this.value;}
          }).get();

          if(compressArray(days).length != 5){
                event.preventDefault();
                alert("Problem Exists in Operating Hours section");
          };





        });

        if (modelName) {
            $('form#' + modelName + '_form :input:visible:enabled:first').focus();
        }
    });
})(django.jQuery);
