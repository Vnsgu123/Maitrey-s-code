<?php
session_start();
?>
<html>
    <body>
        <?php
        $_SESSION["favcourse"] = "mscit";
        $_SESSION["favsubject"] = "DS";
        echo "session variables are set ";
        ?>
    </body>
</html>
