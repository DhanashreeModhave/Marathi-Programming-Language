function runCode(){

let code = document.getElementById("code").value;

fetch("/run",{
method:"POST",
headers:{
"Content-Type":"application/json"
},
body: JSON.stringify({code:code})
})
.then(res=>res.json())
.then(data=>{

if(data.error){
document.getElementById("output").innerText = data.error;
}
else{
document.getElementById("output").innerText =
"Generated Python:\n"+data.python+
"\n\nOutput:\n"+data.output;
}

})
.catch(err=>{
document.getElementById("output").innerText = err;
});

}