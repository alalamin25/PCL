// $("#id_fp_item_many_to").children().first().val();
// $("#id_fp_item_chained").find(":selected").val()
// <option value=​"12" title=​"AZZ00002:​ zimCompound">​AZZ00002: zimCompound​</option>​


(function($){   
    $(function(){
        $(document).ready(function() {
        	$(".id_memo_no").bind('keyup focusout change', update_return_rate);
        });
});  
})(django.jQuery);
var $ = django.jQuery.noConflict();

function update_return_rate()
{

    var value = $(this).val();
    var target_id = $(this).attr('id') + '_text'; 
    var ajax_url =  "/ajax_request/fpitem/?code=" + value;
	// console.log(v);
	// $('#id_deport_code_text').val(v);
	// 
	console.log("value changed");
	console.log(value);
	console.log(target_id);
	// $('#'+target_id).val(value);



  // var action_type = $('#id_type').val();
  $.ajax({
          "type"     : "GET",
          "url"      : ajax_url,
          "dataType" : "json",
          "cache"    : false,
          "success"  : function(json) {

          	  console.log("\n\n ajax successful");
          	  console.log(json);
          	  $('#'+target_id).val(json['data']);

          }           
  });

}


function isNumber(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}

function calculateTotal()
{

    // var basic_id = $(this).find(':first-child').attr('id');
    var basic_id = $(this).find('input').attr('id');
    console.log("basic id");
    console.log(basic_id);
    var index = basic_id.lastIndexOf('-');
    basic_id = basic_id.substring(0, index);

    var quantity_id =  basic_id + '-quantity';
    var commission_id = basic_id + '-commission';
    var rate_id = basic_id + '-rate';
    var total_text_id = basic_id + '-total';
    var net_total_text_id = basic_id + '-net_total';


    var quantity = $('#'+quantity_id).val();
    var rate = $('#'+rate_id).val();
    var commission = $('#'+commission_id).val();

    var total = quantity * rate;
    var net_total = total - (total * commission / 100);
     //    var target_id = $(this).attr('id') + '_text'; 
 //    var ajax_url =  "/ajax_request/fpitem/?code=" + value;
	// // console.log(v);
	// // $('#id_deport_code_text').val(v);
	// 
	console.log("Going to calculate Total");
	console.log(rate);
	console.log(quantity);
  console.log(commission);


  total = Number(total.toFixed(2));
  net_total = Number(net_total.toFixed(2));
	$('#'+total_text_id).val(total);
	$('#'+net_total_text_id).val(net_total);


  var net_grand_total = 0;
	var net_net_total = 0;
	var net_total_commission = 0;


 	for(var i=0; i<100; i++){
 		var val = $('#id_selldetailinfo_set-' + i + '-total').val();
    	if(isNumber( val)){
    		val = parseFloat(val);
    		net_grand_total += val;
    		// console.log(val);
    	}

 	}
    console.log("net grand_total is: ");
    console.log(net_grand_total);
// id_selldetailinfo_set-0-net_total_text

 	for(var i=0; i<100; i++){
 		var val = $('#id_selldetailinfo_set-' + i + '-net_total').val();
    	if(isNumber( val)){
    		val = parseFloat(val);
    		net_net_total += val;
    		// console.log(val);
    	}

 	}
	
    console.log("net net_total is: ");
    console.log(net_net_total);

    net_total_commission = net_grand_total - net_net_total;

    
    net_grand_total = Number(net_grand_total.toFixed(2));
    net_total_commission = Number(net_total_commission.toFixed(2));
    net_net_total = Number(net_net_total.toFixed(2));


    $("#id_grand_total").val(net_grand_total);
    $("#id_total_commission").val(net_total_commission);
    $("#id_net_total").val(net_net_total);






}