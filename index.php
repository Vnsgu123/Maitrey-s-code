<?php
session_start();
//echo "hello world";
//echo 4+5 ;
?>
<html>
    <body>
        <?php
        echo "favourate course is ".$_SESSION["favcourse"];
        echo "favourate subject is ".$_SESSION["favsubject"];
        ?>
        </body>
</html>