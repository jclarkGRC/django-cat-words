$( document ).ready(function() {
      // Set the date we're counting down to
      var countDownDate = new Date()
      countDownDate.setSeconds(countDownDate.getSeconds() + 30);

      // Update the count down every 1 second
      var x = setInterval(function() {

      // Get today's date and time
      var now = new Date().getTime();

      // Find the distance between now and the count down date
      var distance = countDownDate - now;

      // Time calculations for days, hours, minutes and seconds
      var seconds = Math.floor((distance % (1000 * 30)) / 1000);

      // Output the result in an element with id="demo"
      //document.getElementById("countdownTimer").innerHTML = seconds + "s ";
      $("#countdownTimer").html(seconds + "s ");

      // If the count down is over, The game is over
      if (distance < 0) {
        clearInterval(x);
        $("#countdownTimer").html("TIMES UP!");
        window.location.href = 'http://' + document.domain + ':8000/game/scores';
        return false;
      }
    }, 1000);
});