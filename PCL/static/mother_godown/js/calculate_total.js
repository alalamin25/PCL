(function($){
    $(function(){
        $(document).ready(function() {

            $(price_id).on('focusout', {input_field: 'price'}, calculate_total);
            $(total_id).on('focusout', {input_field: 'total'}, calculate_total);


        });

    var price_id = "#id_unit_price";
    var amount_id = "#id_unit_amount";
    var total_id = "#id_total_price";
    var unit_type_id = "#id_unit_type";

    var price;
    var total;

    function calculate_total(e){
        var input_field = e.data.input_field;
        console.log("value has been changed");
        var unit_type = $(unit_type_id + " option:selected").val();
        console.log(unit_type);
        var amount = $(amount_id).val();
        if(unit_type == 'ton'){
            amount = amount * 1000;
        }
        console.log(amount);

        if(input_field == 'price'){
             price = $(price_id).val();
             console.log(price);
             if(price !='' && !isNaN(price)){
                 total = price * amount;
                 if(!isNaN(total)){
                    $(total_id).val(total);
                 }
                 
             }
        }


        if(input_field == 'total'){
             total = $(total_id).val();
             // console.log(price);
             if(total !='' && !isNaN(total)){
                 price = total / amount;
                 if(!isNaN(price)){
                    $(price_id).val(price);
                 } 
             }
        }



    }


});  
})(django.jQuery);
var $ = django.jQuery.noConflict();

