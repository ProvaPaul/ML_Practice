var nam=document.querySelector("#nam");
var loc=document.querySelector("#loc");
var photo=document.querySelector("#photo");
var desc=document.querySelector("#desc");
var submit=document.querySelector("#submit");

var countt=0;

submit.addEventListener(("click"),function(event){  
        event.preventDefault();
        var errormsg=document.querySelector(".error");
        errormsg.innerText="";
        errormsg.style.marginTop="1rem";

    if(nam.value!="" && loc.value!="" && photo.value!="" && desc.value!=""){ 
    var outerdiv=document.querySelector(".form2");
    if(countt==0){
        var head=document.querySelector(".headd");
        head.innerText="My WishList"

    outerdiv.innerText="";
    }

    errormsg.innerText="Destination Details Added Successfully!";
    errormsg.style.color="rgb(4, 71, 4)";



    var innerdiv=document.createElement("div");
    innerdiv.className="result";

    var img1=document.createElement("img");
    img1.className="img";
    img1.src=photo.value;
    innerdiv.append(img1);

    var place1=document.createElement("h3");
    place1.className="h22";
    place1.innerText=nam.value;
    innerdiv.append(place1);
    
    var loc1=document.createElement("h3");
    loc1.className="h33";
    loc1.innerText=loc.value;
    innerdiv.append(loc1);

    var desc1=document.createElement("p");
    desc1.className="details";
    desc1.innerText=desc.value;
    innerdiv.append(desc1); 
    
    var remove=document.createElement("button");
    remove.className="remove";
    remove.innerText="remove";
    innerdiv.append(remove);


    outerdiv.appendChild(innerdiv);

    

    remove.addEventListener(("click"),function(event){
    event.preventDefault();
        innerdiv.remove();  //for removing the specific div

        if(outerdiv.children.length==0){
            var head=document.querySelector(".headd");
            head.innerText="Enter Your WishList";
        }
        
});

    countt=1;
  }

else{
    // for not fillup the all input

        var form=document.querySelector(".form-in");
        errormsg.innerText="Please fillup the form correctly!";
        errormsg.style.color="red";
        form.append(errormsg);
    }
          
    

});
