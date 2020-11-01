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
    //       $('#content').load("engine/showorders.php");            
    //     }
    //   });
    // });

    // $('#content').load("engine/showorders.php");

    // $('#info').click(function(){
    //   $('#content').load("engine/showorders.php");
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