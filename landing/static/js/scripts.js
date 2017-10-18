$(document).ready(function () {
    var invite_in_team = $('#invite_in_team');

    invite_in_team.on('submit', function (e) {
        e.preventDefault();
        var invite_member = $('#invite_member').val();
        var submit_btn = $('#submit_btn');
        var team = submit_btn.data("team_id");
        console.log(team);
    });



    /*function showingUserInfo() {
        $('.user-menu').toggleClass('show');
        $('.user-containerr').toggleClass('show');
    }

    $('.user-container').on('click', function(e){
        e.preventDefault();
        showingUserInfo();
     });

    $('.user-container').mouseover(function(){
        showingUserInfo();
     });

    $('.user-container').mouseout(function(){
        showingUserInfo();
     });*/



});