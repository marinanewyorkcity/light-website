/* Renders event cards from events.json: top picks, monthly grids, news list, trip planner.
   All outbound links open in a new tab. */
(function () {
  "use strict";

  function esc(s) {
    return String(s == null ? "" : s)
      .replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function cardHTML(ev) {
    return (
      '<article class="event-card">' +
        '<h3><a href="' + esc(ev.url) + '" target="_blank" rel="noopener">' + esc(ev.title) + "</a></h3>" +
        '<div class="event-meta">' +
          '<div class="row"><span class="mk">Date</span><br><strong>' + esc(ev.dateText) + "</strong></div>" +
          '<div class="row"><span class="mk">Time</span><br>' + esc(ev.time) + "</div>" +
          '<div class="row"><span class="mk">Location</span><br>' + esc(ev.location) + "</div>" +
          '<div class="row"><span class="mk">Price</span><br><strong>' + esc(ev.price) + "</strong></div>" +
        "</div>" +
        '<p class="event-why">' + esc(ev.why) + "</p>" +
        '<p class="event-good"><strong>Good for:</strong> ' + esc(ev.goodFor) + "</p>" +
        '<a class="event-link" href="' + esc(ev.url) + '" target="_blank" rel="noopener">Official information</a>' +
      "</article>"
    );
  }

  function todayISO() {
    var d = new Date();
    return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
  }

  fetch("events.json")
    .then(function (r) { return r.json(); })
    .then(function (events) {
      var today = todayISO();

      /* ----- top picks (hub) ----- */
      var picksGrid = document.getElementById("picks-grid");
      if (picksGrid) {
        var picks = events.filter(function (e) { return e.picks && e.end >= today; });
        if (!picks.length) {
          picks = events.filter(function (e) { return e.picks; }).slice(0, 6);
        }
        picksGrid.innerHTML = picks.map(cardHTML).join("");
      }

      /* ----- monthly grid ----- */
      var monthGrid = document.getElementById("month-grid");
      if (monthGrid) {
        var month = monthGrid.getAttribute("data-month");
        var list = events.filter(function (e) { return e.months.indexOf(month) !== -1; });
        list.sort(function (a, b) { return a.start < b.start ? -1 : 1; });
        monthGrid.innerHTML = list.map(cardHTML).join("");
      }

      /* ----- news list (home): next upcoming events ----- */
      var newsList = document.getElementById("news-list");
      if (newsList) {
        var upcoming = events
          .filter(function (e) { return e.end >= today; })
          .sort(function (a, b) { return a.start < b.start ? -1 : 1; })
          .slice(0, 5);
        newsList.innerHTML = upcoming.map(function (e) {
          return (
            '<article class="news-item">' +
              "<div><h3><a href=\"" + esc(e.url) + '" target="_blank" rel="noopener">' + esc(e.title) + "</a></h3>" +
              "<p>" + esc(e.dateText) + " · " + esc(e.location) + "</p></div>" +
              '<span class="news-date">' + esc(e.dateText) + "</span>" +
            "</article>"
          );
        }).join("");
      }

      /* ----- trip planner ----- */
      var form = document.getElementById("planner-form");
      if (form) {
        var err = document.getElementById("planner-error");
        var out = document.getElementById("planner-results");
        form.addEventListener("submit", function (ev) {
          ev.preventDefault();
          var a = document.getElementById("arrival").value;
          var d = document.getElementById("departure").value;
          if (!a || !d || d < a) {
            err.hidden = false;
            out.innerHTML = "";
            return;
          }
          err.hidden = true;
          var hits = events.filter(function (e) {
            return e.start && e.end && e.start <= d && e.end >= a;
          }).sort(function (x, y) { return x.start < y.start ? -1 : 1; });
          if (!hits.length) {
            out.innerHTML = '<div class="planner-hit"><div><h4>No events found for those dates</h4><p>Try widening your trip, or check the monthly guides.</p></div></div>';
            return;
          }
          out.innerHTML = hits.map(function (e) {
            return (
              '<div class="planner-hit"><div><h4><a href="' + esc(e.url) + '" target="_blank" rel="noopener">' +
              esc(e.title) + "</a></h4><p>" + esc(e.dateText) + " · " + esc(e.location) + " · " + esc(e.price) + "</p></div>" +
              '<a class="event-link" href="' + esc(e.url) + '" target="_blank" rel="noopener">Details</a></div>'
            );
          }).join("");
        });
      }
    })
    .catch(function () { /* events.json failed to load; sections stay empty */ });
})();
