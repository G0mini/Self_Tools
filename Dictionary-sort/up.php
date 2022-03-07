<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>数据导入</title>
</head>
<body>
<script>
function import_check(){
    var f_content = form1.file.value; /*获取到文件完整路径*/
    var fileext=f_content.substring(f_content.lastIndexOf("."),f_content.length)/*获取到文件格式后缀*/
        fileext=fileext.toLowerCase()/*把文件格式后缀转换成小写*/
     if (fileext!='.txt')
        {
         alert("对不起，导入数据格式必须是txt格式文件哦，请您调整格式后重新上传，谢谢 !");            
         return false;
        }
}
</script>
    <table width="98%" border="0" align="center" style="margin-top:20px; border:1px solid #9abcde;">
    <form id="form1" name="form1" enctype="multipart/form-data" method="post" action="insert.php">   
        <tr >
            <td height="28" colspan="2">
            <label>  <strong>关键词数据导入</strong></label>
        </td>
        </tr>
        <tr>
            <td width="18%" height="50"> 选择你要导入的关键词库</td>
            <td width="82%">
            <label>
            <input name="file" type="file" id="file" size="50" />
            </label>
            <label>
            <input name="button" type="submit" class="nnt_submit" id="button" value="导入数据"    onclick="return import_check();"/>
            &nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp
            </label>
    </form>
    <form id="form2" name="form2" enctype="multipart/form-data" method="get" action="search.php" style="display: inline">
            <label>
                <input name="button" type="submit" class="nnt_submit" id="button" value="查询数据"> 
            </label>          
    </form>
</td>
        </tr>
        <tr>
            <td colspan="2" bgcolor="#DDF0FF">  [<span class="STYLE1">注</span>]数据导入格式说明:</td>
        </tr>
        <tr>
            <td colspan="2">    1、其它.导入数据表文件必须是<strong>excel</strong>文件格式{.<span class="STYLE2">txt</span>}为扩展名.</td>
        </tr>
        <tr>
            <td colspan="2">  2、txt文件导入数据顺序必须如:关键词,搜索量    </td>
        </tr>
        <tr>
            <td colspan="2"> </td>
        </tr></form>
    </table>
</body>
</html>