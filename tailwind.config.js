/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html", 
    "./*/templates/**/*.html", 
    "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      fontFamily:{
        "tajwal": ['Tajawal', 'sans-serif']
      },
      colors:{
        light:{
          base:"var(--text-base)",
          title:"var(--color--text-title)",
          primary:'var(--color-primary)',
          secondary:"var(--color-secondary)",
          bgcolor:"var(--bg-color)",
          bglight:"var(--bg--light-color)"

        }
      }
    },
  },
  plugins: [
    require("flowbite/plugin")
  ],
};
