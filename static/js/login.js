

function loginCheck(){
alert("ajaxing");
$.ajax({
    type:"POST",
    url: "{% url 'buddi:login_ajax' %}",
    data: $('#login-form').serialize(),
    success: function(response){
        // do something with response

        res = response['result'];
         if (res === 'Success'){
            alert("Loggin in");
            return true;
         }
         else{
            alert("Nope");
            return false;
         }
     }
});
}