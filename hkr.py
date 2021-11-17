< ?xml
version = "1.0"
encoding = "UTF-8"? >
< !DOCTYPE
html
PUBLIC
"-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd" >
< html
xmlns = "http://www.w3.org/1999/xhtml" >
< head >
< title > HKR自动化测试报告 < / title >
< meta
name = "generator"
content = "HTMLTestRunner 0.8.2" / >
< meta
http - equiv = "Content-Type"
content = "text/html; charset=UTF-8" / >

< style
type = "text/css"
media = "screen" >
body
{font - family: verdana, arial, helvetica, sans - serif;
font - size: 80 %;}
table
{font - size: 100 %;}
pre
{}

/ *-- heading - --------------------------------------------------------------------- * /
h1
{
    font - size: 16pt;
color: gray;
}
.heading
{
    margin - top: 0ex;
margin - bottom: 1
ex;
}

.heading.attribute
{
    margin - top: 1ex;
margin - bottom: 0;
}

.heading.description
{
    margin - top: 4ex;
margin - bottom: 6
ex;
}

/ *-- css
div
popup - ----------------------------------------------------------------------- * /
a.popup_link
{
}

a.popup_link: hover
{
    color: red;
}

.popup_window
{
    display: none;
position: relative;
left: 0
px;
top: 0
px;
/ *border: solid  # 627173 1px; */
padding: 10
px;
background - color:  # E6E6D6;
font - family: "Lucida Console", "Courier New", Courier, monospace;
text - align: left;
font - size: 8
pt;
width: 500
px;
}

}
/ *-- report - ----------------------------------------------------------------------- * /
   # show_detail_line {
   margin - top: 3
ex;
margin - bottom: 1
ex;
}
# result_table {
width: 80 %;
border - collapse: collapse;
border: 1
px
solid  # 777;
}
# header_row {
font - weight: bold;
color: white;
background - color:  # 777;
}
# result_table td {
border: 1
px
solid  # 777;
padding: 2
px;
}
# total_row  { font-weight: bold; }
.passClass
{background - color:  # 6c6; }
    .failClass
{background - color:  # c60; }
    .errorClass
{background - color:  # c00; }
    .passCase
{color:  # 6c6; }
    .failCase
{color:  # c60; font-weight: bold; }
.errorCase
{color:  # c00; font-weight: bold; }
    .hiddenRow
{display: none;}
.testcase
{margin - left: 2em;}

/ *-- ending - --------------------------------------------------------------------- * /
# ending {
}

< / style >

< / head >
< body >
< script
language = "javascript"
type = "text/javascript" > <!--
output_list = Array();

/ *level - 0: Summary;
1: Failed;
2: All * /
function
showCase(level)
{
    trs = document.getElementsByTagName("tr");
for (var i = 0; i < trs.length; i++)
{
    tr = trs[i];
id = tr.id;
if (id.substr(0, 2) == 'ft')
{
if (level < 1)
{
    tr.className = 'hiddenRow';
}
else {
    tr.className = '';
}
}
if (id.substr(0, 2) == 'pt') {
if (level > 1) {
tr.className = '';
}
else {
tr.className = 'hiddenRow';
}
}
}
}

function
showClassDetail(cid, count)
{
    var
id_list = Array(count);
var
toHide = 1;
for (var i = 0; i < count; i++)
{
    tid0 = 't' + cid.substr(1) + '.' + (i + 1);
tid = 'f' + tid0;
tr = document.getElementById(tid);
if (!tr)
{
    tid = 'p' + tid0;
tr = document.getElementById(tid);
}
id_list[i] = tid;
if (tr.className)
{
    toHide = 0;
}
}
for (var i = 0; i < count; i++) {
    tid = id_list[i];
if (toHide) {
document.getElementById('div_'+tid).style.display = 'none'
document.getElementById(tid).className = 'hiddenRow';
}
else {
document.getElementById(tid).className = '';
}
}
}

function
showTestDetail(div_id)
{
    var
details_div = document.getElementById(div_id)
var
displayState = details_div.style.display
               // alert(displayState)
if (displayState != 'block')
{
    displayState = 'block'
details_div.style.display = 'block'
}
else {
    details_div.style.display = 'none'
}
}


function
html_escape(s)
{
    s = s.replace( / & / g, '&amp;');
s = s.replace( / < / g, '&lt;');
s = s.replace( / > / g, '&gt;');
return s;
}

/ *obsoleted
by
detail in < div >
function
showOutput(id, name)
{
var
w = window.open("", // url
name,
"resizable,scrollbars,status,width=800,height=450");
d = w.document;
d.write("<pre>");
d.write(html_escape(output_list[id]));
d.write("\n");
d.write("<a href='javascript:window.close()'>close</a>\n");
d.write("</pre>\n");
d.close();
}
* /
--> < / script >

        < div


class ='heading' >

< h1 > HKR自动化测试报告 < / h1 >
< p


class ='attribute' > < strong > Start Time:<

    / strong > 2021 - 11 - 17
14: 30:02 < / p >
< p


class ='attribute' > < strong > Duration:<

    / strong > 0: 00:29.240515 < / p >
< p


class ='attribute' > < strong > Status:<

    / strong > Error
4 < / p >

< p


class ='description' > HKR测试报告 < / p >

< / div >

< p
id = 'show_detail_line' > Show
< a
href = 'javascript:showCase(0)' > Summary < / a >
< a
href = 'javascript:showCase(1)' > Failed < / a >
< a
href = 'javascript:showCase(2)' > All < / a >
< / p >
< table
id = 'result_table' >
< colgroup >
< col
align = 'left' / >
< col
align = 'right' / >
< col
align = 'right' / >
< col
align = 'right' / >
< col
align = 'right' / >
< col
align = 'right' / >
< / colgroup >
< tr
id = 'header_row' >
< td > Test
Group / Test
case < / td >
< td > Count < / td >
< td > Pass < / td >
< td > Fail < / td >
< td > Error < / td >
< td > View < / td >
< / tr >

< tr


class ='errorClass' >

< td > Testhkr.Testhkr < / td >
< td > 4 < / td >
< td > 0 < / td >
< td > 0 < / td >
< td > 4 < / td >
< td > < a
href = "javascript:showClassDetail('c1',4)" > Detail < / a > < / td >
< / tr >

< tr
id = 'ft1.1'


class ='none' >

< td


class ='errorCase' > < div class ='testcase' > testloginError_1 < / div > < / td >

< td
colspan = '5'
align = 'center' >

< !--css
div
popup
start -->
< a


class ="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_ft1.1')" >


error < / a >

< div
id = 'div_ft1.1'


class ="popup_window" >

< div
style = 'text-align: right; color:red;cursor:pointer' >
< a
onfocus = 'this.blur();'
onclick = "document.getElementById('div_ft1.1').style.display = 'none' " >
[x] < / a >
< / div >
< pre >

ft1
.1: Traceback(most
recent
call
last):
File
"D:\Pythonproject\pythonproject1\venv\lib\site-packages\ddt.py", line
191, in wrapper
return func(self, *args, **kwargs)
File
"D:\Pythonproject\pythonproject1\pycode4\Testhkr.py", line
69, in testloginError
print(Initpage.xlw(num, '通过'))
File
"D:\Pythonproject\pythonproject1\pycode4\InitPage.py", line
45, in xlw
wb.save('D:\Python自动化测试\其他课程\自动化\day03\HKR.xls')
File
"D:\Pythonproject\pythonproject1\venv\lib\site-packages\xlwt\Workbook.py", line
710, in save
doc.save(filename_or_stream, self.get_biff_data())
File
"D:\Pythonproject\pythonproject1\venv\lib\site-packages\xlwt\CompoundDoc.py", line
262, in save
f = open(file_name_or_filelike_obj, 'w+b')
PermissionError: [Errno 13]
Permission
denied: 'D:\\Python自动化测试\\其他课程\\自动化\\day03\\HKR.xls'

< / pre >
< / div >
< !--css
div
popup
end -->

< / td >
< / tr >

< tr
id = 'ft1.2'


class ='none' >

< td


class ='errorCase' > < div class ='testcase' > testloginError_2 < / div > < / td >

< td
colspan = '5'
align = 'center' >

< !--css
div
popup
start -->
< a


class ="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_ft1.2')" >


error < / a >

< div
id = 'div_ft1.2'


class ="popup_window" >

< div
style = 'text-align: right; color:red;cursor:pointer' >
< a
onfocus = 'this.blur();'
onclick = "document.getElementById('div_ft1.2').style.display = 'none' " >
[x] < / a >
< / div >
< pre >

ft1
.2: Traceback(most
recent
call
last):
File
"D:\Pythonproject\pythonproject1\venv\lib\site-packages\ddt.py", line
191, in wrapper
return func(self, *args, **kwargs)
File
"D:\Pythonproject\pythonproject1\pycode4\Testhkr.py", line
69, in testloginError
print(Initpage.xlw(num, '通过'))
File
"D:\Pythonproject\pythonproject1\pycode4\InitPage.py", line
45, in xlw
wb.save('D:\Python自动化测试\其他课程\自动化\day03\HKR.xls')
File
"D:\Pythonproject\pythonproject1\venv\lib\site-packages\xlwt\Workbook.py", line
710, in save
doc.save(filename_or_stream, self.get_biff_data())
File
"D:\Pythonproject\pythonproject1\venv\lib\site-packages\xlwt\CompoundDoc.py", line
262, in save
f = open(file_name_or_filelike_obj, 'w+b')
PermissionError: [Errno 13]
Permission
denied: 'D:\\Python自动化测试\\其他课程\\自动化\\day03\\HKR.xls'

< / pre >
< / div >
< !--css
div
popup
end -->

< / td >
< / tr >

< tr
id = 'ft1.3'


class ='none' >

< td


class ='errorCase' > < div class ='testcase' > testloginSuccess_1 < / div > < / td >

< td
colspan = '5'
align = 'center' >

< !--css
div
popup
start -->
< a


class ="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_ft1.3')" >


error < / a >

< div
id = 'div_ft1.3'


class ="popup_window" >

< div
style = 'text-align: right; color:red;cursor:pointer' >
< a
onfocus = 'this.blur();'
onclick = "document.getElementById('div_ft1.3').style.display = 'none' " >
[x] < / a >
< / div >
< pre >

ft1
.3: Traceback(most
recent
call
last):
File
"D:\Pythonproject\pythonproject1\venv\lib\site-packages\ddt.py", line
191, in wrapper
return func(self, *args, **kwargs)
File
"D:\Pythonproject\pythonproject1\pycode4\Testhkr.py", line
44, in testloginSuccess
print(Initpage.xlw(num, '通过'))
File
"D:\Pythonproject\pythonproject1\pycode4\InitPage.py", line
45, in xlw
wb.save('D:\Python自动化测试\其他课程\自动化\day03\HKR.xls')
File
"D:\Pythonproject\pythonproject1\venv\lib\site-packages\xlwt\Workbook.py", line
710, in save
doc.save(filename_or_stream, self.get_biff_data())
File
"D:\Pythonproject\pythonproject1\venv\lib\site-packages\xlwt\CompoundDoc.py", line
262, in save
f = open(file_name_or_filelike_obj, 'w+b')
PermissionError: [Errno 13]
Permission
denied: 'D:\\Python自动化测试\\其他课程\\自动化\\day03\\HKR.xls'

< / pre >
< / div >
< !--css
div
popup
end -->

< / td >
< / tr >

< tr
id = 'ft1.4'


class ='none' >

< td


class ='errorCase' > < div class ='testcase' > testloginSuccess_2 < / div > < / td >

< td
colspan = '5'
align = 'center' >

< !--css
div
popup
start -->
< a


class ="popup_link" onfocus='this.blur();' href="javascript:showTestDetail('div_ft1.4')" >


error < / a >

< div
id = 'div_ft1.4'


class ="popup_window" >

< div
style = 'text-align: right; color:red;cursor:pointer' >
< a
onfocus = 'this.blur();'
onclick = "document.getElementById('div_ft1.4').style.display = 'none' " >
[x] < / a >
< / div >
< pre >

ft1
.4: Traceback(most
recent
call
last):
File
"D:\Pythonproject\pythonproject1\venv\lib\site-packages\ddt.py", line
191, in wrapper
return func(self, *args, **kwargs)
File
"D:\Pythonproject\pythonproject1\pycode4\Testhkr.py", line
44, in testloginSuccess
print(Initpage.xlw(num, '通过'))
File
"D:\Pythonproject\pythonproject1\pycode4\InitPage.py", line
45, in xlw
wb.save('D:\Python自动化测试\其他课程\自动化\day03\HKR.xls')
File
"D:\Pythonproject\pythonproject1\venv\lib\site-packages\xlwt\Workbook.py", line
710, in save
doc.save(filename_or_stream, self.get_biff_data())
File
"D:\Pythonproject\pythonproject1\venv\lib\site-packages\xlwt\CompoundDoc.py", line
262, in save
f = open(file_name_or_filelike_obj, 'w+b')
PermissionError: [Errno 13]
Permission
denied: 'D:\\Python自动化测试\\其他课程\\自动化\\day03\\HKR.xls'

< / pre >
< / div >
< !--css
div
popup
end -->

< / td >
< / tr >

< tr
id = 'total_row' >
< td > Total < / td >
< td > 4 < / td >
< td > 0 < / td >
< td > 0 < / td >
< td > 4 < / td >
< td > & nbsp; < / td >
< / tr >
< / table >

< div
id = 'ending' > & nbsp; < / div >

< / body >
< / html >