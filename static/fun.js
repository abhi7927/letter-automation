function prefill() {    
    var initialdate = document.querySelector("body > div > form > input[type=date]:nth-child(7)").value
    var finaldate = document.querySelector("body > div > form > input[type=date]:nth-child(8)").value
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
  