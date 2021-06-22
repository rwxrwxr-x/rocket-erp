<template>
  <footer class="footer">
    <div class="container-fluid">
      <ul class="nav">
        <li class="nav-item">
          <a
            href="about"
            target="_blank"
            rel="noopener"
            class="nav-link"
          >
            О проекте
          </a>
        </li>
        <li class="nav-item">
                  <div class="togglebutton switch-change-color">
            <span class="label-switch">LIGHT MODE</span>
            <base-switch v-model="darkMode" @input="toggleMode"></base-switch>
            <span class="label-switch label-right">DARK MODE</span>
          </div>
        </li>
      </ul>

      <div class="copyright">
        &copy; {{ year }}, based on

        <a
          href="https://github.com/creativetimofficial/nuxt-black-dashboard/"
          target="_blank"
          rel="noopener"
          >nuxt-black-dashboard</a
        >
        for a better web.
      </div>

    </div>
  </footer>
</template>
<script>
import { BaseSwitch } from '@/components';
export default {
  components: {
    BaseSwitch
  },
  data() {
    return {
      darkMode: true,
      year: new Date().getFullYear()
    };
  },
  methods: {
    toggleMode(type) {
        let docClasses = document.body.classList;
        if (type) {
          docClasses.remove('white-content');
        } else {
          docClasses.add('white-content');
        }
      },
  }
};
</script>
<style></style>
