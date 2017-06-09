var input = $('#input-range');

input.bind('input', function(){
	getRangeValue(input);
}).bind('change', function(){
	getRangeValue(input);	/* for IE */
});

function getRangeValue(e){
	var value = $(e).val();
	$('.value').text(value);
	$('.range').attr('data-value', value);
	input.attr('value', value);
}