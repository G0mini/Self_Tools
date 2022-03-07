<!DOCTYPE html>
<html>
<head>
	<title>数据查询</title>
</head>
<body>
	<form action="<?php echo $_SERVER['PHP_SELF'] ?>" method="GET">
		<select name="cars">
		<option value="10">TOP10</option>
		<option value="100">TOP100</option>
		<option value="1000">TOP1000</option>
		<option value="10000">TOP10000</option>
		<option value="ALL">ALL</option>
		<select>
		<br>
		<br>
		<input type="submit" name='s' value="read">
		 &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
		<input type="submit" name='s' value="down">
		 &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
		<input type="button" name='s' value="return" class="btn_a" onclick="location.href='up.php'">

	</form>
</body>
</html>
<?php
error_reporting(0);
include('conn.php');
if (array_key_exists('s',$_GET)){
	$des =$_GET['cars'];
}
if ($des=="ALL") {
	$count="SELECT keyword from keywords GROUP by keyword ORDER BY COUNT(*) DESC";
	$sear=mysqli_query($conn,$count);
}
else{
	$count="SELECT keyword from keywords GROUP by keyword ORDER BY COUNT(*) DESC limit $des";
	$sear=mysqli_query($conn,$count);
}
$str='';
foreach($sear as $k => $v){
	$str .=implode('',$v)."<br>";
	}
	$str =substr($str,0,strlen($str)-1);
if($_GET['s']=="read")
{	
	print("TOP"."$des"."--读取成功")."<br><br><br>";
	echo("$str");
}
elseif($_GET['s']=="down")
{	
	$str=str_replace("<br>","\r\n",$str);
	$str=preg_replace("/\n\s*\r/","\r\n",$str);
	$str=str_replace("<br","",$str);
	$read=fopen("info.txt",'a+');
	fwrite($read,$str);
	print ("TOP"."$des"."下载成功");
	header("location:search.php");
}
elseif ($_GET['s']=="return") {
}
?>

