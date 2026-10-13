/* Shared behaviors: scroll reveals, client logo marquee */
(function () {
  "use strict";

  var els = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("visible"); io.unobserve(e.target); }
      });
    }, { threshold: 0.1 });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add("visible"); });
  }

  var track = document.getElementById("marquee-track");
  if (track) {
    var scriptSrc = (document.currentScript && document.currentScript.src) || "";
    var assetBase = scriptSrc.slice(0, scriptSrc.lastIndexOf("/") + 1);
    var logos = [];
    for (var i = 1; i <= 24; i++) {
      logos.push(assetBase + "logo-" + (i < 10 ? "0" + i : i) + ".png");
    }
    var pending = logos.length, ok = [];
    logos.forEach(function (name) {
      var probe = new Image();
      probe.onload = function () { ok.push(name); done(); };
      probe.onerror = function () { done(); };
      probe.src = name;
    });
    function done() {
      if (--pending) return;
      ok.sort();
      ok.forEach(function (name) {
        var img = document.createElement("img");
        img.src = name;
        img.alt = "Client logo";
        img.loading = "lazy";
        track.appendChild(img);
      });
      var more = document.createElement("span");
      more.textContent = "and more";
      more.style.cssText = "color:var(--cream);font-size:1.1rem;white-space:nowrap;align-self:center";
      track.appendChild(more);
      track.innerHTML += track.innerHTML; /* seamless loop */
    }
  }
})();
