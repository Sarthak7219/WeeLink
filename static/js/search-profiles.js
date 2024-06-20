let profileList = [];

// Fetch profiles once when the page loads
$.ajax({
  url: "/profile-search/", // Adjust the URL to your actual view
  method: "GET",
  success: function (data) {
    profileList = data.profiles;
  },
});

$("#search-input").on("input", function () {
  const query = $(this).val().toLowerCase();
  const suggestions = profileList.filter((profile) =>
    profile["user__username"].toLowerCase().includes(query)
  );

  $("#search-results").empty();
  suggestions.forEach((profile) => {
    $("#search-results").append(
      `<div data-id="${profile.id}">${profile["user__username"]}</div>`
    );
  });
});

// Handle suggestion click
$("#search-results").on("click", "div", function () {
  const profileId = $(this).data("id");
  window.location.href = `/profile/${profileId}/`;
});
