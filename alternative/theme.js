/* Keep preview preferences separate from the existing site's theme. */
(() => {
  const root = document.documentElement;
  const preference = window.matchMedia("(prefers-color-scheme: dark)");
  let saved = null;
  try {
    saved = localStorage.getItem("alternative-theme");
  } catch (_) {
    // The file preview also works when storage is unavailable.
  }
  let theme = saved === "dark" || saved === "light" ? saved : preference.matches ? "dark" : "light";
  root.dataset.theme = theme;

  document.addEventListener("DOMContentLoaded", () => {
    const button = document.querySelector(".theme-toggle");
    if (!button) return;
    const update = () => {
      root.dataset.theme = theme;
      button.setAttribute("aria-label", `Switch to ${theme === "dark" ? "light" : "dark"} mode`);
      button.title = button.getAttribute("aria-label");
    };
    button.dataset.ready = "";
    update();
    button.addEventListener("click", () => {
      theme = theme === "dark" ? "light" : "dark";
      saved = theme;
      try { localStorage.setItem("alternative-theme", theme); } catch (_) {}
      update();
    });
    preference.addEventListener("change", event => {
      if (saved === "dark" || saved === "light") return;
      theme = event.matches ? "dark" : "light";
      update();
    });
  });
})();
