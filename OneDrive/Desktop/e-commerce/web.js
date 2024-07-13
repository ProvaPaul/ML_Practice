// let home=document.getElementById("home");
// let cloth=document.getElementById("cloth");
// let blogs=document.getElementById("blogs");
// let reviews=document.getElementById("reviews");
// let contacts=document.getElementById("contacts");

// home.addEventListener("click",function(){
//     home.style.color="blue";
//     cloth.style.color="white";
//     blogs.style.color="white";
//     reviews.style.color="white";
//     contacts.style.color="white";
// });

// cloth.addEventListener("click",function(){
//     home.style.color="white";
//     cloth.style.color="blue";
//     blogs.style.color="white";
//     reviews.style.color="white";
//     contacts.style.color="white";
// });

// blogs.addEventListener("click",function(){
//     home.style.color="white";
//     cloth.style.color="white";
//     blogs.style.color="blue";
//     reviews.style.color="white";
//     contacts.style.color="white";
// });

// reviews.addEventListener("click",function(){
//     home.style.color="white";
//     cloth.style.color="white";
//     blogs.style.color="white";
//     reviews.style.color="blue";
//     contacts.style.color="white";
// });

// contacts.addEventListener("click",function(){
//     home.style.color="white";
//     cloth.style.color="white";
//     blogs.style.color="white";
//     reviews.style.color="white";
//     contacts.style.color="blue";
// });


let login=document.getElementById("cartlogo");
console.log(login);
login.addEventListener("click",function(){
        let open=document.querySelector(".loginpage").style.display="block";
});


let submit1=document.getElementById("submit1");
submit1.addEventListener("click",function(){
    let email=document.querySelector("#email");
    let pass=document.querySelector("#pass");
    if(email.value==""|| pass.value== ""){
        alert("Please Enter Your Email Password Correctly!");
    }
    else{
        alert("You've loged in successfully!");
        document.querySelector(".loginpage").style.display="none";
    }
})

let submit=document.getElementById("submit");
submit.addEventListener("click",function(){
    let name=document.querySelector("#contact-name");
    let pass=document.querySelector("#contact-pass");
    if(name.value==""|| pass.value==""){

        alert("Please enter name and password correctly!");
    }
    else{
        alert("Submitted Succesfully !");
    }
})