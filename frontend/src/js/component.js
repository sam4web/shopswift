class Header extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
    <header class="dark:bg-body-dark transition"
    x-data="{navbarToggle: false}"
    >
    <nav class="bg-secondary-dark dark:bg-gray-dark transition">
      <div class="max-w-7xl w-full mx-auto px-4 lg:px-10 py-1.5">
        <ul
          class="text-light flex justify-center sm:justify-end space-x-6 text-sm md:text-[16px] font-light"
        >
          <li>
            <a href="./login.html" class="hover:underline">Sign in</a>
          </li>
          <li>
            <a href="./register.html" class="hover:underline">Create Account</a>
          </li>
        </ul>
      </div>
    </nav>
    <nav class="bg-light dark:bg-primary-dark transition">
      <div class="max-w-7xl w-full mx-auto px-4 lg:px-10 py-4">
        <div class="flex justify-between items-center">
          <h3 class="md:block hidden">
            <a
              href="./index.html"
              class="text-3xl lg:text-[34px] font-bold font-heading dark:text-light"
            >
              Shop<span class="text-primary">Swift</span>.
            </a>
          </h3>

          <ul class="hidden md:flex items-center">
            <li>
              <a class="nav-link" href="./index.html"> Home </a>
            </li>
            <li>
              <a class="nav-link" href="./about.html"> About </a>
            </li>
            <li>
              <a class="nav-link" href="./products.html"> Products </a>
            </li>
            <li>
              <a class="nav-link" href="./cart.html"> Cart </a>
            </li>

            <li>
              <a class="nav-link" href="./checkout.html"> Checkout </a>
            </li>
            <li>
              <a class="nav-link" href="./orders.html"> Orders </a>
            </li>
          </ul>

          <button class="block md:hidden" x-on:click="navbarToggle=!navbarToggle">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              stroke-width="1.5"
              stroke="currentColor"
              class="w-7 h-7 dark:text-light"
            >
              <path
                stroke-linecap="round"
                stroke-linejoin="round"
                d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25H12"
              />
            </svg>
          </button>

          <div class="flex items-center gap-5">
              <button id="toggle-btn">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="w-6 h-6 block dark:hidden"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z"
                  />
                </svg>
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="w-6 h-6 hidden dark:block text-light"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z"
                  />
                </svg>
              </button>
              <a href="">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                  stroke-width="1.5"
                  stroke="currentColor"
                  class="w-6 h-6 dark:text-light"
                >
                  <path
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    d="M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 0 0-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 0 0-16.536-1.84M7.5 14.25 5.106 5.272M6 20.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Zm12.75 0a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z"
                  />
                </svg>
              </a>
          </div>
        </div>
      </div>
    </nav>

    <nav
      x-bind:class="!navbarToggle && 'hidden'"
      class="bg-light dark:bg-primary-dark mt-2 max-w-[240px] mx-auto sm:ml-8 p-2 rounded-md md:hidden transition"
    >
      <ul class="space-y-2.5">
        <li>
          <a class="nav-link" href="./index.html"> Home </a>
        </li>
        <li>
          <a class="nav-link" href="./about.html"> About </a>
        </li>
        <li>
        <a class="nav-link" href="./products.html"> Products </a>
        </li>
        <li>
          <a class="nav-link" href="./cart.html"> Cart </a>
        </li>
      </ul>
    </nav>
  </header>
    `;
  }
}

class Footer extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `    
  <footer class="dark:bg-primary-dark bg-secondary-dark transition">
    <div class="py-6 px-4 text-center">
      <p class="text-light text-lg">
        &copy; ${new Date().getFullYear()}
        <span class="text-primary font-semibold">ShopSwift</span>. All
        rights reserved.
      </p>
    </div>
  </footer>`;
  }
}

customElements.define('app-header', Header);
customElements.define('app-footer', Footer);
