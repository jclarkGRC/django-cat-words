$(window).on('load',function(){

    // Check to see if the user is a first time user.
    let firstTimeUser = localStorage.getItem('firstTimeUser')

    // Only show the modal if it is the users first time playing
    if(firstTimeUser == null){
        $('#myModal').modal('show');
        localStorage.setItem('firstTimeUser', 'false')
    }
    // Set game played so we know whether to show the high scores modal or not if
    // The user goes directly to the high scores page from the home page without playing
    // the game
    $('#letsPlay').on('click', function() {
    localStorage.setItem('gamePlayed', 'true')
    });
});