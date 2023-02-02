function validateform()
{
    var strname=document.forms["regform"]["fname"].value
    var strphn=document.forms["regform"]["phn"].value
    var gnarr=document.getElementsByName("gender")
    if(strname.length==0 || strname.length<5){
        document.getElementById("fspan").innerHTML=" Invalid Name"
        return false    
    }
    else if (!(strphn>=15&&strphn<=20)){
        document.getElementById("pspan").innerHTML="Invalid Age"
        return false
    }
    else{
        if (document.getElementsByName("gender")[0].checked==false && document.getElementsByName("gender")[1].checked==false ){
            document.getElementById("gspan").innerHTML="Please Select Gender"
            return false
        }
    } 
    return true
}

function validname()
{
    var strname=document.forms["regform"]["fname"].value
    if(strname.length==0 || strname.length<5){
        document.getElementById("fspan").innerHTML=" Invalid Name"
        document.getElementById("fspan").style.color="red"
    }
    else
    {
        document.getElementById("fspan").innerHTML=""
    }
}

function validage(){
    var strphn=document.forms["regform"]["phn"].value
    if (!(strphn>=15&&strphn<=20)){
        document.getElementById("pspan").innerHTML="Invalid Age"
        document.getElementById("pspan").style.color="red"
    }
    else
    {
        document.getElementById("pspan").innerHTML=""
    }
}

function validgender(){
    var gnarr=document.getElementsByName("gender")
    if (document.getElementsByName("gender")[0].checked==false && document.getElementsByName("gender")[1].checked==false ){
        document.getElementById("gspan").innerHTML="Please Select Gender"
        document.getElementById("gspan").style.color="red"
    }
    else{
        document.getElementById("gspan").innerHTML=""
    }
}