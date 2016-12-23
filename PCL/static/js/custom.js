(function($){   
    $(function(){
        $(document).ready(function() {
        	$("#id_deport_code_text").prop("readonly", true);
        	$("#id_deport_code").bind('keyup', type_change);


        });
});  
})(django.jQuery);
var $ = django.jQuery.noConflict();

function type_change()
{

  var v = $("#id_deport_code").val();
	console.log(v);
	// $('#id_deport_code_text').val(v);



  // var action_type = $('#id_type').val();
  $.ajax({
          "type"     : "GET",
          "url"      : "/ajax_request/deport/?code="+v,
          "dataType" : "json",
          "cache"    : false,
          "success"  : function(json) {

          	  console.log("\n\n ajax successful");
          	  console.log(json);
          	  $('#id_deport_code_text').val(json['data']);

          }           
  });

}