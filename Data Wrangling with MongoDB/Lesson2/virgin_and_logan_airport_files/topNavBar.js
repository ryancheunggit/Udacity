var cssmenuids=["local1","local2","local3","local4","local5","local6"] //Enter id(s) for local menus ONLY, separated by commas
var csssubmenuoffset=-1 //Offset of submenus from main menu. Default is 0 pixels.

function createcssmenu2(){
for (var i=0; i<cssmenuids.length; i++){
  var ultags=document.getElementById(cssmenuids[i]).getElementsByTagName("ul")
    for (var t=0; t<ultags.length; t++){
			ultags[t].style.top=ultags[t].parentNode.offsetHeight+csssubmenuoffset+"px"
    	var spanref=document.createElement("span")
			spanref.className="arrowdiv"
			spanref.innerHTML="&nbsp;&nbsp;&nbsp;&nbsp;"
			ultags[t].parentNode.getElementsByTagName("a")[0].appendChild(spanref)
    	ultags[t].parentNode.onmouseover=function(){
					this.style.zIndex=100
    	this.getElementsByTagName("ul")[0].style.visibility="visible"
					this.getElementsByTagName("ul")[0].style.zIndex=0
    	}
    	ultags[t].parentNode.onmouseout=function(){
					this.style.zIndex=0
					this.getElementsByTagName("ul")[0].style.visibility="hidden"
					this.getElementsByTagName("ul")[0].style.zIndex=100
    	}
    }
  }
}

if (window.addEventListener)
window.addEventListener("load", createcssmenu2, false)
else if (window.attachEvent)
window.attachEvent("onload", createcssmenu2)