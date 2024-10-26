$(document).ready(function() {
    $('#add_expense').click(function(){

        var category = $("#category").val();
        var amount = $("#amount").val()

        $.ajax({
            url: '/add_expense',
            type:'POST',
            contentType: 'application/json',
            data: JSON.stringify({'category': category, 'amount':parseFloat(amount)}),
            success: function(response){
                alert(response.status)
                window.location.reload();
            },
            error: function(response){
                alert(response.responseJSON.status);
            }
        });
    });

    $('.delete_expense').on('click',function() {
        var expenseID = $(this).attr('data-id');

        $.ajax({
            url: '/delete_expense/'+ expenseID,
            type: 'DELETE',
            success: function(response) {
                alert(response.status)
                window.location.reload()
            },
            error: function(response) {
                alert(response.responseJSON.status);
            }
        });
    });
});