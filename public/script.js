
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
  
  
  
  