<?php 
session_start();
//echo $_POST['name'];
//echo $_POST['password'];

// $p = $_POST['name'];
// print_r( $_COOKIE);
//session_start();
//echo "hello world";
//print_r($_SESSION);
//echo  $_POST['name'];
//     echo $_SERVER["REQUEST_METHOD"];

if($_SERVER["REQUEST_METHOD"]=="POST")
{
if(!empty($_POST['name']) && !empty($_POST['password'])) {
$t=$_POST['name'];
$p=$_POST['password'];

$_SESSION["username"] = $t;
$_SESSION["password"] = $p;

echo "Hey ,".$_SESSION["username"]." you are logged in";

}

else
{
    echo "invalid username or password ";
    //header("location:form1.php");
}
}
//print_r($_SESSION);
//header("location:new.php");

//}
//         echo "Hey ,".$_SESSION["username"]." you are logged in";
//         //echo "password  is ".$_SESSION["password"];
