function validateForm(){
    var url = "{% url 'buddi:login_ajax' %}";

    alert(url);

    $.ajax({
    type:"POST",
    url: url,
    data: $('#login-form').serialize(),
    success: function(response){
        // do something with response
        alert(response['result']); // equals 'Success or failed';
//        response['message']; // equals 'you"re logged in or You messed up';
     },
     error: function(response){
        alert("nope");
     }
//
    });
//    alert(response);
    return false;


}

$(document).ready(function(){

    $("#login-submit").click(function () {
            alert($('#login-form').serialize())

//            var password = $("#register-password").val();
//            var confirmPassword = $("#register-password-confirm").val();
//            if (password != confirmPassword) {
//                alert("Passwords do not match.");
//                return false;
//            }
//            alert("match")
//            return true;
        });

//    $.ajax({
//    type:"POST",
//    url: '/login/',
//    data: $('#login-form').serialize(),
//    success: function(response){
//        // do something with response
//        response['result']; // equals 'Success or failed';
//        response['message']; // equals 'you"re logged in or You messed up';
//     }

//});

});