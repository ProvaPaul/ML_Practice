let string="";
let btn=document.querySelectorAll(".button");
let arr=Array.from(btn);

arr.forEach((button)=>{
    button.addEventListener("click",(e)=>{
        let p=e.target.innerText;
        if(p==="="){
            string=eval(string);
            document.querySelector(".input").value=string;
            string="";
        }
        else{
            if(p==="C"){
                string="";
                document.querySelector(".input").value=string;
            }
            else
            {
            string= string + e.target.innerText;
             console.log(e.target.innerText);
             document.querySelector(".input").value=string;    
            }
         
   
        }
        
    })
})



