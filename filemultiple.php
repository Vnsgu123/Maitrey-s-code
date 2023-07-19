<html>
<body>
<form action ="file_upload.php" method="post" enctype="multipart/form-data">

	Username<input type="text" name="uname">
	Password<input type="password" name="pass">
	Jobtype<input type="text" name="job">
	Email<input type="text" name="email">
	salary<input type="number" name="sal">
	<input type="submit" value="submit" name="submit">

select file to upload for profile:
<input type="file" name="name"><br>
<input type="file" name="name1"><br>
<input type="file" name="name2"><br>

<input type="submit" value="uploadimage" name="submit">
</body>
</html>

<?php 
$target_dir = "uploads/";
print_r($_FILES);
$target_file = $target_dir . basename($_FILES[name][name]);
$target_file1 = $target_dir . basename($_FILES[name1][name1]);
$target_file2 = $target_dir . basename($_FILES[name2][name2]);

echo $target_file;

if($_SERVER["REQUEST_METHOD"]="POST"){
	$uploadok=1;
}
$imagefiletype=strtolower(pathinfo($target_file,PATHINFO_EXTENSION));
$imagefiletype1=strtolower(pathinfo($target_file1,PATHINFO_EXTENSION));
$imagefiletype2=strtolower(pathinfo($target_file2,PATHINFO_EXTENSION));

echo $imagefiletype;

if(isset($_POST["submit"]))
{
	$check = getimagesize[$_FILES[name][tmp_name]]
	$check1 = getimagesize[$_FILES[name1][tmp_name]];
	$check2 = getimagesize[$_FILES[name2][tmp_name]];
;
	if(check !== false || check1 !== false ||check2 !== false ||)
	{
		echo " all file is  an image ";
		$uploadok=1;
	}
	else
	{
		echo " file is  not an image ";
		$uploadok=0;
	}
}
print_r($_FILES);

if(file_exists($target_file))
{

echo "sorry file already exist";
		$uploadok=0;
}
if(file_exists($target_file1))
{

echo "sorry file already exist";
		$uploadok=0;
}
if(file_exists($target_file2))
{

echo "sorry file already exist";
		$uploadok=0;
}
if($_FILES["name"]["size"]>500000)
{
	echo "file is too large";
	$uploadok=0;

}
print_r( $_FILES);
if($imagefiletype != "jpg" && $imagefiletype != "png" && $imagefiletype != "jpeg")
{
	echo "not a specified type";
	$uploadok=0;
}

if($uploadok == 0)
{
	echo "sorry , your file is not uploadded";
}
else
{

	echo $_FILES["name"]["tmp_name"];
	echo "<br>";

	echo $target_file;
	
	if(move_uploaded_file($_FILES["name"]["tmp_name"],$target_file))
	{
	echo "file is uploaded";
	}
	else
	{
	echo "something errpr is occured";
	}
}

?>
