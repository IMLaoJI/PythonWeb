// 定义变量
var a = 10;
var b = 20.5;
var x = true;
var score = 50;

// console 输出结果
console.log(a>b);
console.log(score > 60 && score < 100);
console.log(typeof a);
console.log(typeof b);
console.log(typeof x);

// if, else, else if 的运用
if(typeof a == "number"){
  console.log("条件正确");
}

if(score >= 60){
  document.write("<h2 style='color:green'>及格</h2>")
}
else if(score >= 70){
  document.write("良");
}

// 判断
var grade = 'A';
switch (grade)
{
  case 'A': document.write("成绩<br/>不错!");
  break;
  
  case 'B': document.write("还可以");
  break;
    
  case 'c': document.write("马马虎虎!");
  break;
    
  default: document.write("成绩未知!");
}

// 循环
var count = 0;
while (count < 10){
  document.write("当前值是:" + count + "<br/>");
  count++;
}
document.write("循环停止!");

// 先执行一次,再改变值,再判断
var count = 0;
do{
  document.write("当前值是:" + count + "<br/>");
  count++;
}
while(count < 10)
