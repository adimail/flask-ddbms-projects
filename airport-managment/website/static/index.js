function deleteflight(flight_id) {
  fetch("/delete-flight", {
    method: "POST",
    body: JSON.stringify({ flight_id: flight_id }),
  }).then((_res) => {
    window.location.href = "/";
  });
}

function deletebooking(flight_id) {
  fetch("/delete-booking", {
    method: "POST",
    body: JSON.stringify({ flight_id: flight_id }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
