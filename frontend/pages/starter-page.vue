<template>
  <div class="row">
    <sidebar-plugin></sidebar-plugin>
    <h3>Starter page</h3></div>
</template>
<script>
import {SidebarPlugin} from "~/components";
  export default {
      middleware: 'auth',
    components: {
        SidebarPlugin,
    },
    name: 'starter-page',
    layout: 'starter',
    data() {
      return {};
    }
  };
</script>
<style></style>
