(function($){   
    $(function(){
        $(document).ready(function() {
        	// $("#id_memo_no").val("alamin");
        	$("#id_deport_code").bind('keyup focusout change', deport_customer);
        	$("#id_deport").bind('keyup focusout change', deport_customer);      	

        });
});  
})(django.jQuery);
var $ = django.jQuery.noConflict();


function deport_customer()
{
	console.log("update")
	var value = $(this).find(":selected").val();
	value = value + "--";
	console.log(value)
	var customer_id = "id_customer_input";
	$("#"+customer_id).val(value);

}