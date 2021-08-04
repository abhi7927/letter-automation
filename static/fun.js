function leaveLetterPrefill() {    
    var initialdate = document.querySelector("body > div > form > input[type=date]:nth-child(7)").value
    var finaldate = document.querySelector("body > div > form > input[type=date]:nth-child(10)").value
    var fullname = document.querySelector("body > div > form > input[type=text]:nth-child(1)").value
    var duration = (Date.parse(finaldate)-Date.parse(initialdate))/(24*3600000)+1
    document.getElementById("body").value = "Respected Mr/Mrs,"+ "\n\n" +
    "I would like to bring to your kind attention that due to (enter the reason),"+
    " I would like to take a leave of absence for " + duration +
    " days. I have handled my responsibilities to (enter the names) and I am sure they will co-operate in my absence."+
    " I hope you understand my situation and grant me leave from " +
     initialdate +" to "+finaldate +"."+
    "\n\nThank You," + "\n\nYours Faithfully\n"+fullname;
}
function requestDocsPrefill(){
    var fullname = document.querySelector("body > div > form > input[type=text]:nth-child(1)").value
    var documents = document.querySelector("body > div > form > input[type=text]:nth-child(7)").value
    document.getElementById("body").value = "Respected Mr/Mrs,"+ "\n\n" +
    "This letter is to inform you that for further process of your request we need the required documents as mentioned: "+
    documents + "." + " You are requested to do the needful as early as possible." + 
    "\n\nThank You," + "\n\n"+fullname;
}  
