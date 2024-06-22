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
  console.log(query);
  const suggestions = profileList.filter((profile) => {
    // Check if username exists before calling toLowerCase()
    if (profile.username) {
      return profile.username.toLowerCase().includes(query);
    }
    return false;
  });

  $("#search-results").empty();
  suggestions.forEach((profile) => {
    const profileHtml = `
      <div class="no-before d-flex align-items-center mb-2" data-id="${profile.id}" style="cursor:pointer; border-bottom:1px">
        <div class="iq-profile-avatar">
          <img class="rounded-circle avatar-50" src="${profile.image_url}" alt="" style="object-fit: cover;">
        </div>
        <div class="ms-3">
          <h6 class="mb-0">${profile.username}</h6>
        </div>
      </div>
    `;
    $("#search-results").append(profileHtml);
  });

  // Show the search results
  if (suggestions.length > 0) {
    $("#search-results").addClass("visible");
  } else {
    $("#search-results").removeClass("visible");
  }
});

// Handle suggestion click
$("#search-results").on("click", ".d-flex", function () {
  const profileId = $(this).data("id");
  window.location.href = `/profile/${profileId}/`;
});

// Hide search results on clicking outside
$(document).on("click", function (e) {
  if (!$(e.target).closest("#search-container").length) {
    $("#search-results").removeClass("visible");
  }
});

// Prevent hiding when clicking inside the search container
$("#search-container").on("click", function (e) {
  e.stopPropagation();
});
