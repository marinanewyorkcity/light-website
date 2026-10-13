/* Renders event cards from events.json in Marina's card style.
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
        '<p class="f"><b>Date</b> ' + esc(ev.dateText) + "</p>" +
        '<p class="f"><b>Time</b> ' + esc(ev.time) + "</p>" +
        '<p class="f"><b>Location</b> ' + esc(ev.location) + "</p>" +
        '<p class="f"><b>Price</b> ' + esc(ev.price) + "</p>" +
        '<p class="why"><b>Why visit:</b> ' + esc(ev.why) + "</p>" +
        '<p class="f"><b>Good for</b> ' + esc(ev.goodFor) + "</p>" +
        '<a class="off" href="' + esc(ev.url) + '" target="_blank" rel="noopener">Official information: View event details</a>' +
      "</article>"
    );
  }

  function todayISO() {
    var d = new Date();
    return d.getFullYear() + "-" + String(d.getMonth() + 1).padStart(2, "0") + "-" + String(d.getDate()).padStart(2, "0");
  }

  var MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"];
  function fmtRange(a, b) {
    // "October 12 to 18"
    var pa = a.split("-"), pb = b.split("-");
    var ma = MONTHS[parseInt(pa[1], 10) - 1], mb = MONTHS[parseInt(pb[1], 10) - 1];
    if (pa[1] === pb[1]) return ma + " " + parseInt(pa[2], 10) + " to " + parseInt(pb[2], 10);
    return ma + " " + parseInt(pa[2], 10) + " to " + mb + " " + parseInt(pb[2], 10);
  }

  fetch("events.json")
    .then(function (r) { return r.json(); })
    .then(function (events) {
      var today = todayISO();

      var picksGrid = document.getElementById("picks-grid");
      if (picksGrid) {
        var picks = events.filter(function (e) { return e.picks && e.end >= today; });
        if (!picks.length) picks = events.filter(function (e) { return e.picks; }).slice(0, 10);
        picksGrid.innerHTML = picks.map(cardHTML).join("");
        var datesEl = document.getElementById("picks-dates");
        if (datesEl && picks.length) {
          var starts = picks.map(function (e) { return e.start; }).sort();
          var ends = picks.map(function (e) { return e.end; }).sort();
          datesEl.textContent = fmtRange(starts[0], ends[ends.length - 1]);
        }
      }

      var monthGrid = document.getElementById("month-grid");
      if (monthGrid) {
        var month = monthGrid.getAttribute("data-month");
        var list = events
          .filter(function (e) { return e.months.indexOf(month) !== -1; })
          .sort(function (a, b) { return a.start < b.start ? -1 : 1; });
        monthGrid.innerHTML = list.map(cardHTML).join("");
      }

      var form = document.getElementById("planner-form");
      if (form) {
        var out = document.getElementById("planner-results");
        form.addEventListener("submit", function (ev) {
          ev.preventDefault();
          var a = document.getElementById("arrival").value;
          var d = document.getElementById("departure").value;
          if (!a || !d || d < a) {
            out.innerHTML = '<div class="planner-hit"><p>Please pick an arrival date and a departure date on or after it.</p></div>';
            return;
          }
          var hits = events.filter(function (e) {
            return e.start && e.end && e.start <= d && e.end >= a;
          }).sort(function (x, y) { return x.start < y.start ? -1 : 1; });
          if (!hits.length) {
            out.innerHTML = '<div class="planner-hit"><p>No events found for those dates. Try widening your trip, or browse the monthly guides.</p></div>';
            return;
          }
          out.innerHTML = hits.map(function (e) {
            return '<div class="planner-hit"><div><h4><a href="' + esc(e.url) + '" target="_blank" rel="noopener">' +
              esc(e.title) + "</a></h4><p>" + esc(e.dateText) + " · " + esc(e.location) + "</p></div>" +
              '<a class="off" href="' + esc(e.url) + '" target="_blank" rel="noopener">View event details</a></div>';
          }).join("");
        });
      }
    })
    .catch(function () {});
})();
