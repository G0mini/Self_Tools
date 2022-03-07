<?php
// require ('waf.php');
require('conn.php');
error_reporting(E_ALL ^ E_NOTICE);
if($_POST){
$mydate=file($_FILES["file"]["tmp_name"]);//打开文件写入数组
}
$n=count($mydate);//统计关键词数量(数组个数)
for($i=0;$i<$n;$i++){
$date=explode(",",$mydate[$i]);//分割再组成数组
if ($mydate[$i]=="\r\n") {
	continue;
}
else{
	$date=preg_replace(array("/</","/>/"),"", $date);
	$str="insert into keywords(keyword,searches) values('".$date[0]."','".$date[1]."')";
	mysqli_query($conn,$str);
}
}
?>
<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>
	<pre></pre>		
	<a href="up.php">返回首页 </a>
</body>
</html>