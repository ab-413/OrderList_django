$(document).ready(function(){

    $("#addorder").modalForm({
        formURL: '/addorder/'
    });

    $("#addcustomer").modalForm({
        formURL: '/addcustomer/'
    });

    $("#addcustomerfrommodal").modalForm({
        formURL: '/addcustomer/'
    });

    $(".order-detail").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url")});
    });

    $(".order-edit").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url")});
    });

    $(".order-delete").each(function () {
        $(this).modalForm({formURL: $(this).data("form-url"), isDeleteForm: true});
    });

    $('#customers').click(function(){
      location.href = '/allcustomers/';
    });

    $('#allorders').click(function(){
      location.href = '/allorders/';
    });

    $('#refresh').click(function(){
      location.reload();
    });

    $('.datepicker').datepicker();

    $(".statuses").change(function(){
        $.ajax({url: "update_status/" + $(this).data(), success: function(result){
            console.log(result);
        }});
    });
});