$(document).ready(function(){
    // $('#add').click(function(event){
    //   event.preventDefault();
    //   $.ajax({
    //     url:"engine/addorder.php",
    //     method:"POST",
    //     data:$('#addform').serialize(),          
    //     success:function(data){
    //       $('#addform')[0].reset();
    //       $('#orderAddModal').modal('hide');
    //       $('#content').load("orders/showorders.html");            
    //     }
    //   });
    // });

    // $('#content').load("showorders.html");

    // $('#info').click(function(){
    //   $('#content').load("showorders.html");
    // });

    $('#refresh').click(function(){
      location.reload();
    });
  });
  $('#orderdeadline').datepicker({
    format: 'yyyy/mm/dd',
    language: 'ru',
    todayHighlight: true
  });