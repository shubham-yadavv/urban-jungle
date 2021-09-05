 function save()
   {
       fname = document.getElementById("first_name").value,
       phno = document.getElementById("last_name").value,
       console.log(fname);
   Email.send({
    Name: document.getElementById("first_name").value,
    Host : "smtp.gmail.com",
    Username : "tirals.trials@gmail.com",
    Password : "Trials321",
    To : document.getElementById("email").value
    From : "tirals.trials@gmail.com",
    Subject : "Order confirmation",
    Body : "And this is the body"
}).then(function(response){
if(response=="OK"){
    alert("Congratulations. Your msg has been sent successfully");

}
else{
alert(response.statusText);
    throw new Error("Error:"+ response);
}
}


);
          };
