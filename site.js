/* Shared site behaviors: reveals, parallax hero, counters, marquee, gallery + lightbox */
(function () {
  "use strict";

  /* ---------- scroll reveals ---------- */
  var revealEls = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("visible"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add("visible"); });
  }

  /* ---------- parallax hero ---------- */
  var heroBg = document.querySelector(".hero-bg");
  if (heroBg && !window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    var ticking = false;
    window.addEventListener("scroll", function () {
      if (!ticking) {
        window.requestAnimationFrame(function () {
          var y = window.scrollY;
          if (y < window.innerHeight * 1.2) {
            heroBg.style.transform = "translateY(" + y * 0.28 + "px) scale(1.06)";
          }
          ticking = false;
        });
        ticking = true;
      }
    }, { passive: true });
    heroBg.style.transform = "scale(1.06)";
  }

  /* ---------- animated counters ---------- */
  var counters = document.querySelectorAll(".counter");
  function animateCounter(el) {
    var target = parseFloat(el.getAttribute("data-target"));
    var suffix = el.getAttribute("data-suffix") || "";
    var dur = 1600, start = null;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (p < 1) window.requestAnimationFrame(step);
    }
    window.requestAnimationFrame(step);
  }
  if ("IntersectionObserver" in window && counters.length) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { animateCounter(e.target); cio.unobserve(e.target); }
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { cio.observe(el); });
  }

  /* ---------- client logo marquee ---------- */
  var track = document.getElementById("marquee-track");
  if (track) {
    var logos = [];
    for (var i = 1; i <= 24; i++) {
      logos.push("logo-" + (i < 10 ? "0" + i : i) + ".png");
    }
    var loaded = 0;
    logos.forEach(function (src) {
      var img = new Image();
      img.onload = function () {
        img.alt = "Client logo";
        track.appendChild(img);
        loaded++;
        if (loaded === logos.length) {
          // duplicate for seamless loop
          track.innerHTML += track.innerHTML;
        }
      };
      img.src = src;
    });
  }

  /* ---------- gallery + lightbox ---------- */
  var grid = document.getElementById("gallery-grid");
  if (grid) {
    var box = document.createElement("div");
    box.className = "lightbox";
    var boxImg = document.createElement("img");
    box.appendChild(boxImg);
    document.body.appendChild(box);
    box.addEventListener("click", function () { box.classList.remove("open"); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") box.classList.remove("open");
    });
    for (var g = 1; g <= 8; g++) {
      (function (n) {
        var src = "gallery-0" + n + ".jpg";
        var probe = new Image();
        probe.onload = function () {
          var img = document.createElement("img");
          img.src = src;
          img.alt = "New York City photo " + n + " by Marina Kapler";
          img.loading = "lazy";
          img.addEventListener("click", function () {
            boxImg.src = src;
            box.classList.add("open");
          });
          grid.appendChild(img);
        };
        probe.src = src;
      })(g);
    }
  }
})();
