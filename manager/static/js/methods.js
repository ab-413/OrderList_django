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

    $('#customers').click(function(){
      location.href = '/allcustomers/';
    });

    $('#allorders').click(function(){
      location.href = '/allorders/';
    });

    $('#refresh').click(function(){
      location.reload();
    });
  });