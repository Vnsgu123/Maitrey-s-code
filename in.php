<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
<table id="t1" >
    <tr>
        <td>
            <h1>PHP AJAX</h1>
        </td>
    </tr>
    <tr>
        <td>
            <input type="button" id="load" value="loaddata">
        </td>
    </tr>
    <tr>
        <td id="tab1">
        </td>
    </tr>
    </table>    

    <div class="output"></div>

<script type="text/javascript" src="jquery-3.7.1.min.js"></script>

<script type="text/javascript">

    $(document).ready(function(){
        $("#load").on("click",function(e){
            $.ajax({
                url:"insert.php",
                type:"POST",
                success:function(data){
                    // $('.output').text(JSON.stringify(data));

                    $("#tab1").html(data);
                }
            })
        })
    })


</script>


</body>
</html>