$(document).ready(function(){
    $('#addorder').click(function(){
      location.href = '/addorder/';
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
  });