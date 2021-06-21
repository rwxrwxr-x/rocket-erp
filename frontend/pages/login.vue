<template>
  <div>
    <!-- Page content -->
    <login-form></login-form>

  </div>
</template>
<script>
import LoginForm from "~/components/auth/LoginForm";

export default {
  layout: "starter",
  components: { LoginForm},
  middleware: 'noauth',
};
</script>