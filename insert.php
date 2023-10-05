<?php

$conn = mysqli_connect("localhost","root","","shop_db") or die("connection failed");

$sql = "select * from users" ;

$result = mysqli_query($conn,$sql) or die("result failed");

if(mysqli_num_rows($result) > 0){

    $output = '<table border="1" width="100%" cellspacing="0" cellpadding="10px">
               <tr>
               <th>ID</th>
               <th>name</th>
               </tr>';
            while($row = mysqli_fetch_assoc($result)){
                $output .= "<tr><td>{$row["ID"]}</td><td>{$row["name"]}</td></tr>"; 
            }
            $output .= '</table>';
            mysqli_close($conn);

            echo $output;
}
else{
    echo "<h2>no record foud </h2>";
}



?>