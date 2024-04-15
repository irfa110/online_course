var player;
var video_list;
window.onload = ()=>{
    player = document.getElementById('player')
    video_list = document.getElementById('leacher')
    menainRation()
}

window.onresize = ()=>{
    menainRation()
}

function menainRation(){
    var w = player.clientWidth
    var h = (w*9)/16
    player.height = h
    video_list.style.maxHeight= h +"px"
    console.log("hi")
}