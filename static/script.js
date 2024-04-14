let cur = "";

function addd(n){
    document.getElementById("dot" + cur.length).style["background"] = "rgb(2,2,2)";
    cur += n;

    if(cur.length == 4){
        setTimeout(function(){
            window.location.href = '/approved/' + cur;
        },50);
    }
    
}

function del(){
    if(cur == "")return;
    document.getElementById("dot" + (cur.length-1)).style["background"] = "transparent";
    cur = cur.substring(0,cur.length-1);
}