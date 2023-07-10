<HTML>
    <BODY>
        <form action = "fileupload.php" method="post" enctype="multipart/form-data">
            select image to upload:<br>
            <input type ="file" name="image"><br>
            <input type ="submit" value="upload image" name = "submit">
</form>
</body>
</html>

<?php
$target_dir = "upload/";
$target_file = $target_dir.basename($_FILES['image']['name']);
if($_SERVER["REQUEST_METHOD"] = "POST"){
    $uploadok = 1;
}
print_r($_FILES);
echo  "<br>";
//print_r($_POST);


$imagefiletype=strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
print_r($imagefiletype);
if(isset($_POST["submit"]))
{
    $check = getimagesize($_FILES["image"]["tmp_name"]);
    print_r($check);
}

if(file_exists($target_file)){
    echo "file already exit <br> ";
    $uploadok=0;
}

if(filesize($target_file) > 50000)
{
    $uploadok=0;
    echo " file size is greator <br>";
}
print_r($imagefiletype);
// if( $imagefiletype != "jpeg" && $imagefiletype != "png" $imagefiletype != "jpg")
// {
//     $uploadok=0;
//     echo " file is unwanted type <br>";
// }
if ($uploadok == 0)
{
    echo "sorry !!! file not uploaded <br>";
}
else
{
if (move_uploaded_file($_FILES["image"]["tmp_name"],$target_file))
{
    echo "file uploaded successfully <br>";
}
else
{
    echo " so sorry <br>";
}
}
?>