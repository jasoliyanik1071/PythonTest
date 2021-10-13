$(document).ready(function() {
	$("#ProductListDataTable").DataTable();

	function add_loader_in_page(elem){
	    $('.block-ui').remove();
	    elem.append("<div class='block-ui'></div>");
	    $(".block-ui").append("<img src='/static/images/spinner-1s-200px.gif' alt='' class='loading_image' style='top: 50%;position: absolute;left: 50%;transform: translate(-50%, -50%);'>");
	    $(".block-ui").css({'left': "50%", "position": "fixed", "top": "50%", "width": "100%", "height": "100%", "z-index": "9999999999", "text-align": "center","background":"#00000060","transform":"translate(-50%,-50%)"});
	}

	function remove_loader_from_page(){
	    $('.block-ui').remove();
	}


	$("body .edit-product-btn").click(function(event){
		debugger
	})
	$("body .edit-product-btn").on("click", function(event){
		event.preventDefault();
		debugger
	});

	$("#product-category").on("change", function(event){
        event.preventDefault();
        add_loader_in_page($('body'));

        var categ_id = 0;

        if ($(this).find("option:selected") && $(this).find("option:selected") != undefined){
        	var categ_id = $($(this).find("option:selected")[0]).val();
        }
        debugger

        $.ajax({
            type: 'POST',
            headers: {"X-CSRFToken": Cookies.get("csrftoken")},
            // url: $(this).data('url'),
            url: '/get-categ-related/product',
            data: {"category_id": categ_id},
            datatype: 'json',
            success: function(data){
                remove_loader_from_page();
                debugger
                $("#product-details-data").html(data.product_list_data);

                $("#ProductListDataTable").DataTable();
            },
            error: function(data){
                console.log('Error');
                remove_loader_from_page();
            }
        })

    });

    $("#product-category").change();

});
