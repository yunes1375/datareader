function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function demo() {
  console.log('Taking a break...');
  var k=0;
  await sleep(10);
   
  // Sleep in loop
  while(1!=0) {
    if (k!=0){
    await sleep(10000);
    }
    k=k+1;
    var s='/test/';
    fetch(s)
.then(function (response) {
   return response.json();
}).then(function (text) {
  var html='<table ><tr> <th>Id</th>  <th>Name</th> <th>Price</th> <th>EPS</th><th>PE</th> <th>PE Group</th> <th>PS</th> <th>تعداد خرید حقیقی</th><th>تعداد خرید حقوقی</th> <th>تعداد فروشی حقیقی</th> <th>تعداد فروش حقوقی</th> <th>سرانه</th><th>تاریخ</th><th>ساعت به روزرسانی</th></tr>';
  
  for (let i=0;i<Object.keys(text).length;i++){
    html=html+'<tr>';
    console.log(i);
    html=html+'<td>'+text[i].data[0].id+'</td>';
    html=html+'<td>'+text[i].data[1].namee+'</td>';
    html=html+'<td>'+text[i].data[2].price+'</td>';
    html=html+'<td>'+text[i].data[3].eps+'</td>';
    html=html+'<td>'+text[i].data[4].pe+'</td>';
    html=html+'<td>'+text[i].data[5].pegroup+'</td>';
    html=html+'<td>'+text[i].data[6].ps+'</td>';
    html=html+'<td>'+text[i].data[7].hakh+'</td>';
    html=html+'<td>'+text[i].data[8].hokh+'</td>';
    html=html+'<td>'+text[i].data[9].haf+'</td>';
    html=html+'<td>'+text[i].data[10].hof+'</td>';
    html=html+'<td>'+text[i].data[11].sarane+'</td>';
    html=html+'<td>'+text[i].data[12].dateday+'</td>';
    html=html+'<td>'+text[i].data[13].time+'</td></tr>';
  }
  html=html+'</table>';
  document.getElementById("table").innerHTML=html;
  

    // tag=text.greeting
  
    // console.log(obj[1].id)
    
}
);

// return false;
  }
};

demo();
// button.onclick = function(){
//   document.getElementById('sqlreqcondition').innerHTML="Request sent";
//   var a=document.getElementById('mysqltimeinput');
//   var x=a.value;
//   var s='/test/'+x
//   fetch(s)
// .then(function (response) {
//     return response.json();
// }).then(function (text) {
//   document.getElementById('sqlreqcondition').innerHTML="Request sent";
//     console.log('GET response:');
//     document.getElementById('sqlreqcondition').innerHTML("Data recieved")
//     tag=text.greeting
//     console.log("tag updated in function",tag)
// });

// return false;
// };