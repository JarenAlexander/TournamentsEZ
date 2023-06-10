/*

This is the JavaScript that helps format our frontend web pages.

Authors: Jaren Alexander, Yankun Chen, Brett Fox, Kevin Truong, Sam Windheim

Group Name: TournamentsEZ

Last Modification Date: 6/9/2023

*/


window.addEventListener('DOMContentLoaded', function() {
    var tournamentName = localStorage.getItem('selectedTournament');
    var tournamentNameElement = document.getElementById('tournamentName');
    if (tournamentName && tournamentNameElement) {
      tournamentNameElement.textContent = tournamentName;
    }
  });
  
  // function redirectToSignUp(tournamentName) {
  //   localStorage.setItem('selectedTournament', tournamentName);
  //   window.location.href = 'signup.html';
  // }

  function tournRedirectToSignUp() {
    var tournamentSelect = document.getElementById("tournamentSelect");
    var selectedTournament = tournamentSelect.options[tournamentSelect.selectedIndex].value;
    if (selectedTournament !== "") {
      window.location.href = "signup.html?tournament=" + encodeURIComponent(selectedTournament);
    }
  }
  
  
  
  
