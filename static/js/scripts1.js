function myFunction() {
    var time1 = document.getElementById("time1").value;
    var time2 = document.getElementById("time2").value;
    var diff = (new Date(time2)).getTime() - (new Date(time1)).getTime();
    var hrs = Math.floor(diff / (1000 * 60 * 60));
    var risk = document.querySelector('input[name="risk"]:checked').value;
    document.getElementById("getga").innerHTML = document.getElementById("ga").value;
    if (isNaN(hrs)) {
        hrs = document.getElementById("age").value;
    }
    document.getElementById("getage").innerHTML = hrs;
    document.getElementById("getrisk").innerHTML = risk;
    document.getElementById("getmb").innerHTML = document.getElementById("tcb").value;
    return false;
}