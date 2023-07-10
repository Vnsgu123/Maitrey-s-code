<?php
$c_name = "userr";
$c_value  = "lawrence";

setcookie($c_name , $c_value , time() + (86400*30),"/")

?>

<HTML>
    <body>
        <?php if(isset($_COOKIE[$c_name]))
        {
            echo "cookie named ".$c_name." is set !";
        }
        else
        {
            echo "not set";
        }
        ?>
        </body>
    </HTML>







    <!-- <?php 

    //print_r( $_SERVER) ;
    //echo $_SERVER["REQUEST_METHOD"];
    if($_SERVER["REQUEST_METHOD"]=="POST")
    {
        $c_name = $_POST['name'];
        $c_value  =$_POST['password'];



        setcookie($c_name , $c_value , time() + (86400*30),"/");

        echo $_POST['name'];
        echo $_POST['password'];
        echo $c_name;
        echo $c_value;


        //echo "maitrrey";
    }
    ?> -->




<form action = "<?php echo $_SERVER['PHP_SELF'] ?>" method ="get" >
