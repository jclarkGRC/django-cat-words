$(window).on('load',function(){
    let scoreSaved = localStorage.getItem('scoreSaved');
    let gamePlayed = localStorage.getItem('gamePlayed');
    if(scoreSaved == null && gamePlayed == "true"){
    $('#myModal').modal('show');
    }
    $('#saveScore').on('click', function(){
        localStorage.setItem('scoreSaved', "true");
    });
    $('#playAgainButton').on('click', function(){
        localStorage.removeItem('scoreSaved')
    });
});